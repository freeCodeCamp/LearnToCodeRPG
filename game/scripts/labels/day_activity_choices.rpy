label day_activity_choices:
    $ day_activity = None
    # this label should end up jumping to day_end

    # if the player has low_energy level, jump directly to one of the relaxing choices
    if player_stats.is_sanity_low():
        call day_activity_relax from _call_day_activity_relax

    player "Okay, what shall we do for the day?"
    menu:
        # if the player has searched for jobs on this day and saw nothing
        # they jump back here and this first option won't be available
        "Search for job openings" if has_completed_curriculum and not has_done_job_search_today:
            $ has_done_job_search_today = True
            player "Let's search for job openings."
            call day_activity_job_search from _call_day_activity_job_search_1
            call day_end from _call_day_end

        # TODO: change this string to study more CS fundamentals
        # when the player has completed the curriculum
        "Study CS fundamentals":
            # this choice helps grow coding knowledge
            python:
                day_activity = 'study'
                text = renpy.random.choice([
                    "Let's hit the books!",
                    "Let's head over to [developerquiz]!",
                    "Let's ramp up on my CS knowledge!"
                    ])
                renpy.say(player, text)
            call study_session from _call_study_session_1

            python:
                text = renpy.random.choice([
                    "I feel like I just did a good amount of brain gymnastics...",
                    "That was a lot of new information to digest...",
                    "Phew... hopefully my brain will thank me for this workout later..."
                    ])
                renpy.say(player, text)

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

            call day_end from _call_day_end_1
        
        "Work gig as a barista":
            # this choice unlocks interesting tech rumors and recovers a bit of sanity
            $ day_activity = 'barista'
            player "I can work some shifts to cover my bills. Plus, I get to interact with people and take my mind off cramming for a bit."
            call day_activity_barista from _call_day_activity_barista
            call day_end from _call_day_end_2

        "Hang out at Hacker Space" if has_visited_hacker_space_with_annika:
            # this choice progresses the Hacker Space side story
            $ day_activity = 'hackerspace'
            player "I'm feeling adventurous. Why not check out Hacker Space for some adventures?"
            call day_activity_hacker_space from _call_day_activity_hacker_space
            call day_end from _call_day_end_3

        "Take a day off and relax":
            call day_activity_relax from _call_day_activity_relax_1
            call day_end from _call_day_end_4
    return
            
label day_activity_relax:
    # this choice boosts sanity
    player "Hmmm... Actually, instead of doing something, I feel like I could use some rest today."
    if player_stats.is_sanity_low():
        "(Whoa! {sc}Slow down, tiger.{/sc} We know you are excited about beefing up your {b}CS Knowledge{/b}, but it's important not to deplete your {b}Sanity{/b}. Why not take some time to recharge?)"
    player pout "...But I have so much work to do..."
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
            player "Nothing beats some video games."
            call day_activity_video_game from _call_day_activity_video_game
    $ player_stats.change_stats_random('Sanity', 5, 20)
    # all relaxing activities converges to the end of the day
    return

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
                call hacker_space_tech_trivia from _call_hacker_space_tech_trivia
            "Sorry, not feeling like it.":
                player "Sorry, but I'm not feeling like it."
                trivia_guy "No problem. Let me know anytime if you are to a challenge."
                player "(Let's just check out what's happening around here.)"
                call day_activity_hacker_space_random from _call_day_activity_hacker_space_random
    else:
        call day_activity_hacker_space_random from _call_day_activity_hacker_space_random_1

    scene bg hacker_space dusk with fadehold
    player "Wow, it's already getting dark? Today's quite an eventful day."
    player "Somehow I feel quite relaxed in this coder-centric atmosphere."
    # bump sanity for a little bit
    $ player_stats.change_stats('Sanity', 5)
    player "Let's head home now."
    return

label day_activity_hacker_space_random:
    scene bg hacker_space with blinds
    python:
        if len(seen_hacker_space_events) == 4: # all seen, now pick random
            hacker_space_event = renpy.random.choice(seq=hacker_space_events)
        else: # just add the next one
            hacker_space_event = hacker_space_event_labels[len(seen_hacker_space_events)]
            seen_hacker_space_events.add(hacker_space_event)

        renpy.call(hacker_space_event)
    return

label day_activity_barista:
    scene bg cafe with slideright
    # TODO: play sound ding-dong

    # TODO: refactor
    python:
        if len(seen_hacker_space_events) == 4: # all seen, now pick random
            hacker_space_event = renpy.random.choice(seq=hacker_space_events)
        else: # just add the next one
            hacker_space_event = hacker_space_event_labels[len(seen_hacker_space_events)]
            seen_hacker_space_events.add(hacker_space_event)


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
    $ day_activity = 'park'
    scene bg park1 with slideright
    play sound 'audio/sfx/birds.wav'
    player happy "It always soothe my nerves to take a walk in the park."
    scene bg park2 with fadehold
    pause 2.0
    scene bg park3 with fadehold
    pause 2.0
    scene bg park4 with fadehold
    pause 2.0
    play sound 'audio/sfx/birds.wav'
    scene bg park1 dusk with fadehold
    pause 2.0
    player "Time really flies when I'm relaxing in nature... Let's head home now."
    return

label day_activity_video_game:
    $ day_activity = 'videogame'
    player "I recently got this rhythm game everyone's talking about. Let's pick a song from the playlist."
    $ choice = renpy.display_menu(list(rhythm_game_beatmaps.items()))
    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()

    # unpack the file paths associated with the chosen song
    $ audio_path, beatmap_path = choice
    call screen rhythm_game(audio_path, beatmap_path)

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return
    player "I hit [num_hits] notes out of [num_notes]. That wasn't bad!"
    player "Video games are the best way to let off steam, aren't they?"
    player "Now I feel properly relaxed and fueled for a battle tomorrow!"
    return

label day_activity_job_search:
    # 0.5 chance there is no new job posting and the player goes back to other routines
    if renpy.random.random() > 0.5: # go back to routines
        player "I don't see any new job postings that I haven't applied to."
        player "Let's go do something else."
        jump day_activity_choices

    else: # proceed to application
        $ day_activity = 'jobsearch'
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
    $ day_activity = 'interview'
    player "Today is my big day! I have an interview with [interview_company_name]."    

    scene bg interview_room with slideright
    player "Wow. Their office sure is fancy. I wish I can get my cubicle in a fancy office like this..."

    interviewer "Hello, is that [persistent.player_name]?"
    player "Yes. Good morning."

    interviewer "Alright, since we are here, let's get started."
    call interview_session from _call_interview_session

    player "... {w}Was that everything? {w}Thank god..."
    $ player_stats.change_stats_random('Sanity', -20, -10)
    player "That was more intense than I thought. I hope I did well."
    player "I can't wait to go home and just cuddle with Mint now..."
    return