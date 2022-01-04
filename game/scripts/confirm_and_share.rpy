# https://www.renpy.org/doc/html/screen_special.html
# based on the confirm screen

define alternative_endind_message = _("Congratulations! You just discovered an alternative ending.")

screen confirm_and_share_screen(title, message=None, ok_text=None, tweet_content_url=tweet_default, show_achievements_count=True):

    # using `game menu root` will make this screen replace background image
    # modal True
    # window:
    #     style "gm_root"
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

            if message is None:
                $ message = _("Now that's an achievement unlocked!")
            text _(message):
                xalign 0.5
                text_align 0.5

            if show_achievements_count:
                $ num_achievements = len(persistent.achievements)
                text _("Number of Achievements Unlocked:") + " [num_achievements] / [total_num_achievements]":
                    xalign 0.5

            textbutton "{icon=icon-twitter} " + _("Tweet this"):
                xalign 0.5
                action OpenURL(tweet_content_url)

            if ok_text is None:
                $ ok_text = _("Gotta Unlock 'Em All!")
            textbutton ok_text:
                xalign 0.5
                action [
                Notify("This achievement is saved to the Bonus menu. Feel free to tweet about it later if you haven't!"),
                Return()
                ]