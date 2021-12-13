# https://www.renpy.org/doc/html/screen_special.html
# based on the confirm screen

screen confirm_and_share_screen(title, message="Now that's an achievement unlocked!", ok_text="Gotta Unlock 'Em All!", tweet_content_url=tweet_default, show_achievements_count=True):

    # using `game menu root` will make this screen replace background image
    # modal True
    # window:
    #     style "gm_root"

    on "show" action renpy.sound.play('audio/sfx/confirm_and_share.wav')

    frame:
        style_prefix "confirm"

        xfill True
        xsize 1000
        # xmargin 50 # don't use this, otherwise {sc} tag overflows
        ypadding 30
        yalign .25

        vbox:
            xfill True
            spacing 25

            text _(title):
                xalign 0.5
                text_align 0.5
                color gui.accent_color
                size gui.label_text_size
                font gui.interface_text_font

            text _(message):
                xalign 0.5
                text_align 0.5

            if show_achievements_count:
                $ num_achievements = len(persistent.achievements)
                text _("Number of Achievements Unlocked: [num_achievements] / [total_num_achievements]"):
                    xalign 0.5

            textbutton "{icon=icon-twitter} " + _("Tweet this"):
                xalign 0.5
                action OpenURL(tweet_content_url)

            textbutton ok_text:
                xalign 0.5
                action [
                Notify("This achievement is saved to the Bonus menu. Feel free tweet about it later if you haven't!"),
                Return()
                ]