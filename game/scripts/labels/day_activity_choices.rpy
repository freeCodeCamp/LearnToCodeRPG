label day_activity_choices:
    # this label should end up jumping to day_end

    # if the player has low_energy level, jump directly to one of the relaxing choices
    if player_stats.is_sanity_low():
        jump day_activity_relax

    player "Okay, what shall we do for the day?"
    menu:
        # if the player has searched for jobs on this day and saw nothing
        # they jump back here and this first option won't be available
        "Search for job openings" if has_completed_curriculum and not has_done_job_search_today:
            $ has_done_job_search_today = True
            player "Let's search for job openings."
            call day_activity_job_search from _call_day_activity_job_search_1
            jump day_end

        # TODO: change this string to study more CS fundamentals
        # when the player has completed the curriculum
        "Study CS fundamentals":
            # this choice helps grow coding knowledge
            python:
                text = renpy.random.choice([
                    "Let's hit the books!",
                    "Let's head over to [developerquiz]!",
                    "Let's ramp up on my CS knowledge!"
                    ])
                renpy.say('player', text)
            call study_session from _call_study_session_1

            python:
                text = renpy.random.choice([
                    "I feel like I just did a good amount of brain gymnastics...",
                    "That was a lot of new information to digest...",
                    "Phew... hopefully my brain will thank me for this workout later..."
                    ])
                renpy.say('player', text)

            $ player_stats.change_stats_random('Sanity', -20, -10)

            if num_correct == 4:
                player "But I got all questions right! Way to go!"
            elif num_correct == 3:
                player "But I got most questions right! At this rate I can make it!"
            elif num_correct == 2:
                player "I got half of the questions right. I need to put in more work."
            elif num_correct == 1:
                player pout "... I only got one question correct."
                player neutral "Well, it's better than nothing. I just have to try harder next time!"
            elif num_correct == 0:
                player pout "... I got all questions wrong..."
                player neutral "But it will get better with practice, won't it?"

            jump day_end
        
        "Work gig as a barista":
            # this choice unlocks interesting tech rumors and recovers a bit of sanity
            player "I can work some shifts to cover my bills. Plus, I get to interact with people and take my mind off cramming for a bit."
            call day_activity_barista from _call_day_activity_barista
            jump day_end

        "Hang out at Hacker Space" if has_visited_hacker_space_with_annika:
            # this choice progresses the Hacker Space side story
            player "I'm feeling adventurous. Why not check out Hacker Space for some adventures?"
            call day_activity_hacker_space from _call_day_activity_hacker_space
            jump day_end

        "Take a day off and relax":
            call day_activity_relax
            
label day_activity_relax:
    # this choice boosts sanity
    player pout "Hmmm... Actually, instead of doing something, I feel like I could use some rest today."
    "(Whoa! {sc}Slow down, tiger.{/sc} We know you are excited about beefing up your {b}CS Knowledge{/b}, but it's important not to deplete your {b}Sanity{/b}. Why not take some time to recharge?)"
    player "...But I have so much work to do..."
    show mint
    mint "Meow~"
    player neutral "Oh Mint. Are you trying to tell me to take better care of myself?"
    player "Awww thanks Mint."
    hide mint
    player "Okay. Let's take a day off and chill. What shall we do?"
    menu:
        "Take a walk in the park":
            player "Let's head out to the park. Too bad I can't take Mint out on a walk. Annika does that with her puppy sometimes and they both love it."
            call day_activity_park from _call_day_activity_park
        "Play some video games":
            player "Nothing beats some indie games."
            call day_activity_video_game from _call_day_activity_video_game
    $ player_stats.change_stats_random('Sanity', 5, 20)
    # all relaxing activities converges to the end of the day
    jump day_end

