screen ctc(arg=None):

    zorder 100

    text "{icon=chevrons-down}" at ctc_animation:
        size 40
        xalign 0.96
        yalign 0.96
        color gui.accent_color

transform ctc_animation:
    parallel:
        alpha .2
        linear 1.0 alpha .9
        linear 1.0 alpha .2
        repeat
    parallel:
        linear 0.5 yoffset 0
        linear 0.5 yoffset 10
        linear 0.5 yoffset 0
        linear 0.5 yoffset -10
        repeat