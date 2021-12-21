# https://github.com/RuolinZheng08/renpy-rhythm

# music channel for renpy.play
define CHANNEL_RHYTHM_GAME = 'CHANNEL_RHYTHM_GAME'

# scores for Good and Perfect hits
define SCORE_GOOD = 60
define SCORE_PERFECT = 100

# the song that the player chooses to play, set in `select_song_screen` below
default selected_song = None

screen select_song_screen(songs):

    default cell_size = (380, 80)

    frame:
        xalign 0.5
        yalign 0.25
        xpadding 80
        ypadding 30
        background white80

        vbox:
            spacing 20

            label "Click on a song to play" xalign 0.5

            null height 20

            vpgrid:

                cols 3
                rows len(songs) + 1
                spacing 10
                draggable True
                mousewheel True
                ymaximum 760

                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                # Since we have scrollbars, we have to position the side, rather
                # than the vpgrid proper.
                side_xalign 0.5

                # header row
                label '{icon=icon-music} ' + _('Song Name') xysize cell_size
                label '{icon=icon-chevrons-up} ' + _('Highest Score') xysize cell_size
                label '{icon=icon-star} ' + _('% Perfect Score') xysize cell_size

                # body rows
                for song in songs:
                    textbutton song.name:
                        xysize cell_size
                        action [
                        Return(song)
                        ]
                    $ highest_score, highest_percent = persistent.rhythm_game_high_scores[song.name]
                    text str(highest_score) xysize cell_size xalign 0.5
                    text '[highest_percent]%' xysize cell_size xalign 0.5

            textbutton '{icon=icon-x-circle} ' + _("Exit"):
                xalign 0.5
                action Return(None)

screen rhythm_game(rhythm_game_displayable):

    zorder 103 # always on top, covering textbox, quick_menu, calendar, etc.

    # disable the arrow keys from activating the Quit button
    # https://www.renpy.org/doc/html/screens.html#key
    key 'K_LEFT' action NullAction()
    key 'K_UP' action NullAction()
    key 'K_DOWN' action NullAction()
    key 'K_RIGHT' action NullAction()

    add Solid('#000')
    add rhythm_game_displayable

    vbox:
        xpos 50
        ypos 50
        spacing 20

        textbutton '{icon=icon-x-circle} Quit' action [
        Confirm('Would you like to quit the rhythm game?',
            yes=[
            Stop(CHANNEL_RHYTHM_GAME), # stop the music on this channel
            Return(rhythm_game_displayable.score)
            ])]:
            # force the button text to be white when hovered
            text_hover_color '#fff'

        text rhythm_game_displayable.song_name:
            color '#fff'
            size 30
            xmaximum 300

        # can also use has_music_started so this won't show during the silence
        showif rhythm_game_displayable.has_game_started:
            text 'Score: ' + str(rhythm_game_displayable.score):
                color '#fff'
                size 40

    ## XXX: for some reason, the bar is not accurate for some audio files
    # # use has_music_started, do not use has_game_started, b/c we are still in silence
    showif rhythm_game_displayable.has_music_started:
        bar:
            xalign 0.5
            ypos 20
            xsize 740
            value AudioPositionValue(channel=CHANNEL_RHYTHM_GAME)

    # return the number of hits and total number of notes to the main game
    if rhythm_game_displayable.has_ended:
        # use a timer so the player can see the screen before it returns
        timer 2.0 action Return(rhythm_game_displayable.score)

## end screen definition

