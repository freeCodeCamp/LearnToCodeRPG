label study_menu:
    menu:
        "Study CS fundamentals":
            player "Let's crunch some more code."
            call study_menu_choices from _call_study_menu_choices_1
            jump end_of_day_script
        "Take a walk":
            player "Let's head out to the park."
            call choice_walk from _call_choice_walk
            jump end_of_day_script
        "Work gig as a barista":
            player "I can do some shifts to cover my bills."
            call barista from _call_barista
            jump end_of_day_script
        "Hang out at Hacker Space":
            call hacker_space from _call_hacker_space
            jump end_of_day_script
        "Work on open-source projects":
            player "Annika mentioned that contributing to open-source project is a good way to learn."
            
            if player_stats.player_stats_map['CS Knowledge'] > 3: # can proceed
                player "Let's see, what are the newest Pull Requests?"
                call open_source from _call_open_source
                jump end_of_day_script
            else:
                player "Ehhh... I don't think my technical skills are solid enough for open-source projects yet. Maybe we can learn Git first?"
                call study_menu from _call_study_menu # re-enter choice screen

label open_source:
    scene bg laptop_screen
    player "Hmm... I don't know how to solve this but I can re-assign it to the original author."
    player "It's cool how people volunteer their time and energy to make software accessible."
    $ player_stats.change_stats('CS Knowledge', 1)
    return

label hacker_space:
    scene bg hacker_space
    player "Let's check out what cool projects people are working on."
    $ player_stats.change_stats('CS Knowledge', 1)
    return

label barista:
    scene bg cafe
    player "Here's your matcha latte. Enjoy your day!"
    player "Hmm... There are a group of kids in the back with their computers."
    kid "So I have this hackathon idea..."
    player "I don't mean to eavesdrop, but did they mention a hackathon?"
    player "Geez, kids these days are intense."
    player "But a hackathon? That sounds cool. I should give it a try when I know more about coding."
    return

label choice_walk:
    scene bg park
    player happy "It always soothe my nerves to take a walk in the park."
    player "I almost feel like it restores my sanity."
    $ player_stats.change_stats('Sanity', 10)
    return


label end_of_day_script:
    scene bg bedroom night with dissolve
    # TODO: rewrite logic
    $ player_stats.change_stats('Sanity', -10)
    player "Phew... That was a long day."

    # evaluate
    if player_stats.player_stats_map['CS Knowledge'] > 5 and player_stats.day_counter > 8:
        jump stage7_ryan
    else:
        jump day_activity_choices # a new day

    # evalute whether to proceed to the next stage
    call screen confirm_and_share(
        "{bt}{size=[gui.name_text_size]}Congratulations!{/size}{/bt}\n\nYou completed the coding curriculum in {b}[player_stats.day_counter]{/b} days.\nNow you are ready to rock the coding interview and realize your dream of becoming a software engineer.\n Feel free to share your progress with the world!",
        ok_text="Let's go!", ok_action=Jump('stage8')
        )