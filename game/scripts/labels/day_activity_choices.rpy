label day_activity_choices:
    $ day_activity = None
    $ has_triggered_ending_today = False
    # this label should end up jumping to day_end

    # if the player has low sanity, jump directly to one of the relaxing choices
    if player_stats.is_sanity_low():
        # TODO: notify
        $ renpy.notify('Your sanity is dropping dangerously low. Why not take some time to relax and recharge?')
        $ num_times_sanity_low += 1

        if has_met_layla and not has_triggered_ending_farmer and \
        num_times_sanity_low > 5 and renpy.random.random() < 0.05:
            call ending_farmer from _call_ending_farmer
        else:
            call day_activity_relax from _call_day_activity_relax

        call day_end from _call_day_end
        return # return to script.rpy

    player smile "What should we do for the day?"
    menu:
        # this string goes from 'study CS fundamentals' to 'study more CS fundamentals'
        # when the player has completed the curriculum
        "Study CS fundamentals":
            # this choice helps grow coding knowledge
            python:
                day_activity = 'study'
                text = renpy.random.choice([
                    "Let's hit the books!",
                    "Let's head over to [developerquiz]!",
                    "Let's ramp up my CS knowledge!"
                    ])
                renpy.say(player, text)

            call study_session_choose_topic from _call_study_session_choose_topic_1

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
                player @ laugh "I got all questions my right! Way to go!"
            elif num_correct == 3:
                player @ happy "But I got most questions right! At this rate I can make it!"
            elif num_correct == 2:
                player @ smile "I got half of the questions right. I need to put in more work."
            elif num_correct == 1:
                player pout "... I only got one question correct."
                player neutral "Well, it's better than nothing. I just have to try harder next time!"
            elif num_correct == 0:
                player pout "... I got all the questions wrong..."
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
            player "I'm feeling adventurous. Why not check out Hacker Space and meet some other people who are learning to code?"
            call day_activity_hacker_space from _call_day_activity_hacker_space
            call day_end from _call_day_end_3

        "Take a day off and relax":
            call day_activity_relax from _call_day_activity_relax_1
            call day_end from _call_day_end_4

    
    return

label study_session_choose_topic:
    menu:
        "Which topic to study?"

        "General CS concepts":
            player "It's never a bad idea to go back to CS (Computer Science) fundamentals!"
            $ study_session_questions = general_questions

        "HTML":
            player "HTML (HyperText Markup Language) is useful for web development. Let's go with that!"
            $ study_session_questions = html_questions

        "CSS":
            player "CSS (Cascading Style Sheets) is useful for web development. Let's go with that!"
            $ study_session_questions = css_questions

        "JavaScript":
            player "JavaScript is useful for web development and a lot of other things. Let's go with that!"
            $ study_session_questions = javascript_questions

        "Python":
            player "Python is useful for things like data science and machine learning. Let's go with that!"
            $ study_session_questions = python_questions

        "Linux":
            player "Linux is a family of open-source Unix-like operating systems. It has some cool commands that every cool developer should know. Let's go with that!"
            $ study_session_questions = linux_questions

        "Git":
            player "Git is a useful version control system. Let's go with that!"
            $ study_session_questions = git_questions

        "SQL":
            player "SQL (Structured Query Language) is useful for database operations. Let's go with that!"
            $ study_session_questions = sql_questions

        "IT":
            player "It's never a bad idea to go back to IT (Information Technology) fundamentals!"
            $ study_session_questions = it_questions

        # TODO: need to look up which category the question belongs to
        # "Mix and match all topics":
        #     player "How about mixing and matching all topics? That sounds more realistic in an interview setting."
        #     $ study_session_questions = interview_questions
    return
            
