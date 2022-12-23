label day_start:
    $ calendar.next()

    scene black
    play sound 'audio/sfx/alarm.wav'
    pause 2.0
    scene bg bedroom with eyeopen
    play sound 'audio/sfx/birds.wav'
    pause 3.0

    if is_in_v2_arc1 and not 'v2_running_late' in seen_v2_arc1_events[HOME] and renpy.random.random() < 0.2:
        $ seen_v2_arc1_events[HOME].add('v2_running_late')
        call v2_running_late from _call_v2_running_late

    else:
        # randomly choose a start-of-day label to call
        python:
            day_start_text = renpy.random.choice(seq=[
                'day_start_text1',
                'day_start_text2',
                'day_start_text3',
                ])
            renpy.call(day_start_text)
        
    return

label day_start_text1:
    player happy "A new day!"
    show mint
    player "Good morning, Mint."
    hide mint
    player neutral "Hmmm, I don't feel like eating a big breakfast today. I guess a cookie will do."

    scene bg kitchen with blinds
    show cookie at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player laugh "Yum yum."
    hide cookie

    scene bg bedroom with blinds
    player "Mom's homemade cookies never fail to kick-start my morning."
    return

label day_start_text2:
    mom "[player_name], breakfast's ready!"
    player happy "Okay, I'm up!"

    scene bg kitchen with blinds
    show toast at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player laugh "Yum yum."
    hide toast
    player smile "I'm done. Gotta go and get ready for the day."
    player "Have a good day at work!"
    dad "You too, [player_name]!"
    mom "See you later, honey!"
    
    scene bg bedroom with blinds
    player "Alright, moving on from the most important meal of the day."
    return

label day_start_text3:
    show mint
    player relieved "Yawwwwwn..."
    player "(I feel like hitting snooze on my alarm...)"
    mint "Meow!"
    player surprised "Ahhh... Mint, are you hungry? Okay I'm getting up and getting you breakfast."

    scene bg bedroom with fadehold
    show mint
    play sound 'audio/sfx/chew_food.wav'
    pause 4.0
    hide mint

    player happy "Haha Mint, thanks for waking me up."
    player "Now let's get on with the day."
    return

label day_end:
    
    scene bg bedroom with blinds
    player relieved "Phew... That was a long day."

    if renpy.random.random() < 0.2:
        # dinner scene
        mom "[player_name], dinner's ready!"
        player happy "Coming, mom!"

        scene bg kitchen night with blinds
        play sound 'audio/sfx/dining_ambient.wav'
        $ show_random_dinner_image()

        mom "How was your day, honey?"
        player "Good, good."
        if day_activity == STUDY:
            player "I spent today studying and learned a lot!"
        elif day_activity == BARISTA:
            player "I worked at the cafe today and heard some interesting conversations."
        elif day_activity == HACKER_SPACE:
            player "I went to Hacker Space today and saw some people working on cool projects."
        elif day_activity == PARK:
            player "I was at the park reading a nice book. It was really refreshing."
        elif day_activity == VIDEO_GAME:
            player "I played some cool video games today. Hopefully one day I'll able to code up a game myself."
        elif day_activity == MUSIC:
            player "I was listening to some really good music today. Music always helps me relax."
        elif day_activity == JOB_SEARCH:
            player "I spent my day looking for job openings. I hope that my résumé will catch the recruiter's eye."
        elif day_activity == INTERVIEW:
            player "I had an interview today. I wouldn't say it wasn't stressful, but I felt like I gave it my best shot."
        else:
            player "I just chilled for the day."
        dad "Sounds like you enjoyed your day."
        mom "Talk to us if you need anything."
        player laugh "Thanks! You two are the best."

    if has_met_layla and not has_triggered_ending_today and \
    not has_triggered_ending_tutor and \
    renpy.random.random() < 0.05:
        call ending_tutor from _call_ending_tutor

    scene bg bedroom with blinds
    player happy "Delicious home-cooked dinner as always."

    if has_met_layla and not has_triggered_ending_today and \
    not has_triggered_ending_office and \
    has_completed_curriculum and renpy.random.random() < 0.05:
        call ending_office from _call_ending_office

    if has_triggered_ending_today:
        jump day_end_sleep

    if not topics_to_ask and not day_activity == BARISTA:
        jump day_end_sleep

    # either has something to ask or has worked as a barista that day
    player smile "Hmmm... Let's see. Do I have any cool tech terms I caught during my barista shifts that I need to research?"
    if not topics_to_ask:
        player "Looks like there's nothing on my list."
        # TODO: hint at how to get those tech terms
    else: # if there are topics to ask about, call Annika or Marco
        player "I do have something to ask."
        # randomly decide between Annika and Marco
        if not has_met_marco:
            player "Should I give Annika a call now?"
            menu:            
                "Call Annika now":
                    $ npc = annika
                    $ npc_sprite = 'annika'
                    call npc_conversation_start from _call_npc_conversation_start_2
            
                "Save the buzzword for later":
                    player "Hmm... Let's save up those buzzwords and ask when I've gathered a few more of them."
        else:
            player "Who should I talk to?"
            menu:
                "Who to ask about tech buzzwords?"
            
                "Annika":
                    player "Let's give Annika a call."
                    $ npc = annika
                    $ npc_sprite = 'annika'
                    call npc_conversation_start from _call_npc_conversation_start
            
                "Marco":
                    player "Let's chat with Marco."
                    $ npc = marco
                    $ npc_sprite = 'marco'
                    call npc_conversation_start from _call_npc_conversation_start_1

                "Save the buzzword for later":
                    player "Hmm... Let's save up those buzzwords and ask when I've gathered a few more of them."

