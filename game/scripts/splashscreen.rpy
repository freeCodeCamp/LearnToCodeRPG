image splash = 'gui/fcc_primary_large.jpg'

label splashscreen:
    scene gray90 with Pause(1)
    show splash with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)
    # return control to the `start` label
    return