label day_activity_relax:
    # this choice boosts sanity
    player neutral "Hmmm... Actually, instead of doing something, I feel like I could use some rest today."
    # if player_stats.is_sanity_low():
    #     "(Whoa! {sc}Slow down, tiger.{/sc} We know you are excited about beefing up your {b}CS Knowledge{/b}, but it's important not to deplete your {b}Sanity{/b}. Why not take some time to recharge?)"
    # player pout "...But I have so much work to do..."
    show mint
    mint "Meow~"
    player smile "Oh Mint. Are you trying to tell me to take better care of myself?"
    player "Awww thanks Mint."
    hide mint
    player "Okay. Let's take a day off and chill. What should we do?"
    menu day_activity_relax_choices:
        "Take a walk in the park":
            $ day_activity = 'park'
            player "Let's head out to the park. Too bad I can't take Mint out on a walk. Annika does that with her puppy sometimes and they both love it."
            call day_activity_park from _call_day_activity_park
        "Play some video games":
            # NOTE
            if renpy.mobile:
                player "I'd love to play some games, but those are only available on my laptop."
                "(You won't able to access mini-games when you are playing the mobile or the web version. Please download the desktop version instead.)"
                player "Let's go take a walk in the park instead."
                call day_activity_park from _call_day_activity_park_1
            else:
                $ day_activity = 'videogame'
                player "Nothing beats some video games."
                call day_activity_video_game from _call_day_activity_video_game
        "Listen to music":
            $ day_activity = 'music'
            player "Let's listen to some music."
            call screen music_room_screen_in_script()
    $ player_stats.change_stats_random('Sanity', 5, 20)
    # all relaxing activities converge to the end of the day
    return

label day_activity_hacker_space:
    scene bg hacker_space with slideright
    play sound 'audio/sfx/office_ambient.wav'
    player "(As always, a lot of people are hanging out here.)"
    player "(I can go around and talk to people to learn about what cool things are happening.)"

    # hacker space trivia
    if not has_won_hacker_space_trivia:
        show man
        trivia_guy "Hey, you there! Would you be up for a round of tech trivia?"
        menu:        
            "Sure!":
                call hacker_space_tech_trivia from _call_hacker_space_tech_trivia
            "Sorry, not feeling like it.":
                player @ neutral "Sorry, but I'm not feeling like it."
                trivia_guy "No problem. Let me know anytime if you want a challenge."
                hide man
                player "(Let's just check out what's happening around here.)"
                call day_activity_hacker_space_random from _call_day_activity_hacker_space_random
    else:
        call day_activity_hacker_space_random from _call_day_activity_hacker_space_random_1

    scene bg hacker_space dusk with fadehold
    player @ surprised "Wow, it's already getting dark? Today's been quite an eventful day."
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
    player "Alright, let's serve some coffee to help get people started with their day!"
    play sound 'audio/sfx/cafe_pour.wav'
    show coffee at truecenter
    pause 5
    hide coffee
    player "Here's your mocha latte. Enjoy your day!"
    # if all seen, skip
    if len(seen_barista_events) == len(barista_event_labels) or renpy.random.random() < 0.3:
        player "(It's pretty quiet in the cafe today. Guess I won't get to hear any tech gossip.)"
    else:
        # 70% trigger rate, pick random tech gossip
        player @ surprised "(Pssst... Looks like there are people hanging out and having a fun conversation.)"
        python:
            available_labels = list(set(barista_event_labels) - seen_barista_events)
            label = renpy.random.choice(available_labels)
            seen_barista_events.add(label)
            renpy.call(label)

    scene bg cafe dusk with fadehold
    play sound 'audio/sfx/cafe_pour.wav'
    show coffee at truecenter
    pause 5
    hide coffee

    player @ relieved "My shift is almost over now."
    player "Serving coffee is no easy work, but somehow I feel refreshed from meeting and greeting people."
    $ player_stats.change_stats('Sanity', 5)

    if has_met_layla and not has_triggered_ending_barista and renpy.random.random() < 0.05:
        call ending_barista from _call_ending_barista
    return

