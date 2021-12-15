label splashscreen:
    scene gray90 with Pause(1)
    play sound 'audio/sfx/title_fire_swoosh.ogg'
    show learn_to_code_rpg_logo at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    scene gray90 with Pause(1)
    play sound 'audio/sfx/title_fire_swoosh.ogg'
    show fcc_logo at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    $ accessibility_tips = _p("""
        Accessibility Tips: To enable auto-voicing of the text, please first configure the speech synthesis settings (speaker gender, accent, etc.) on your computer according to {a=https://www.renpy.org/doc/html/self_voicing.html#speech-synthesis}these instructions{/a}.
        Back to the game, you may press the {b}{u}v{/u}{/b} key to switch on auto-voicing.

        Adjust the volume of music and sound effects on the {icon=icon-settings} Settings screen.

        Press the {b}{u}Esc{/u}{/b} key to access the {icon=icon-grid}Game Menu at any time during the game.
        """)
    # use a lighter background because the hyperlinks are dark blue
    scene main_menu overlay with dissolve
    pause 1
    show text "{size=48}[accessibility_tips]{/size}"
    with dissolve
    show screen ctc() # click to continue
    pause
    hide text with dissolve

    $ beta_disclaimer = _p("""
        This game, {b}Learn to Code RPG{/b}, is currently in beta.

        If you notice any bugs or have suggestions about accessibility, the interface, the story, or anything at all, please report them on our {a=https://github.com/freeCodeCamp/LearnToCodeRPG}GitHub repo{/a}.

        If you are enjoying this game, please {icon=icon-thumbs-up} rate and review us on {a=https://freecodecamp.itch.io/learn-to-code-rpg}itch.io{/a} and {icon=icon-star} star our {a=https://github.com/freeCodeCamp/LearnToCodeRPG}GitHub repo{/a}.
        """)
    # use a lighter background because the hyperlinks are dark blue
    show text "{size=48}[beta_disclaimer]{/size}"
    with dissolve 
    pause
    hide screen ctc
    hide text with dissolve

    # return control to the `start` label

    return