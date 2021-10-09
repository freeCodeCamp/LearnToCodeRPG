# https://www.renpy.org/doc/html/screen_special.html
# based on the confirm screen

screen confirm_and_share(title, message, ok_text, ok_action=Return()):

    modal True

    window:
        style "gm_root"

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
                textbutton "{icon=logo-facebook}" action OpenURL('https://www.facebook.com')
                textbutton "{icon=logo-instagram}" action OpenURL('https://www.instagram.com')
                textbutton "{icon=logo-twitter}" action OpenURL('https:///www.twitter.com')

            hbox:
                spacing 100
                xalign .5
                textbutton ok_text action ok_action