label day_activity_hacker_space:
    scene bg hacker_space with slideright
    play sound 'audio/sfx/office_ambient.wav'
    player "(As always, a lot of people are hanging out here.)"
    player "(I can go around and talk to people to learn about what cool things are happening.)"

    # hacker space trivia
    if not has_won_hacker_space_trivia:
        trivia_guy "Hey, you there! Would you be up to a round of tech trivia?"
        menu:        
            "Sure!":
                call hacker_space_tech_trivia
            "Sorry, not feeling like it.":
                player "Sorry, but I'm not feeling like it."
                trivia_guy "No problem. Let me know anytime if you are to a challenge."
                player "(Let's just check out what's happening around here.)"
                call day_activity_hacker_space_random
    else:
        call day_activity_hacker_space_random

    scene bg hacker_space dusk with fadehold
    player "Wow, it's already getting dark? Today's quite an eventful day."
    player "Let's head home now."

    return

label day_activity_hacker_space_random:
    scene bg hacker_space with blinds
    python:
        hacker_space_event = renpy.random.choice(seq=[
            'hacker_space_tech_talk',
            'hacker_space_project',
            'hacker_space_open_source',
            'hacker_space_playtest'
            ])
        renpy.call(hacker_space_event)
        player_stats.change_stats('Sanity', 5)
        player_stats.change_stats('Dev Trivia', 5)
    return

label day_activity_barista:
    scene bg cafe with dissolve
    # play sound ding-dong
    player "Here's your matcha latte. Enjoy your day!"
    player "Hmm... There are a group of kids in the back with their computers."
    kid "So I have this hackathon idea..."
    player "I don't mean to eavesdrop, but did they mention a hackathon?"
    player "Geez, kids these days are intense."
    player "But a hackathon? That sounds cool. I should give it a try when I know more about coding."

    player "Serving coffee is no easy work, but somehow I feel refreshed from meeting all these people."
    $ player_stats.change_stats('Sanity', 5)
    return

label day_activity_park:
    scene bg park
    player happy "It always soothe my nerves to take a walk in the park."
    player "I almost feel like it restores my sanity."
    return

label day_activity_bake:
    scene bg kitchen day
    player "I'm staying home and bake"
    return

label day_activity_read:
    scene bg living_room day
    player "I'm staying home and read"
    return

label day_activity_video_game:
    player "play some video game"
    return

label day_activity_job_search:
    # 0.5 chance there is no new job posting and the player goes back to other routines

    if renpy.random.random() > 0.7: # go back to routines
        player "I don't see any new job postings that I haven't applied to."
        player "Let's go do something else."
        jump day_activity_choices

    else: # proceed to application
        $ company_name = renpy.random.choice(seq=all_company_names)

        show screen job_posting_screen(company_name, all_skill_names)
        player "Oh, a job posted by {b}[company_name]{/b}."
        player "Should I apply to this job posting?"
        menu:
            "Apply":
                player "Let's apply and see what they say."
                # TODO: refactor
                if days_before_interview is not None: # already has an interview scheduled
                    pass
                else:
                    python:
                        # coin flip
                        if renpy.random.random() > 0.3:
                            days_before_interview = renpy.random.randint(2, 4)
                            interview_company_name = company_name
                            renpy.notify("This is a debug message, you have an interview with [interview_company_name] in [days_before_interview] days")

            "Don't apply":
                player "I don't think I qualify for this job yet... They will probably reject me any ways."

        hide screen job_posting_screen

    return

label day_activity_interview:
    player "Today is my big day! I have an interview with [interview_company_name]."    

    scene bg interview_room with dissolve
    player "Wow they have a fancy office. I do wish I can work here."

    interviewer "Hello, is that [persistent.player_name]?"
    player "Yes. Good morning."

    interviewer "Alright, since we are here, let's get started."
    call interview_session from _call_interview_session

    player "... {w}Was that everything? {w}Thank god..."
    $ player_stats.change_stats_random('Sanity', -20, -10)
    player "That was more intense than I thought. I hope I did well."
    player "I can't wait to go home and just cuddle with Mint now..."
    return