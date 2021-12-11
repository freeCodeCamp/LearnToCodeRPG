# https://www.renpy.org/doc/html/screen_special.html
# based on the confirm screen

screen confirm_and_share_screen(title, message="Now that's an Easter Egg uncovered!", ok_text='Call me the Egg Hunter!', tweet_content_url=tweet_default, show_easter_egg_count=True):

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

            label _(title) xalign 0.5

            text _(message):
                text_align 0.5 # align multiline
                xalign 0.5

            if show_easter_egg_count:
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