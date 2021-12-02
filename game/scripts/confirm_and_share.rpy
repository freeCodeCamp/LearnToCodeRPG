# https://www.renpy.org/doc/html/screen_special.html
# based on the confirm screen

screen confirm_and_share_screen(title, message, ok_text, tweet_content_url='https:///www.twitter.com'):

    # using `game menu root` will make this screen replace background image
    # modal True
    # window:
    #     style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xsize 1000
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            text _(title):
                text_align 0.5
                xalign 0.5
                size gui.name_text_size

            text _(message):
                text_align 0.5
                xalign 0.5

            hbox:
                spacing 100
                xalign .5
                textbutton "{icon=icon-twitter}" action OpenURL(tweet_content_url)

            hbox:
                spacing 100
                xalign .5
                textbutton ok_text action Return()