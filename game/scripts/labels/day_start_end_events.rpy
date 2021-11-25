label day_start:
    hide screen player_stats_screen
    # this label should end up jumping to day_end, which then returns control to the main game
    $ calendar.next()

    scene bg bedroom with fadehold

    play sound 'audio/sfx/alarm.wav'
    pause 2.0
    play sound 'audio/sfx/birds.wav'
    pause 3.0

    # randomly choose a start-of-day label to call
    python:
        day_start_text = renpy.random.choice(seq=[
            'day_start_text1',
            'day_start_text2',
            'day_start_text3',
            ])
        renpy.call(day_start_text)
        
    return

# TODO: special text on days of interview
label day_start_text1:
    player "A new day!"
    show mint
    # mint "Meow meow~"
    player "Good morning, Mint."
    hide mint
    player "Hmmm, I don't feel like eating a big breakfast today. I guess a cookie will do."

    scene bg kitchen with blinds
    show cookie at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Yum yum."
    hide cookie

    scene bg bedroom with blinds
    player "Mom's homemade cookies never fail to kick-start my morning."
    return

label day_start_text2:
    mom "[persistent.player_name], breakfast's ready!"
    player "Okay, I'm up!"

    scene bg kitchen with blinds
    show toast at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Yum yum."
    hide toast
    player "I'm done. Gotta go and prepare for the day."
    player "Have a good day at work!"
    dad "You too, [persistent.player_name]!"
    mom "See you later, honey!"
    
    scene bg bedroom with blinds
    player "Alright, moving on from the most important meal of the day."
    return

label day_start_text3:
    show mint
    # mint "Meow!"
    player "Yawwwwwn..."
    player "(I feel like hitting snooze on my alarm...)"
    mint "Meow!"
    player "Ahhh... Mint, are you hungry? Okay I'm getting up and getting you breakfast."

    scene bg bedroom with fadehold
    show mint
    play sound 'audio/sfx/chew_food.wav'
    pause 4.0
    hide mint

    player "Haha Mint, thanks for waking me up."
    player "Now let's get on with the day."
    return

label day_end:
    hide screen player_stats_screen
    scene bg bedroom dusk with slideright
    player "Phew... That was a long day."

    # dinner
    mom "[persistent.player_name], dinner's ready!"
    player "Coming, mom!"

    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    $ show_random_dinner_image()

    mom "How was your day, honey?"
    player "Good, good."
    # TODO: different text according to the day activity
    if day_activity == 'study':
        player "I spent today studying and learned a lot!"
    elif day_activity == 'barista':
        player "I worked at the cafe today and heard some interesting conversations."
    elif day_activity == 'hackerspace':
        player "I went to Hacker Space today and saw some people working on cool projects."
    elif day_activity == 'park':
        player "I was at the park reading a nice book. It was really refreshing."
    elif day_activity == 'videogame':
        player "I played some cool video games today. Hopefully one day I'll able to code up a game myself."
    elif day_activity == 'jobsearch':
        player "I spent my day looking for job openings. I hope that my resume will catch the recruiter's eyes."
    elif day_activity == 'interview':
        player "I had an interview today. I wouldn't say it wasn't stressful, but I felt like I've given it my best shot."
    else:
        player "I just chilled for the day."
    dad "Sounds like you enjoyed your day."
    mom "Talk to us if you need anything."
    player "Thanks! You two are the best."

    scene bg bedroom night with blinds
    player happy "Delicious home-cooked dinner as always."

    player "Hmmm... Let's see. Do I have any cool tech terms I caught during my barista shift that I need to research about?"
    if not topics_to_ask:
        player "I don't have anything on my list."
    else: # if there are topics to ask about, call Annika or Marco
        player "I do have something to ask."
        # randomly decide between Annika and Marco
        if not has_met_marco:
            player "Shall I give Annika a call now?"
            menu:            
                "Call Annika now":
                    $ npc = annika
                    $ npc_sprite = 'annika'
            
                "Save the buzzword for later":
                    player "Hmm... Let's save up on those buzzwords and ask when I've gathered a few of them."
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
                    player "Hmm... Let's save up on those buzzwords and ask when I've gathered a few of them."

    player "Anyways, I feel like I've done a lot today. Let's call it a day and get some rest."
    player "Tomorrow will be another day. Right, Mint?"
    show mint
    mint "Meow!"
    player "Haha good night Mint."
    hide mint

    hide screen player_stats_screen
    scene black with fadehold

    return # should return control to script.rpy

label day_end_interview:
    hide screen player_stats_screen
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    $ show_random_dinner_image()

    mom "How was your day, honey? How did the interview go?"
    player "Well, I wouldn't say it wasn't stressful, but I felt like I've given it my best shot."
    player "I also feel like I need to work harder on interview prep."
    dad "That's the spirit."
    mom "We are proud of you, honey."
    dad "Let us know if you need anything."
    player "Thanks, I will. It's awesome to have you two behind my back!"
    dad "Any time, pumpkin."

    scene bg bedroom night with blinds
    player "Phew... What a day. I can't wait to go to catch some zzzz's already..."
    play sound 'audio/sfx/social_media_notification.wav'
    player "Oh. Here's a text from Annika."
    show annika
    player "It reads {i}'Hope your interview went well & take some well-deserved rest & let me know if there's anything you need help with! <3'{/i}"
    hide annika
    player "Awww that's so nice of Annika..."
    play sound 'audio/sfx/social_media_notification.wav'
    player "Hmm? Wow. A text from Marco as well?"
    show marco
    player "It reads {i}'Hey [persistent.player_name]! How did the interview go? Hopefully it wasn't too stressful for ya. Just keep in mind that we have all been there before. You can do it if you put in the work!{/i}"
    hide marco
    player "That's so considerate of Marco..."
    show mint
    mint "Meow meow~"
    player "Awww Mint, now you too?"
    hide mint
    player "I'm lucky to have mom, dad, Annika, Marco, and Mint supporting me."
    player "Yawwwwwn... Let's call this a day and wake up to a brand new tomorrow..."

    return