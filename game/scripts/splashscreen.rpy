image learn_to_code_splash = 'images/others/learn_to_code_rpg_logo.png'
image fcc_splash = 'images/others/fcc_logo.png'

label splashscreen:
    scene gray90 with Pause(1)
    play sound 'audio/sfx/title_drop_swoosh.wav'
    show learn_to_code_splash at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    scene gray90 with Pause(1)
    play sound 'audio/sfx/title_drop_swoosh.wav'
    show fcc_splash at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    # use a lighter background because the hyperlinks are dark blue
    scene gray10 with dissolve
    pause 1
    show text "{size=48}Accessibility Tips: Press the {b}v{/b} key to enable self-voicing.\nAdjust the volume of music and sound effects on the Settings screen.\nPress the {b}esc{/b} key to access the Game Menu at any time during the game.{/size}"
    with dissolve 
    pause 8

    # use a lighter background because the hyperlinks are dark blue
    scene gray10 with dissolve
    pause 1
    show text "{size=48}This game, {b}Learn to Code RPG{/b}, is currently in beta. If you notice any bugs or have suggestions about accessibility, the interface, the story, or anything at all, please be sure to {a=https://github.com/freeCodeCamp/LearnToCodeRPG}visit us on GitHub and bookmark the page.{/a}{/size}"
    with dissolve 
    pause 8

    # return control to the `start` label

    return