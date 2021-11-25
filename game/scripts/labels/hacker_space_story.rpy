label hacker_space_tech_trivia:
    player "(Maybe I won't get a prize for doing this, but it sounds like fun!)"
    trivia_guy "Glad that you are interested!"
    trivia_guy "I have a prize for you if you get all questions correct."
    trivia_guy "Don't worry if you can't get all of them correct this time."
    trivia_guy "I ask the same eight questions to everyone here, until someone gets all correct."
    trivia_guy "Are you ready?"
    player "Yes, let's do this!"

    call trivia_session from _call_trivia_session # see quiz_session.rpy
    # results has been checked
    return

label hacker_space_tech_talk:
    player "Looks like there is someone giving a tech talk!"
    player "Sounds like something cool! Let's go listen."
    play sound 'audio/sfx/applause.wav'
    scene bg hacker_space with fadehold
    player "I could only understand some parts of it, but that was cool."
    player "Well, enough tech talk for the day."
    return

label hacker_space_project:
    player "Wow. Whiteboards and sticky notes everywhere..."
    player "Looks like people are hard at work on their projects."
    play sound 'audio/sfx/office_ambient.wav'
    player "Let's not disturb them and just watch from a distance."
    scene bg hacker_space with fadehold
    player "Their app idea is really cool even if it's still nothing but mocks."
    player "I guess that's a nice skill to have if I want to develop my project one day."
    player "Well, enough people-watching for the day."
    return

label hacker_space_open_source:
    player "Looks like there is someone talking about their open-source project."
    player "Let's listen to what they have to say."
    male "Contributing to open-source is a great way to practice your technical skills, and to beef up your resume."
    player "(Is that so? Then contributing to open-source sounds like a great side project for me.)"
    male "You might be wondering, where do we find open-source projects that could use a hand? Well, they are technically everywhere."
    male "Check out these websites as a starter!"
    scene bg hacker_space with fadehold
    player "Hmm... that was an informative talk. Let's maybe put some of that into action."
    return

label hacker_space_playtest:
    college_girl "Hey there!"
    player "Huh? Me?"
    college_girl "Yes. Do you have a moment?"
    college_girl "We are working on a game project for our college CS course, and we'd really appreciate it if you are willing to play-test it."
    college_girl "It's a simple pong game, in case you are wondering."
    menu:
        "Shall we play-test the pong game?"
    
        "Yes!":
            window hide  # Hide the window and  quick menu while in pong
            $ quick_menu = False
            # avoid rolling back and losing minigame state
            $ renpy.block_rollback()

            call screen pong

            # avoid rolling back and entering the chess game again
            $ renpy.block_rollback()
            # restore rollback from this point on
            $ renpy.checkpoint()
            $ quick_menu = True

            if _return == "computer":
                player "Wow. The computer was really good..."
                college_girl "Yay! I have a feeling that we are doing well on this project!"
            else:
                player "That's my victory!"
                college_girl "Wow. Congrats! That was a nice game."
            college_girl "Thanks for your time!"
            player "No problem. Happy to help!"

    
        "Sorry, but I'll pass.":
            player "Sorry, but I'm not super into arcade games. Best of luck on your project!"
            college_girl "No worries and thanks!"
    player "Let's check out that other group of people over there."
    return