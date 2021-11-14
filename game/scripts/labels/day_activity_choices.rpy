label day_activity_choices:
    $ day_activity = None
    # this label should end up jumping to day_end

    # if the player has low_energy level, jump directly to one of the relaxing choices
    if player_stats.is_sanity_low():
        call day_activity_relax from _call_day_activity_relax
        call day_end
        return # return to script.rpy

    player "Okay, what shall we do for the day?"
    menu:
        # TODO: change this string to study more CS fundamentals
        # when the player has completed the curriculum
        "[day_acitivity_study]":
            # this choice helps grow coding knowledge
            python:
                day_activity = 'study'
                text = renpy.random.choice([
                    "Let's hit the books!",
                    "Let's head over to [developerquiz]!",
                    "Let's ramp up on my CS knowledge!"
                    ])
                renpy.say(player, text)

            if has_completed_curriculum: # can choose a topic to study
                menu study_session_choose_topic:
                    "Which topic to study for the coding interview?"

                    "General CS knowledge":
                        player "It's never a bad idea to go back to CS fundamentals!"
                        $ study_session_questions = general_questions

                    "JavaScript":
                        player "I feel like crunching some JavaScript questions today!"
                        $ study_session_questions = javascript_questions

                    "Web Development":
                        player "Let's buckle up and go with Web Dev!"
                        $ study_session_questions = web_questions

                    "Algorithms":
                        player "I wonder if I can develop a better algorithm to streamline my interview prep process?"
                        $ study_session_questions = algorithm_questions

                    "System Design":
                        player "Let's do some high-level system design!"
                        $ study_session_questions = system_questions

                    "Mix and match all topics":
                        player "How about mixing and matching all topics? That sounds more realistic in an interview setting."
                        $ study_session_questions = interview_questions

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
        if len(seen_hacker_space_events) == len(hacker_space_event_labels): # all seen, now pick random
            label = renpy.random.choice(hacker_space_event_labels)
        else: # just add the next one
            label = hacker_space_event_labels[len(seen_hacker_space_events)]
            seen_hacker_space_events.add(label)

        renpy.call(label)
    return

label day_activity_barista:
    scene bg cafe with slideright
    player "Alright, let's focus on my shift!"
    play sound 'audio/sfx/cafe_pour.wav'
    show coffee at truecenter
    pause 5
    hide coffee
    player "Here's your mocha latte. Enjoy your day!"
    # if all seen, skip
    if len(seen_barista_events) == len(barista_event_labels) or renpy.random.random() < 0.3:
        player "(It's pretty quiet in the cafe today. Guess I won't get to hear any tech gossips.)"
    else:
        # 70% trigger rate, pick random tech gossip
        python:
            label = renpy.random.choice(barista_event_labels)
            seen_barista_events.add(label)
            renpy.call(label)

    scene bg cafe dusk with fadehold
    play sound 'audio/sfx/cafe_pour.wav'
    show coffee at truecenter
    pause 5
    hide coffee

    player "My shift is almost over now."
    player "Serving coffee is no easy work, but somehow I feel refreshed from meeting and greeting people."
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
    $ day_activity = 'jobsearch'
    if has_won_hacker_space_trivia and not has_applied_to_cupcakecpu:
        player "Hey. I remember that the trivia guy at Hacker Space gave me a business card."
        show business_card at truecenter with zoomin
        player "Here's the business card. It's from CupcakeCPU."
        player "Let's apply to CupcakeCPU."
        hide business_card
        show screen job_posting_screen('CupcakeCPU', all_skill_names)
        $ has_applied_to_cupcakecpu = True
        # guaranteed interview
        $ interview_company_name = 'CupcakeCPU'

    else:
        # apply to some random company
        $ company_name = renpy.random.choice(all_company_names)
        show screen job_posting_screen(company_name, all_skill_names)
        if renpy.random.random() < 0.8: # 80% chance of interview
            $ interview_company_name = company_name

    player "They require so many different skills... but I think I'll be fine. I should at least try."
    play sound 'audio/sfx/todo_complete.wav'
    player "Application submitted. Let's hope for the best."

    if has_won_hacker_space_trivia:
        $ todo_list.complete_todo(todo_apply_cupcakecpu)
    hide screen job_posting_screen

    return

label day_activity_interview:
    $ day_activity = 'interview'
    player "Today is my big day! I have an interview with [interview_company_name]."    

    $ interview_room_bg = renpy.random.choice(interview_room_bgs)
    scene interview_room_bg with slideright
    player "Wow. Their office sure is fancy. I wish I can get my cubicle in a fancy office like this..."

    # TODO
    # $ interviewer_sprite = renpy.random.choice(seq=[])
    # show interviewer_sprite
    interviewer "Hello, is that [persistent.player_name]?"
    player "Yes. Good morning."

    interviewer "Alright, since we are here, let's get started with the interview."
    call interview_session from _call_interview_session

    interviewer "Thanks for taking your time. We will be in touch about next steps."
    player "(... Was that everything? Kudos to myself for surviving...)"
    $ player_stats.change_stats_random('Sanity', -20, -10)
    player "That was as intense as I expected. I hope I did well with all those preparations."
    player "I can't wait to go home and just relax now..."
    return