label day_activity_park:
    scene bg park1 with slideright
    play sound 'audio/sfx/birds.wav'
    player happy "It always soothes my nerves to take a walk in the park."
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
    player laugh "I recently got this rhythm game everyone's been talking about."
    player smile "Let's pick a song from the playlist."
    
    # see rhythm_minigame.rpy    
    call rhythm_game_entry_label from _call_rhythm_game_entry_label

    player laugh "That was fun!"
    player smile "Video games are the best way to let off steam, aren't they?"
    player "Now I feel properly relaxed and refueled for a battle tomorrow!"
    return

label day_activity_job_search:
    $ day_activity = 'jobsearch'
    if has_won_hacker_space_trivia and not has_applied_to_cupcakecpu:
        player "Speaking of job postings, I remember that the trivia guy at Hacker Space gave me a business card."
        show business_card at truecenter with zoomin
        player "Here's the business card. It's from CupcakeCPU."
        player "Let's apply to CupcakeCPU."
        hide business_card
        call screen job_posting_screen('CupcakeCPU', all_skill_names)
        $ has_applied = _return
        if has_applied:
            $ has_applied_to_cupcakecpu = True
            # guaranteed interview
            $ company_name = 'CupcakeCPU'
            $ interview_company_name = company_name # a guaranteed interview

    else:
        # apply to some random company
        $ company_name = renpy.random.choice(all_company_names.keys())
        if renpy.random.random() < 0.02: # 2% chance of getting Easter Egg
            $ easter_egg_skill = renpy.random.choice(easter_egg_skills)
        else:
            $ easter_egg_skill = None
        call screen job_posting_screen(company_name, all_skill_names, easter_egg_skill=easter_egg_skill)
        $ has_applied = _return
        if has_applied:
            if renpy.random.random() < 0.8: # 80% chance of interview
                $ interview_company_name = company_name

    if has_applied:
        $ num_companies_applied += 1
        player @ smile "Application submitted. Let's hope for the best."
    else:
        player @ pout "I feel like I'm not ready for this job. They require so many skills that I don't yet have."

    if has_won_hacker_space_trivia:
        $ todo_list.complete_todo(todo_apply_cupcakecpu)

    return

label day_activity_interview:
    # this doesn't call `day_start` in advance
    # so we need to manually increment the calendar day here
    $ calendar.next()

    scene bg bedroom with fadehold
    $ day_activity = 'interview'

    show smartphone at truecenter
    play sound 'audio/sfx/alarm.wav'
    pause 3.0
    hide smartphone

    player smile "Today is my big day! I have an interview with {b}[interview_company_name]{/b}."    

    $ interview_room_bg = renpy.random.choice([
        'bg interview_room1',
        'bg interview_room2',
        'bg interview_room3'
        ])
    $ renpy.scene()
    $ renpy.show(interview_room_bg)
    with slideright
    # the above is equivalent to the below show statement
    # scene interview_room_bg with slideright
    player surprised "Wow. Their office sure is fancy. I hope I can get my cubicle in a fancy office like this..."

    $ interviewer_sprite = renpy.random.choice([
        'man',
        'woman',
        ]) + ' ' + renpy.random.choice(['', 'red', 'orange', 'blue', 'purple'])
    $ renpy.show(interviewer_sprite)
    interviewer "Hello, is that [persistent.player_name]?"
    player smile "Yes. Good morning."

    interviewer "Nice to meet you! We're glad that you applied to our job posting."
    interviewer "Alright, since we're all here, let's get started with the interview."
    player "Sounds good!"
    call interview_session from _call_interview_session

    interviewer "Thanks for taking your time. We will be in touch about next steps."
    $ renpy.hide(interviewer_sprite)

    player relieved "(... Was that everything? Kudos to me for surviving...)"
    $ player_stats.change_stats_random('Sanity', -20, -10)
    player "That was as intense as I expected. I hope I did well with all my preparations."
    player "I can't wait to go home and just relax now..."
    return
