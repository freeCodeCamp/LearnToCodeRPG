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

    $ accessibility_tips = _p("""
        Accessibility Tips: Press the {b}{u}v{/u}{/b} key to enable auto-voicing of the text.

        Adjust the volume of music and sound effects on the {icon=icon-settings} Settings screen.

        Press the {b}{u}Esc{/u}{/b} key to access the {icon=icon-grid}Game Menu at any time during the game.

        (Click anywhere to dismiss this message)
        """)
    # use a lighter background because the hyperlinks are dark blue
    scene main_menu with dissolve
    show white80 zorder 100 with dissolve
    pause 1
    show text "{size=48}[accessibility_tips]{/size}" zorder 101
    with dissolve
    pause
    hide text with dissolve

    $ beta_disclaimer = _p("""
        This game, {b}Learn to Code RPG{/b}, is currently in beta.

        If you notice any bugs or have suggestions about accessibility, the interface, the story, or anything at all, please report them on our {a=https://github.com/freeCodeCamp/LearnToCodeRPG}GitHub repo{/a}.

        If you are enjoying this game, please {icon=icon-award} rate and review us on {a=https://freecodecamp.itch.io/learn-to-code-rpg}itch.io{/a} and {icon=icon-star} star our {a=https://github.com/freeCodeCamp/LearnToCodeRPG}GitHub repo{/a}.

        (Click anywhere to dismiss this message)
        """)
    # use a lighter background because the hyperlinks are dark blue
    show text "{size=48}[beta_disclaimer]{/size}" zorder 101
    with dissolve 
    pause
    hide text with dissolve
    hide white80 with dissolve

    # return control to the `start` label

    return