label day_end_sleep:

    player "Anyways, I feel like I've done a lot today. Let's call it a day and get some rest."
    player "Tomorrow will be another day. Right, Mint?"
    show mint
    mint "Meow!"
    player "Haha good night Mint."
    hide mint

    scene black with eyeclose

    if has_met_layla and not has_triggered_ending_today and \
    not has_triggered_ending_cat and \
    renpy.random.random() < 0.05:
        call ending_cat from _call_ending_cat

    return # should return control to script.rpy

label day_end_interview:
    
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    $ show_random_dinner_image()

    mom "How was your day, honey? How did the interview go?"
    player smile "Well, I wouldn't say it wasn't stressful, but I felt like I gave it my best shot."
    player "I also feel like I need to work harder on interview prep."
    dad "That's the spirit."
    mom "We are proud of you, honey."
    dad "Let us know if you need anything."
    player happy "Thanks, I will. It's awesome to know that you two have my back!"
    dad "Any time, pumpkin."

    scene bg bedroom with blinds
    player relieved "Phew... What a day. I can't wait to go catch some zzzz's already..."
    play sound 'audio/sfx/social_media_notification.wav'
    show smartphone at truecenter
    player surprised "Oh. Here's a text from Annika."
    hide smartphone
    show annika
    player "It reads {i}'Hope your interview went well & take some well-deserved rest & let me know if there's anything you need help with! <3'{/i}"
    hide annika
    player smile "Awww that's so nice of Annika..."
    play sound 'audio/sfx/social_media_notification.wav'
    player surprised "Hmm? Wow. A text from Marco as well?"
    show marco
    player "It reads {i}'Hey [player_name]! How did the interview go? Hopefully it wasn't too stressful for ya. Just keep in mind that we have all been there before. You can do it if you put in the work!{/i}"
    hide marco
    player happy "That's so considerate of Marco..."
    show mint
    mint "Meow meow~"
    player laugh "Awww Mint, now you too?"
    hide mint
    player smile "I'm lucky to have mom, dad, Annika, Marco, and Mint supporting me."
    player relieved "Yawwwwwn... Let's call it a day and wake up to a brand new tomorrow..."

    scene black with eyeclose

    return
