label day_activity_choices:
    $ has_had_study_session_today = False
    # this label should end up jumping to day_end

    # hide unavailable choices
    $ config.menu_include_disabled = False

    menu:
        "Search for job openings" if has_completed_curriculum:
            player "Let's search for job openings."
            call day_activity_job_search

        "Study CS fundamentals":
            $ has_had_study_session_today = True
            # this choice helps grow coding knowledge
            # TODO: different text
            player "Let's hit the books."
            call study_session
            player "I feel like I just did a good amount of brain gymnastics..."

            $ player_stats.change_stats_random('Sanity', -20, -10)

            if num_correct == 4:
                player "But I got all questions right! Way to go!"
            elif num_correct == 3:
                player "But I got most questions right! At this rate I can make it!"
            elif num_correct == 2:
                player "I got half of the questions right. I need to put in more work."
            elif num_correct == 1:
                player confused "... {w}I only got one question correct."
                player neutral "Well, it's better than nothing. I just have to try harder next time!"
            elif num_correct == 0:
                player confused "... {w}I got all questions wrong..."
                player neutral "But it will get better with practice, won't it?"

            jump day_end
        
        "Work gig as a barista":
            # this choice unlocks interesting tech rumors and recovers a bit of sanity
            player "I can work some shifts to cover my bills. Plus, I get to interact with people and take my mind off cramming for a bit."
            call day_activity_barista
            jump day_end

        "Hang out at Hacker Space":
            # this choice progresses the Hacker Space side story
            player "The Hacker Space place that Annika mentioned sounds fun. Let's hit the road."
            call day_activity_hacker_space
            jump day_end

        "Work on open-source projects" if annika_open_source_visited:
            # this choice progresses the open-source side story and highlights the project on the player's resume
            if annika_open_source_first_visit:
                player "Annika mentioned that contributing to open-source project is a good way to learn."
                player "Plus it will beef up my resume and make me more visible to recruiters."
            
            if player_stats.player_stats_map['CS Knowledge'] > 3: # can proceed
                call day_activity_open_source
                jump day_end
            else:
                player "Ehhh... I don't think my technical skills are solid enough for open-source projects yet. Maybe we can learn some coding fundamentals first?"
                jump day_activity_choices # re-enter choice screen

        "Take a day off and relax":
            # this choice boosts sanity
            player confused "Hmmm... I feel like my energy level is quite low today."
            player "..."
            player "But I have so much work to do..."
            mint "Meow"
            player neutral "Oh Mint. Are you trying to tell me to take this slow?"
            mint "Meow"
            player "Awww thanks Mint."
            player "Okay. Let's take a day off and rejuvenate. Any idea for chill activities?"
            menu:
                "Take a walk in the park":
                    player "Let's head out to the park. Too bad I can't take Mint out on a walk like Annika does with her puppy."
                    call day_activity_park
                "Chill at home with Mint":
                    player "Hey Mint, come here. I will grab a nice book and we will just chill with some tea in the living room. Sounds good?"
                    mint "Meow"
                    call day_activity_read
                "Bake some treats":
                    player "Hmmm... how about baking something yummy?"
                    call day_activity_bake
                "Play some video games":
                    player "Nothing beats some indie games."
                    call day_activity_video_game
            $ player_stats.change_stats_random('Sanity', 5, 20)
            # all relaxing activities converges to the end of the day
            jump day_end

label day_activity_open_source:
    scene bg laptop_screen with dissolve
    player "Let's see, what are the newest Pull Requests?"
    player "Hmm... I don't know how to solve this but I can re-assign it to the original author."
    player "It's cool how people volunteer their time and energy to make software accessible."
    $ player_stats.change_stats_random('CS Knowledge', 2, 4)
    return

label day_activity_hacker_space:
    scene bg hacker_space with dissolve
    player "Let's check out what cool projects people are working on."
    $ player_stats.change_stats('CS Knowledge', 1)
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
    $ player_stats.change_stats('Sanity', 2)
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

label day_activity_job_search:
    $ company_name = renpy.random.choice(seq=all_company_names)

    show screen job_posting_screen(company_name, skills=all_skill_names)
    player "Oh, a job posted by {b}[company_name]{/b}"
    player "Should I apply to this job posting?"
    menu:
        "Apply":
            player "Let's apply and see what they say."

        "Don't apply":
            player "I don't think I qualify for this job yet..."

    hide screen job_posting_screen

label day_activity_interview:
    scene bg interview_room with dissolve
    player "Today is my big day! I have an interview."
    call interview_session
    # check results