# https://www.renpy.org/doc/html/screen_special.html
# based on the confirm screen

screen confirm_and_share(message, ok_text):

    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xsize 800
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            text _(message):
                text_align 0.5
                xalign 0.5

            textbutton "{icon=logo-python}" action Return()

            hbox:
                spacing 100
                xalign .5
                textbutton ok_text action Return()