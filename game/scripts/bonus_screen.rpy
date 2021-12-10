screen bonus_screen():
    tag menu
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Bonus"), scroll="viewport"):
        style_prefix "bonus"
        vbox:
            spacing 15
            
            label 'Bonus Content'
            textbutton '{icon=icon-award} ' + _("Achievements") action Show('achievements_screen')
            textbutton '{icon=icon-headphones} ' + _("Music Room") action Show('music_room_screen')
            # textbutton '{icon=icon-book-open} ' + _("Glossary") action Show('glossary_screen')
            # textbutton '{icon=icon-code} ' + _("Quiz Collection") action Show('quiz_screen')

            null height 20

            label 'Videos'
            # TODO: play game trailer from YouTube
            textbutton '{icon=icon-film} ' + _("Game Trailer") action NullAction()
            textbutton '{icon=icon-youtube} ' + _("Learn to Code RPG: The Making of") action NullAction()

            null height 20
            label 'Mini Games'
            textbutton '{icon=icon-music} ' + _("Rhythm Game") action Start('rhythm_game_entry_label')
            # TODO: more mini games, quiz speedrun survival mode etc.

            null height 20
            label 'Awesome freeCodeCamp Resources'
            textbutton '{icon=icon-youtube} ' + _("freeCodeCamp YouTube Channel") action OpenURL("https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            textbutton '{icon=icon-map} ' + _("freeCodeCamp Curriculum") action OpenURL("https://www.freecodecamp.org/learn/")
            textbutton '{icon=icon-compass} ' + _("freeCodeCamp Forum") action OpenURL("https://forum.freecodecamp.org/")
            textbutton '{icon=icon-coffee} ' + _("freeCodeCamp Code Radio") action OpenURL("https://coderadio.freecodecamp.org/")
            textbutton '{icon=icon-edit-3} ' + _("freeCodeCamp Style Guide") action OpenURL("https://design-style-guide.freecodecamp.org/")

screen achievements_screen():
    tag menu
    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "bonus"

        $ num_achievements = len(persistent.achievements)
        text _("Number of Easter Eggs unlocked: [num_achievements] / [total_num_achievements]"):
            xalign 0.5

        vbox:
            spacing 50
            for category in [plot_achievement, plot_bonus, quiz_bonus, ending_achievement]:
                vbox:
                    spacing 15
                    label category

                    $ achievement_to_tweet_map = achievement_labels_map[category]
                    grid 2 len(achievement_to_tweet_map):
                        xspacing 60

                        for achievement in sorted(achievement_to_tweet_map.keys()):
                            $ is_unlocked = (achievement in persistent.achievements)

                            if is_unlocked:
                                $ tweet = achievement_to_tweet_map[achievement]
                                text '{icon=icon-unlock} [achievement]'
                                textbutton '{icon=icon-twitter} Tweet this' action OpenURL(tweet)
                            else:
                                text '{icon=icon-lock} ???'
                                null

# https://www.renpy.org/doc/html/rooms.html
screen music_room_screen():
    # this is called from the menu
    tag menu
    use game_menu(_("Music Room"), scroll="viewport"):
        style_prefix "bonus"
        vbox:
            spacing 10
            xalign 0.5

            hbox:
                spacing 20
                # Buttons that let us advance tracks.
                textbutton _("Previous") + ' {icon=icon-arrow-left-circle}' action music_room.Previous()
                textbutton '{icon=icon-arrow-right-circle} ' + _("Next") action music_room.Next()
                # textbutton "Pause" action music_room.TogglePause()
                null width 40
                textbutton '{icon=icon-stop-circle} ' + _("Stop") action music_room.Stop()

            null height 20

            label _('All Tracks')
            # The buttons that play each track.
            for track in all_music_tracks:
                $ file = all_music_tracks[track]
                textbutton '{icon=icon-headphones} ' + track action music_room.Play(file)

screen music_room_screen_in_script():
    # this is called inside renpy scripts
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 80
        ypadding 30
        background white80

        vbox:
            spacing 10
            xalign 0.5

            hbox:
                spacing 20
                # Buttons that let us advance tracks.
                textbutton _("Previous") + ' {icon=icon-arrow-left-circle}' action music_room.Previous()
                textbutton '{icon=icon-arrow-right-circle} ' + _("Next") action music_room.Next()
                # textbutton "Pause" action music_room.TogglePause()
                null width 40
                textbutton '{icon=icon-stop-circle} ' + _("Stop") action music_room.Stop()

            null height 20

            label _('All Tracks')
            # The buttons that play each track.
            for track in all_music_tracks:
                $ file = all_music_tracks[track]
                textbutton '{icon=icon-headphones} ' + track action music_room.Play(file)

            null height 20
            # The button that lets the user exit the music room.
            textbutton '{icon=icon-x-circle} ' + _("Exit") action Return()

    # # Start the music playing on entry to the music room.
    # on "replace" action music_room.Play()

    # # Restore the main menu music upon leaving.
    # on "replaced" action Play("music", config.main_menu_music)

# TODO: v2
screen glossary_screen():
    tag menu
    use game_menu(_("Glossary"), scroll="viewport"):
        style_prefix "bonus"
        text "Coming in v2!"

# TODO: v2
screen quiz_screen():
    tag menu
    use game_menu(_("Quiz Questions"), scroll="viewport"):
        style_prefix "bonus"
        text "Coming in v2!"

style bonus_label is gui_label
style bonus_label_text is gui_label_text
style bonus_text is gui_text

style bonus_label_text:
    size gui.label_text_size