init python:

    # register channel
    renpy.music.register_channel(CHANNEL_RHYTHM_GAME)

    import os
    import pygame

    # util func
    def read_beatmap_file(beatmap_path):
        # read newline separated floats
        beatmap_path_full = os.path.join(config.gamedir, beatmap_path)
        with open(beatmap_path_full, 'rt') as f:
            text = f.read()
        onset_times = [float(string) for string in text.split('\n') if string != '']
        return onset_times

    class Song():
        def __init__(self, name, audio_path, beatmap_path, beatmap_stride=2):
            # beatmap_stride (int): Default to 2. Use onset_times[::beatmap_stride] so that the tracks don't get too crowded. Can be used to set difficulty level
            self.name = name
            self.audio_path = audio_path
            self.beatmap_path = beatmap_path

            # can skip onsets to adjust difficulty level
            # skip every other onset so the display is less dense
            self.onset_times = read_beatmap_file(beatmap_path)[::beatmap_stride]
            self.max_score = len(self.onset_times) * SCORE_PERFECT

        def compute_percent(self, score):
            return round(score / float(self.max_score) * 100)
    
    class RhythmGameDisplayable(renpy.Displayable):

        def __init__(self, song):
            """
            song (Song object)
            """
            super(RhythmGameDisplayable, self).__init__()

            self.audio_path = song.audio_path
            self.song_name = song.name

            self.has_game_started = False
            self.has_music_started = False # this happens after `self.silence_offset_start`
            self.has_ended = False
            # the first st
            # an offset is necessary because there might be a delay between when the
            # displayable first appears on screen and the time the music starts playing
            # seconds, same unit as st, shown time
            self.time_offset = None

            # silence before the music plays, in seconds
            self.silence_offset_start = 4.5
            self.silence_start = '<silence %s>' % str(self.silence_offset_start)
            # count down before the music plays, in seconds
            self.countdown = 3.0

            # define some values for offsets, height and width
            # of each element on screen

            # offset from the left of the screen
            self.x_offset = 400
            self.track_bar_height = int(config.screen_height * 0.85)
            self.track_bar_width = 12
            self.horizontal_bar_height = 8

            self.note_width = 75 # width of the note image
            # zoom in on the note when it is hittable
            self.zoom_scale = 1.2
            # offset the note to the right so it shows at the center of the track
            self.note_xoffset = (self.track_bar_width - self.note_width) / 2
            self.note_xoffset_large = (self.track_bar_width - self.note_width * self.zoom_scale) / 2
            # place the hit text some spacing from the end of the track bar
            self.hit_text_yoffset = 30

            # since the notes are scrolling from the screen top to bottom
            # they appear on the tracks prior to the onset time
            # this scroll time is also the note's entire lifespan time before it's either
            # hit or considered a miss
            # the note now takes 3 seconds to travel the screen
            # can be used to set difficulty level of the game
            self.note_offset = 3.0
            # speed = distance / time
            self.note_speed = config.screen_height / self.note_offset

            # number of track bars
            self.num_track_bars = 4
            # drawing position
            self.track_bar_spacing = (config.screen_width - self.x_offset * 2) / (self.num_track_bars - 1)
            # the xoffset of each track bar
            self.track_xoffsets = {
            track_idx: self.x_offset + track_idx * self.track_bar_spacing
            for track_idx in range(self.num_track_bars)
            }

            # define the notes' onset times
            self.onset_times = song.onset_times
            # assign notes to tracks, same length as self.onset_times
            # renpy.random.randint is upper-inclusive
            self.random_track_indices = [
            renpy.random.randint(0, self.num_track_bars - 1) for _ in range(len(self.onset_times))
            ]

            # map track_idx to a list of active note timestamps
            self.active_notes_per_track = {
            track_idx: [] for track_idx in range(self.num_track_bars)
            }

            # detect and record score
            # map onset timestamp to whether it has been hit, initialized to False
            self.onset_hits = {
            onset: None for onset in self.onset_times
            }
            self.score = 0
            # if the note is hit within 0.3 seconds of its actual onset time
            # we consider it a hit
            # can set different threshold for Good, Great hit scoring
            # miss if you hit the note too early, 0.1 second window before note becomes hittable
            self.prehit_miss_threshold = 0.4 # seconds
            self.hit_threshold = 0.3 # seconds
            self.perfect_threshold = 0.18 # seconds
            # therefore good is btw/ hit and perfect

            ## visual explanation
            #     miss       good       perfect    good      miss
            # (-0.4, -0.3)[-0.3, -0.1)[-0.1, 0.1](0.1, 0.3](0.3, inf)

            # map pygame key code to track idx
            self.keycode_to_track_idx = {
            pygame.K_LEFT: 0,
            pygame.K_UP: 1,
            pygame.K_DOWN: 2,
            pygame.K_RIGHT: 3
            }

            # define the drawables
            self.miss_text_drawable = Text('Miss!', color='#fff', size=30)
            self.good_text_drawable = Text('Good!', color='#fff', size=40)
            self.perfect_text_drawable = Text('Perfect!', color='#fff', size=50)
            self.track_bar_drawable = Solid('#fff', xsize=self.track_bar_width, ysize=self.track_bar_height)
            self.horizontal_bar_drawable = Solid('#fff', xsize=config.screen_width, ysize=self.horizontal_bar_height)
            # map track_idx to the note drawable
            self.note_drawables = {
            0: Image('others/rhythm_minigame/left.png'),
            1: Image('others/rhythm_minigame/up.png'),
            2: Image('others/rhythm_minigame/down.png'),
            3: Image('others/rhythm_minigame/right.png')
            }
            self.note_drawables_large = {
            0: Transform(self.note_drawables[0], zoom=self.zoom_scale),
            1: Transform(self.note_drawables[1], zoom=self.zoom_scale),
            2: Transform(self.note_drawables[2], zoom=self.zoom_scale),
            3: Transform(self.note_drawables[3], zoom=self.zoom_scale),
            }

            # record all the drawables for self.visit
            self.drawables = [
            self.miss_text_drawable,
            self.good_text_drawable,
            self.perfect_text_drawable,
            self.track_bar_drawable,
            self.horizontal_bar_drawable,
            ]
            self.drawables.extend(list(self.note_drawables.values()))
            self.drawables.extend(list(self.note_drawables_large.values()))

            ## after all intializations are done, start playing music
            self.play_music()

        def render(self, width, height, st, at):
            """
            st: A float, the shown timebase, in seconds. 
            The shown timebase begins when this displayable is first shown on the screen.
            """
            # cache the first st, when this displayable is first shown on the screen
            # this allows us to compute subsequent times when the notes should appear
            if self.has_game_started and self.time_offset is None:
                self.time_offset = self.silence_offset_start + st

            render = renpy.Render(width, height)

            # draw the countdown if we are still in the silent phase before the music starts
            # count down silence_offset_start, 3 seconds, while silence
            if not self.has_music_started:
                countdown_text = None
                time_before_music = self.countdown - st
                if time_before_music > 2.0:
                    countdown_text = '3'
                elif time_before_music > 1.0:
                    countdown_text = '2'
                elif time_before_music > 0.0:
                    countdown_text = '1'
                else: # no longer in countdown mode
                    self.has_music_started = True
                    renpy.restart_interaction() # force refresh the screen to display the progress bar
                    
                if countdown_text is not None:
                    render.place(Text(countdown_text, color='#fff', size=48),
                        x=config.screen_width / 2, y=config.screen_height / 2)

            # draw the rhythm game if we are playing the music
            # draw the vertical tracks
            for track_idx in range(self.num_track_bars):
                # look up the offset for drawing
                x_offset = self.track_xoffsets[track_idx]
                # y = 0 starts from the top
                render.place(self.track_bar_drawable, x=x_offset, y=0)

            # draw the horizontal bar to indicate where the track ends
            # x = 0 starts from the left
            render.place(self.horizontal_bar_drawable, x=0, y=self.track_bar_height)

            # draw the notes
            if self.has_game_started:
                # self.time_offset cannot be None down here b/c it has been set above
                # check if the song has ended
                if renpy.music.get_playing(channel=CHANNEL_RHYTHM_GAME) is None:
                    self.has_ended = True
                    renpy.timeout(0) # raise an event
                    return render

                # the number of seconds the song has been playing
                # is the difference between the current shown time and the cached first st
                curr_time = st - self.time_offset

                # update self.active_notes_per_track
                self.active_notes_per_track = self.get_active_notes_per_track(curr_time)

                # render notes on each track
                for track_idx in self.active_notes_per_track:
                    # look up track xoffset
                    x_offset = self.track_xoffsets[track_idx]

                    # loop through active notes
                    for onset, note_timestamp in self.active_notes_per_track[track_idx]:
                        # render the notes that are active and haven't been hit
                        if self.onset_hits[onset] is None:
                            # zoom in on the note if it is within the hit threshold
                            if abs(curr_time - onset) <= self.hit_threshold:
                                note_drawable = self.note_drawables_large[track_idx]
                                note_xoffset = x_offset + self.note_xoffset_large 
                            else:
                                note_drawable = self.note_drawables[track_idx]
                                note_xoffset = x_offset + self.note_xoffset

                            # compute where on the vertical axes the note is
                            # the vertical distance from the top that the note has already traveled
                            # is given by time * speed
                            note_distance_from_top = note_timestamp * self.note_speed
                            y_offset = self.track_bar_height - note_distance_from_top
                            render.place(note_drawable, x=note_xoffset, y=y_offset)

                        elif self.onset_hits[onset] == 'miss':
                            render.place(self.miss_text_drawable, x=x_offset, y=self.track_bar_height + self.hit_text_yoffset)
                        # else show hit text
                        elif self.onset_hits[onset] == 'good':
                            render.place(self.good_text_drawable, x=x_offset, y=self.track_bar_height + self.hit_text_yoffset)
                        elif self.onset_hits[onset] == 'perfect':
                            render.place(self.perfect_text_drawable, x=x_offset, y=self.track_bar_height + self.hit_text_yoffset)

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            if self.has_ended:
                # refresh the screen
                renpy.restart_interaction()
                return

            # no need to process the event
            if not self.has_game_started or self.time_offset is None:
                return

            # check if some keys have been pressed
            if ev.type == pygame.KEYDOWN:
                # only handle the four keys we defined
                if not ev.key in self.keycode_to_track_idx:
                    return
                # look up the track that correponds to the key pressed
                track_idx = self.keycode_to_track_idx[ev.key]

                active_notes_on_track = self.active_notes_per_track[track_idx]
                curr_time = st - self.time_offset

                # loop over active notes to check if one is hit
                for onset, _ in active_notes_on_track:
                    if self.onset_hits[onset] is not None: # status already determined, one of miss, good, perfect
                        continue

                    # compute the time difference between when the key is pressed
                    # and when we consider the note hittable as defined by self.hit_threshold

                    ## visual explanation
                    #     miss       good       perfect    good      miss
                    # (-0.4, -0.3)[-0.3, -0.1)[-0.1, 0.1](0.1, 0.3](0.3, inf)

                    # time diff btw/ curr time and actual onset
                    time_delta = curr_time - onset

                    ## any of the events below makes the note disappear from the screen
                    # from narrowest range to widest range

                    # perfect
                    if -self.perfect_threshold <= time_delta <= self.perfect_threshold:
                                            self.onset_hits[onset] = 'perfect'
                                            self.score += SCORE_PERFECT
                                            # redraw immediately because now the note should disappear from screen
                                            renpy.redraw(self, 0)
                                            # refresh the screen
                                            renpy.restart_interaction()

                    # good
                    elif (-self.hit_threshold <= time_delta < self.perfect_threshold) or \
                    (self.perfect_threshold < time_delta <= self.hit_threshold):
                        self.onset_hits[onset] = 'good'
                        self.score += SCORE_GOOD
                        # redraw immediately because now the note should disappear from screen
                        renpy.redraw(self, 0)
                        # refresh the screen
                        renpy.restart_interaction()

                    # miss
                    elif (-self.prehit_miss_threshold <= time_delta < -self.hit_threshold):
                        self.onset_hits[onset] = 'miss'
                        # no change to score
                        # redraw immediately because now the note should disappear from screen
                        renpy.redraw(self, 0)
                        # refresh the screen
                        renpy.restart_interaction()


        def visit(self):
            return self.drawables

        def play_music(self):
            # play slience first, followed by music
            renpy.music.queue([self.silence_start, self.audio_path], channel=CHANNEL_RHYTHM_GAME, loop=False)
            self.has_game_started = True

        def get_active_notes_per_track(self, current_time):
            active_notes = {
            track_idx: [] for track_idx in range(self.num_track_bars)
            }

            for onset, track_idx in zip(self.onset_times, self.random_track_indices):
                # determine if this note should appear on the track
                time_before_appearance = onset - current_time
                if time_before_appearance < 0: # already below the bottom of the screen
                    continue
                # should be on screen
                # recall that self.note_offset is 3 seconds, the note's lifespan
                elif time_before_appearance <= self.note_offset:
                    active_notes[track_idx].append((onset, time_before_appearance))
                # there is still time before the next note should show
                # break out of the loop so we don't process subsequent notes that are even later
                elif time_before_appearance > self.note_offset:
                    break

            return active_notes


    ## rhythm game
    # define the song titles and their files
    rhythm_game_songs = [
    Song(
        "Can't Stop Me. Can't Even Slow Me Down",
        "audio/rhythm_game/Can't Stop Me. Can't Even Slow Me Down.mp3", 
        "audio/rhythm_game/Can't Stop Me. Can't Even Slow Me Down.beatmap.txt", 
        ),
    Song(
        'Chasing That Feeling', 
        'audio/rhythm_game/Chasing That Feeling.mp3', 
        'audio/rhythm_game/Chasing That Feeling.beatmap.txt'
        ),
    Song(
        'Cruising for a Musing', 
        'audio/rhythm_game/Cruising for a Musing.mp3', 
        'audio/rhythm_game/Cruising for a Musing.beatmap.txt'
        ),
    Song(
        'Crystalize That Inner Child', 
        'audio/rhythm_game/Crystalize That Inner Child.mp3', 
        'audio/rhythm_game/Crystalize That Inner Child.beatmap.txt'
        ),
    Song(
        'From the Ground Up', 
        'audio/rhythm_game/From the Ground Up.mp3', 
        'audio/rhythm_game/From the Ground Up.beatmap.txt'
        ),
    Song(
        'Never Not Favored', 
        'audio/rhythm_game/Never Not Favored.mp3', 
        'audio/rhythm_game/Never Not Favored.beatmap.txt'
        ),
    Song(
        'Press Your Advantage', 
        'audio/rhythm_game/Press Your Advantage.mp3', 
        'audio/rhythm_game/Press Your Advantage.beatmap.txt'
        ),
    Song(
        'Scratching The Surface', 
        'audio/rhythm_game/Scratching The Surface.mp3', 
        'audio/rhythm_game/Scratching The Surface.beatmap.txt'
        ),
    Song(
        'Still Learning', 
        'audio/rhythm_game/Still Learning.mp3', 
        'audio/rhythm_game/Still Learning.beatmap.txt'
        ),
    Song(
        'We Are Going to Make it', 
        'audio/rhythm_game/We Are Going to Make it.mp3', 
        'audio/rhythm_game/We Are Going to Make it.beatmap.txt'
        ),
    ]
    # must be persistent to be able to record the scores
    if persistent.rhythm_game_high_scores is None:
        persistent.rhythm_game_high_scores = {
        song.name: (0, 0) for song in rhythm_game_songs
    }
    else: # in case we need to add songs
        for song in rhythm_game_songs:
            if not song in persistent.rhythm_game_high_scores:
                persistent.rhythm_game_high_scores[song.name] = (0, 0)

