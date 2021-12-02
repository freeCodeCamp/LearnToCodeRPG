screen rhythm_game(audio_path, beatmap_path):
    default rhythm_game_displayble = RhythmGameDisplayable(audio_path, beatmap_path)

    add Solid('#000')
    add rhythm_game_displayble

    vbox:
        xpos 50
        ypos 50
        spacing 10
        # show the score heads-up display (HUD)
        text 'Hits: ' + str(rhythm_game_displayble.num_hits):
            color '#fff'
        textbutton '{icon=icon-x-circle} Quit' action [
        Confirm('Would you like to quit the rhythm game?',
            yes=[
            Stop('rhythm_game'),
            Play('sound', 'audio/sfx/phone_hangup.wav'),
            Return(
                (rhythm_game_displayble.num_hits, rhythm_game_displayble.num_notes)
                )
            ])]:
            text_hover_color '#fff'


    # return the number of hits and total number of notes to the main game
    if rhythm_game_displayble.has_ended:
        # use a timer so the player can see the screen before it returns
        timer 2.0 action Return(
            (rhythm_game_displayble.num_hits, rhythm_game_displayble.num_notes)
            )

init python:

    # register channel
    renpy.music.register_channel('rhythm_game')

    import os
    import pygame
    
    class RhythmGameDisplayable(renpy.Displayable):

        def __init__(self, audio_path, beatmap_path):
            super(RhythmGameDisplayable, self).__init__()

            self.audio_path = audio_path

            self.has_started = False
            self.has_ended = False
            # the first st
            # an offset is necessary because there might be a delay between when the
            # displayable first appears on screen and the time the music starts playing
            # seconds, same unit as st, shown time
            self.time_offset = None

            # define some values for offsets, height and width
            # of each element on screen

            # offset from the left of the screen
            self.x_offset = 400
            self.track_bar_height = int(config.screen_height * 0.85)
            self.track_bar_width = 12
            self.horizontal_bar_height = 8

            self.note_width = 75
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
            self.onset_times = self.read_beatmap_file(beatmap_path)
            # can skip onsets to adjust difficulty level
            # skip every other onset so the display is less dense
            self.onset_times = self.onset_times[::2]

            self.num_notes = len(self.onset_times)
            # assign notes to tracks, same length as self.onset_times
            # renpy.random.randint is upper-inclusive
            self.random_track_indices = [
            renpy.random.randint(0, self.num_track_bars - 1) for _ in range(self.num_notes)
            ]

            # map track_idx to a list of active note timestamps
            self.active_notes_per_track = {
            track_idx: [] for track_idx in range(self.num_track_bars)
            }

            # detect and record hits
            # map onset timestamp to whether it has been hit, initialized to False
            self.onset_hits = {
            onset: False for onset in self.onset_times
            }
            self.num_hits = 0
            # if the note is hit within 0.3 seconds of its actual onset time
            # we consider it a hit
            # can set different threshold for Good, Great hit scoring
            self.hit_threshold = 0.3 # seconds

            # map pygame key code to track idx
            self.keycode_to_track_idx = {
            pygame.K_LEFT: 0,
            pygame.K_UP: 1,
            pygame.K_DOWN: 2,
            pygame.K_RIGHT: 3
            }

            # define the drawables
            self.hit_text_drawable = Text('Hit!', color='#fff')
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
            self.hit_text_drawable,
            self.track_bar_drawable,
            self.horizontal_bar_drawable,
            ]
            self.drawables.extend(list(self.note_drawables.values()))
            self.drawables.extend(list(self.note_drawables_large.values()))

        def render(self, width, height, st, at):
            """
            st: A float, the shown timebase, in seconds. 
            The shown timebase begins when this displayable is first shown on the screen.
            """
            # cache the first st, when this displayable is first shown on the screen
            # this allows us to compute subsequent times when the notes should appear
            if self.time_offset is None:
                self.time_offset = st
                # play music here
                renpy.music.play(self.audio_path, channel='rhythm_game', loop=False)
                self.has_started = True

            render = renpy.Render(width, height)

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
            if self.has_started:
                # check if the song has ended
                if renpy.music.get_playing(channel='rhythm_game') is None:
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
                        if self.onset_hits[onset] is False:
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
                        else:
                            # show hit text
                            render.place(self.hit_text_drawable, x=x_offset, y=self.track_bar_height + self.hit_text_yoffset)

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            if self.has_ended:
                # refresh the screen
                renpy.restart_interaction()
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
                    # compute the time difference between when the key is pressed
                    # and when we consider the note hittable as defined by self.hit_threshold
                    if abs(curr_time - onset) <= self.hit_threshold:
                        self.onset_hits[onset] = True
                        self.num_hits += 1
                        # redraw immediately because now the note should disappear from screen
                        renpy.redraw(self, 0)
                        # refresh the screen
                        renpy.restart_interaction()

        def visit(self):
            return self.drawables

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

        def read_beatmap_file(self, beatmap_path):
            # read newline separated floats
            beatmap_path_full = os.path.join(config.gamedir, beatmap_path)
            with open(beatmap_path_full, 'rt') as f:
                text = f.read()
            onset_times = [float(string) for string in text.split('\n') if string != '']
            return onset_times

    rhythm_game_beatmaps = {
        'Chasing That Feeling': (
            'audio/bgm/Chasing That Feeling.mp3',
            'audio/bgm/Chasing That Feeling.beatmap.txt'
            ),
        'Crystalize That Child in Me': (
            'audio/bgm/Crystalize That Child in Me.mp3',
            'audio/bgm/Crystalize That Child in Me.beatmap.txt'
            ),
        'Never Not Favored': (
            'audio/bgm/Never Not Favored.mp3',
            'audio/bgm/Never Not Favored.beatmap.txt'
            ),
        'Press Your Advantage': (
            'audio/bgm/Press Your Advantage.mp3',
            'audio/bgm/Press Your Advantage.beatmap.txt'
            )
    }