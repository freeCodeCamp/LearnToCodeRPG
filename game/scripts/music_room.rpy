# https://www.renpy.org/doc/html/rooms.html

screen music_room_screen():

    tag menu

    frame:
        has vbox

        # The buttons that play each track.
        for track in all_music_tracks:
            $ file = all_music_tracks[track]
            textbutton track action music_room.Play(file)

        null height 20

        # Buttons that let us advance tracks.
        textbutton "Next" action music_room.Next()
        textbutton "Previous" action music_room.Previous()

        null height 20

        # The button that lets the user exit the music room.
        textbutton "Exit" action Hide('music_room_screen')

    # Start the music playing on entry to the music room.
    on "replace" action music_room.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", config.main_menu_music)