## end init python

label rhythm_game_entry_label:
    scene bg bedroom

    # stop the bgm
    # $ continue_looping_music = False
    stop music fadeout 1.0

    call screen select_song_screen(rhythm_game_songs)
    $ selected_song = _return

    # the select_song_screen will show at the bottom of this loop
    # if the player exits, selected_song becomes None and we exit out of the loop
    while isinstance(selected_song, Song):
        
        # avoid rolling back and losing game state
        $ renpy.block_rollback()

        # disable Esc key menu to prevent the player from saving the game
        $ _game_menu_screen = None

        $ renpy.notify('Use the arrow keys on your keyboard to hit the notes as they reach the end of the tracks. Good luck!')
        $ rhythm_game_displayable = RhythmGameDisplayable(selected_song)
        call screen rhythm_game(rhythm_game_displayable)
        $ new_score = _return
        $ del rhythm_game_displayable

        # XXX: old_percent is not used, but doing `old_score, _` causes pickling error
        $ old_score, old_percent = persistent.rhythm_game_high_scores[selected_song.name]

        if new_score > old_score:
            # compute new percent
            $ new_percent = selected_song.compute_percent(new_score)
            $ persistent.rhythm_game_high_scores[selected_song.name] = (new_score, new_percent)

            if old_score != 0: # high score only counts if we have a non-zero old score
                $ renpy.notify('New high score!')
                if not plot_rhythm_highscore in persistent.achievements:
                    $ add_achievement(plot_rhythm_highscore)

            # to get to 90 percent, need 3/4 perfect (100 pt each) and 1/4 good (60 pt each)
            if new_percent > 95:
                # check if one perfect
                if not plot_rhythm_perfect in persistent.achievements:
                    $ add_achievement(plot_rhythm_perfect)

                # check if all perfect
                python:
                    all_perfect = True
                    for score, percent in persistent.rhythm_game_high_scores.values():
                        if not percent > 95:
                            all_perfect &= False
                        else:
                            all_perfect &= True
                if all_perfect and \
                not plot_rhythm_perfect_all in persistent.achievements:
                    $ add_achievement(plot_rhythm_perfect_all)

        # re-enable the Esc key menu
        $ _game_menu_screen = 'save'

        # avoid rolling back and entering the game again
        $ renpy.block_rollback()

        # restore rollback from this point on
        $ renpy.checkpoint()

        # show high score only, not playable
        call screen select_song_screen(rhythm_game_songs)
        $ selected_song = _return

    # first time
    if not plot_rhythm_discover in persistent.achievements:
        $ add_achievement(plot_rhythm_discover)

    # resume the bgm
    # $ continue_looping_music = True
    $ random.shuffle(all_music_files)
    $ renpy.music.queue(all_music_files, loop=True, fadein=1.0, tight=True)

    return