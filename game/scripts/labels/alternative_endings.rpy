label ending_barista:
    # this has a certain probability of being triggered when the player works as a barista
    $ has_triggered_ending_barista = True
    $ has_triggered_ending_today = True

    scene bg cafe with dissolve
    show man orange
    cafe_manager "Hey [player_name]. Can I have a word with you?"
    player surprised "!"
    player worry "(Did I do anything wrong? Served the wrong order and got some customer complaints maybe?)"
    player "(Am I gonna get fired? Why am I unable to hold even a simple barista gig?)"
    with hpunch
    player surprised "!"
    player "(The cafe manager has a big smile on his face.)"
    player relieved "(Calm down... Nothing bad is going to happen.)"
    player smile "Sure. Anything I can help with?"
    cafe_manager "What would you say to a promotion?"
    player surprised "A promotion?"
    cafe_manager "Yes. You've been working hard and performing really well."
    cafe_manager "Our customers love you and we would love to have a full-time barista like you."
    cafe_manager "Your new hourly rate will be twice what you have now. What do you say?"
    player neutral "(That sure sounds like good stuff, but working full-time would also mean that I'll have less time to study coding.)"
    player "(If my job gets too busy, I might need to give up on learning to code all together.)"
    player "(I feel like this is a really important decision for me to make. I need to think this through.)"

    call save_reminder from _call_save_reminder_15

    menu:
        player "(Should I take them up on the full-time barista offer?)"

        "Why not? I need cash and learning to code can wait.":
            pass

        "Nope. I really need to carve out more time to study and become a developer.":
            player "Thanks, but my plate's a bit too full at the moment for a full-time role."
            cafe_manager "No problem. We are happy enough to have you help out part-time."
            cafe_manager "Best of luck with whatever it is that you are doing. You'll do great."
            hide man
            return # return control to the script that called this label

    player happy "I'd love to work full-time here."
    cafe_manager "Great! I was hoping that this would be an offer that you can't turn down."
    cafe_manager "Okay, starting tomorrow, I'm hoping to see you here from nine to five."
    player "Sure thing! Being punctual was one of my biggest strengths during college."
    cafe_manager "That's great news to our customers. Keep up the great work."
    hide man
    player smile "Okay, I guess I have a full-time job now."
    player "Once I have enough cash, I can always quit and learn to code full-time, right?"

    $ calendar_enabled = False
    $ player_base = 'player_apron' # no need to reset this b/c we are using default

    call screen text_over_black_bg_screen("A year later...")
    scene bg cafe with fade
    player neutral "So I've been working full-time as a barista for a whole year now."
    player "The work keeps me quite busy every day, and I don't have much time left by the end of the day to learn to code."
    player smile "But coming in every day, greeting people on their way to work, seeing them leave the cafe with a smile on their face - those are really precious moments."
    player "Plus I still get to hear about cool things happening in tech every now and then."
    show woman purple
    female "Hey [player_name]. How was your day?"
    player surprised "(My customers even know me by name now...)"
    player smile "My day's been great! What about yours?"
    female "Good. I just heard about this new app that's trending in the developer community..."

    scene bg cafe dusk with fade
    player happy "(Well, I'm happy with where I am now, I think.)"

    call screen text_over_black_bg_screen("Two years later...")
    scene bg cafe with fade
    player neutral "Same old day. I've been working full-time here at this cafe for two years now."
    player smile "Well, there is one thing that's different: I got promoted to the cafe manager."
    player "Turns out that the cafe is doing so well that it needs to open up new chain stores, so the old cafe manager who offered me this full-time barista position switched stores."
    player "Now that I'm managing this cafe, I have even more responsibilities."
    player worry "I feel like I won't be getting back to learning to code any time soon."
    player neutral "But that in itself isn't a bad thing...{p=1.0}{nw}"
    show girl blue with moveinleft
    player happy "Hello! What can I get for you?"
    player "..."
    player "(It looks like she is talking on the phone.)"
    girl "I'm at the cafe now."
    girl "What? You won't be here for an hour because you're stuck in traffic?"
    girl "But we need to figure out this bug as soon as possible so we can unblock the team who depends on our API!"
    girl "Grrrrgggghhhhh..."
    player surprised "(It looks like they are stuck on some coding project.)"
    player "(Maybe I can help?)"
    player happy "Hey, excuse me. I'm [player_name]. I work at this cafe."
    player "Sorry that I overheard your conversation, but if it's something related to coding, maybe I can help."
    player "I might not look like much but I used to be an aspiring developer!"
    player pout "(Well, not anymore...)"
    girl "Wow that'd be awesome! Thanks!"
    player laugh "Alright, here goes. Let's take a look..."

    play sound 'audio/sfx/alternative_ending.wav'
    call screen text_over_black_bg_screen("{i}Ending: [ending_barista]{/i}")

    scene bg cafe
    $ add_achievement(
        achievement_name=ending_barista,
        message=alternative_endind_message
        )

    jump second_chance
    scene bg cafe with dissolve

    return # return control to the label it jumped from

label ending_cat:
    # this has a certain probability of being triggered during the night
    $ has_triggered_ending_cat = True
    $ has_triggered_ending_today = True

    scene black
    scene bg bedroom with eyeopen
    play sound 'audio/sfx/keyboard_typing.wav'
    player relieved "Yawwwn...."
    player worry "I heard some strange noises coming from under my bed. Maybe Mint is hungry and woke up?"
    player surprised "Mint? Is that you?"
    player neutral "..."
    player worry "Mint didn't show up. Should I check what's happening?"
    menu:
        player "Should I check what's happening?"

        "Check under the bed.":
            pass # continue with the plot

        "Just go back to sleep.":
            player "Nah. Mint's a good cat and won't do any damage."
            player relieved "I could use more sleep so that I'll wake up energized for a new day."
            return # return control to the script that called this label

    # if player decides to check
    play sound 'audio/sfx/keyboard_typing.wav' volume 1.2
    scene bg laptop_screen night with dissolve    
    show mint_with_pixel_sunglasses with moveinbottom
    player surprised "Mint? What are you doing under my bed with my laptop?"
    with hpunch
    player "And what's with those sunglasses?"
    with vpunch
    player neutral "(Okay. Calm down. Deep breath. Let's find out what Mint is doing)"
    player "(Mint looks absorbed while ardently typing on my laptop.)"
    player "(It looks like Mint has a text editor open. For what? Writing code?)"
    player surprised "(Hang on. Mint is pulling up a terminal now. Maybe the code is done and ready to deploy?)"
    player pout "(Geez... I don't even know if I'm more curious about what Mint has coded up or how a cat is able to do any of these things in the first place.)"
    player surprised "(Oh! The website is coming up live!)"
    player "(Wait. I think I know this interface...)"
    player "(Isn't that just [developerquiz]?!)"
    player "(Wait wait wait. So Mint was the one who coded up [developerquiz], the go-to website for aspiring developers?)"
    player pout "(My logic is failing me at this point...)"
    player relieved "(Maybe this is all a dream?)"
    menu:
        player "Maybe this is all a dream?"

        "I must be dreaming. Let's go back to sleep.":
            player worry "I must be so exhausted and anxious about the coding stuff that I'm hallucinating about Mint writing code."
            player relieved "Let's go get more sleep before my {b}Energy{/b} hits the floor."
            hide mint_with_pixel_sunglasses
            return # return control to the script that called this label

        "This can't be a dream. I need to figure out what's going on.":
            pass

    player neutral "Nope. This can't be a dream. I need to figure out what's going on."
    player "What I've gathered from what I've seen is that Mint is a coding whiz..."
    player laugh "And isn't that awesome? I mean, I have a {bt}cat who codes{/bt}!"
    player smile "Hey Mint! Can I have a moment?"
    player neutral "..."
    player "(Mint is still staring determinedly at the laptop and not responding to me.)"
    player smile "Oh, well, I guess this could be Mint's way of telling me to keep this secret?"
    player "(I better choose my action carefully so as not to upset Mint.)"

    call save_reminder from _call_save_reminder_16

    menu:
        player "Shall I keep this as a secret just between Mint and me?"
    
        "Let's keep this a secret and say goodnight to Mint.":
            player "Alright Mint. You are awesome. Keep doing what you're doing."
            player "One day I'll catch up to you."
            player laugh "Good night!"
            hide mint_with_pixel_sunglasses
            return
    
        "But it's such a loss for the world if people don't know about Mint!":
            pass

    player happy "(It's a waste if Mint's talent goes unnoticed. Together we can make history!)"
    player "Hey Mint! Mind if I join you and learn to code from you?"

    $ player_glasses = 'player_pixelsunglasses'

    player "Here, here. I even got matching sunglasses."
    player laugh "How do these look on me?"
    mint "Meow! (Looks great!)"
    player "You like them? Thanks Mint!"
    mint "Meow! (Now let's get to work!)"
    player "And you're telling me to get to work now? Okay, I'll give it my best shot!"
    $ calendar_enabled = False

    call screen text_over_black_bg_screen("A month later...")
    scene bg hall with fade
    host "And now let's give a round of applause to our hackathon winner team: {b}Cat Who Codes{/b}!"
    play sound 'audio/sfx/applause.ogg'
    show mint_with_pixel_sunglasses
    player laugh "Wow... We managed to win first place all thanks to Mint. This is awesome!"
    host "We hope to see you at our next hackathon as well!"

    call screen text_over_black_bg_screen("A year later...")
    scene bg hall_audience with fade
    play sound 'audio/sfx/applause.ogg'
    show woman orange
    journalist "Did you see that person and the cat there? They are the famous {b}Cat Who Codes{/b}."
    show girl flipped red at left with moveinleft
    college_girl "So that's the team that's been bagging all the trophies at hackathons, large and small?"
    show boy red at right with moveinright
    boy "That's impressive!"
    journalist "Rumor even has it that the cat is a coding whiz."
    college_girl "Now that's cryptic..."

    hide woman
    hide girl
    hide boy
    show mint_with_pixel_sunglasses with moveinbottom
    mint "Meow! (Keep that a secret, will ya?)"
    window hide
    hide mint_with_pixel_sunglasses
    with pixellate

    play sound 'audio/sfx/alternative_ending.wav'
    call screen text_over_black_bg_screen("{i}Ending: [ending_cat]{/i}")

    $ add_achievement(
        achievement_name=ending_cat,
        message=alternative_endind_message
        )
    jump second_chance
    scene bg bedroom with dissolve
    
    return

label ending_tutor:
    # this has a certain prob of being triggered during dinner
    $ has_triggered_ending_tutor = True
    $ has_triggered_ending_today = True

    scene bg kitchen night with dissolve
    mom "I just remembered something to tell you, [player_name]."
    mom "Would you be interested in helping kids learn to code?"
    mom "A high school affiliated with the one where I'm teaching is looking to expand their CS curriculum."
    mom "They are looking for a tutor. It's a temporary position for now, but may eventually turn into a full-time teaching contract."
    player surprised "That sounds cool..."
    mom "I know you are busy teaching yourself to code and this may take time away from your studies."
    mom "The decision is all up to you. No pressure."
    player smile "(Mom's as considerate and resourceful as always.)"

    menu:
        player "(Should I take up the CS tutor gig?)"
    
        "Why not? Teaching is the best way to learn!":    
            pass
    
        "Nah. I'm too busy teaching myself already.":
            player neutral "Thanks mom. I feel like I'm too busy with my own studying already, so I'll pass."
            mom "No worries, hon. Let me know if you need anything."
            return

    player happy "Thanks mom. That sounds fun! I'd love to give it a try."
    mom "Okay, how about you come with me tomorrow to the school?"
    player "Will do!"

    $ calendar.next()
    scene bg classroom with fade
    show boy purple with moveinleft
    boy "Everyone shush and get back to their seats!"
    boy "I heard that we are going to get a new tutor to teach us coding."
    hide boy with moveoutright
    player happy "Hi everyone. I'm [player_name]. I'm your CS tutor for the day."
    player smile "Let's jump right in! Who can tell me what a computer program is?"
    girl "I know! Like an app on your phone!"
    boy "And video games as well!"
    girl "Eh. The video game talk again. Can you talk for one second about something else?"
    player surprised "(Wow. The kids sure are energetic. And smart, too!)"
    player "Alright, those are all great answers. Now let me give you this definition of a computer program..."

    scene bg classroom dusk with fadehold
    boy "Thank you so much for today! That was fun!"
    girl "We learned a lot! Hope to see you again!"

    scene bg kitchen dusk with fadehold
    mom "How did you like teaching, [player_name]?"
    mom "I heard that the kids loved you and the school would like you to come every day if that works for your schedule."
    player neutral "(That was fun, but it was a lot of work as well.)"
    player "(But if I need to come in every day, I won't have time to learn to code and become a developer myself.)"
    player "(That said, am I that hellbent on becoming a developer? Wouldn't it be fun to pass along my coding knowledge?)"
    player "(Should I stick to learning to code, or should I continue to teach coding?)"
    player "(I feel like this is a really important decision for me to make. I need to think this through.)"

    call save_reminder from _call_save_reminder_17

    menu:
        player "(Should I stick to learning to code, or continue to teach coding?)"
    
        "Let's stick to learning to code and become a developer.":
            player "(Right. I shouldn't forget about my initial goal.)"
            player "(If I want to become a proficient developer, I need to put in the hard work.)"
            mom "Hon, you've been quiet. You don't have to rush to decide, you know."
            player smile "Thanks mom. I'm good. I've already made up my mind."
            player "I'll stick to my original plan, learn to code, and get an awesome developer job."
            mom "I'm happy for you either way, hon. Now get some rest tonight."
            return

        "Let's teach coding and pass along the torch.":
            pass

    $ calendar_enabled = False
    call screen text_over_black_bg_screen("A month later...")
    scene bg classroom with fade
    player happy "So this is how a for loop works. Are we all clear on the definition?"
    boy "This for loop thing is amazing! {b}For{/b} each enemy in the game, I'm gonna beat 'em up!"
    girl "... {b}For{/b} each time you mention video games, I'm gonna tell you to cut it out."
    player laugh "Let's {b}break{/b} out of the for loop and move on, shall we?"

    call screen text_over_black_bg_screen("A year later...")
    scene bg classroom with fade
    # actually meets Layla who volunteers here
    player smile "I heard that we're having a special guest today."
    player "She is a developer who loves teaching and volunteering."
    player "She's going to talk to the class about what it's like to work in software engineering."
    player "(Oh, here she comes!)"
    show layla
    player surprised "(Wait. She looks familiar.)"
    player "(...Oh! Was that her at Hacker Space mentoring the kids?)"
    player "(If I remember correctly...)"

    scene bg hacker_space with fadehold
    show layla
    layla @ laugh "So how's everyone's project going? We mentors are here to answer any questions you have!"

    scene bg classroom with fade
    show layla
    player "(That was definitely her at Hacker Space!)"
    layla "Hey there! I'm Layla."
    player smile "Hi Layla. Nice to meet you! I'm [player_name]. I've been teaching here for a year."
    layla "That's awesome! Teaching is my favorite thing to do, actually."
    layla "Alright, enough small talk. Is it about time that we address the class?"
    player happy "Yeah sure!"
    player laugh "Hey class, today we have Layla, a full-time developer, here to talk to you about what it's like to work in tech."
    layla @ laugh "Thanks for the intro, [player_name]. I'm Layla."
    layla "Before I start with my story. Let me just tell you this."
    layla "I once had to make a very difficult choice between working in software or teaching coding at a school."
    player pout "(That sounds familiar. I've been there before, too.)"
    layla "I chose the former and here I am."
    layla @ laugh "Well, sometimes I do wonder what could've happened if I had chosen differently."
    player relieved "(Layla looks content with where she is now. Hmmm... but I do wonder, what could've happened if I'd chosen differently?)"

    play sound 'audio/sfx/alternative_ending.wav'
    call screen text_over_black_bg_screen("{i}Ending: [ending_tutor]{/i}")

    scene bg classroom
    $ add_achievement(
        achievement_name=ending_tutor,
        message=alternative_endind_message
        )
    jump second_chance
    scene bg kitchen night with dissolve
    
    return

label ending_office:
    # this has a certain prob of being tiggered during the evening once the player starts doing coding interviews
    $ has_triggered_ending_office = True
    $ has_triggered_ending_today = True

    scene bg bedroom with dissolve
    play sound 'audio/sfx/social_media_notification.wav'
    show smartphone at truecenter
    player surprised "Hmm... A notification from my phone?"
    player neutral "It reads 'We are hiring!' Maybe it's from some old office job I applied to when I was finishing up college."
    player "Should I read the email?"
    menu:
        player "Should I read the email about an office job application?"
    
        "Won't hurt if I read it.":
            pass
    
        "No. Office jobs are a bore.":
            player "No thanks. There is absolutely no way I'll work a boring office job for the rest of my life."
            player "Message deleted. Now I'm gonna get back to my day."
            hide smartphone
            return

    hide smartphone

    player "Won't hurt if I read the email."
    player "Hmm... They said they looked at my application and thought I'm a good fit. Well, it's easy office work, so anyone is a good fit."
    player "The most technically complicated thing I would need to deal with is probably a spreadsheet."
    player "But the pay is decent enough..."
    player "Maybe I can work for a few months and see how it goes?"
    player "(I feel like this is a really important decision for me to make. I need to think this through.)"

    call save_reminder from _call_save_reminder_18

    menu:
        "Should I accept the office job?"
    
        "It pays okay so why not?":
            pass
    
        "Nah. I want to become a developer, not an office worker.":
            player "Right. I shouldn't forget about my initial goal."
            player "If I want to become a proficient developer, I need to put in the hard work."
            player "Message deleted. Now I'm gonna get back to my day."
            return

    $ calendar_enabled = False
    call screen text_over_black_bg_screen("A week later...")
    scene bg cubicle with fade
    player neutral "(Okay. Here I am. At my new office job.)"
    office_worker "Hey you there. Come with me to fix the fax machine now."
    player surprised "Uhhh okay!"
    player worry "(This is as boring as I thought it'd be.)"
    player "(But I guess beggars can't be choosers...)"

    call screen text_over_black_bg_screen("A year later...")
    scene bg cubicle with fade
    player neutral "(It's been a year, and here I am, still at my office job.)"
    player "(The work is boring and mentally draining, so I come home everyday too exhausted to do anything else.)"
    player @ pout "(Geez, I haven't even had the energy to play video games in a long time, let alone learn to code in my spare time.)"
    office_worker "Hey you. Stop daydreaming. The boss wants this presentation slide deck done today."
    player "Oh, sorry, I'll get it done as soon as possible."

    call screen text_over_black_bg_screen("Two years later...")
    scene bg cubicle with fade
    player neutral "(It's been what, two years already?)"
    player "(Here I am. Still working this office job.)"
    player "(At this point, it's not like I have an opinion anymore about staying here or quitting.)"
    player pout "(I mean, making spreadsheets and slides is the only skill I have.)"
    player worry "(Ugh. And making coffee as well.)"
    player relieved "(Guess this is it? Unless...)"

    play sound 'audio/sfx/alternative_ending.wav'
    call screen text_over_black_bg_screen("{i}Ending: [ending_office]{/i}")

    scene bg cubicle
    $ add_achievement(
        achievement_name=ending_office,
        message=alternative_endind_message
        )
    jump second_chance
    scene bg bedroom with dissolve
    
    return

label ending_farmer:
    # this is triggered if energy is too low
    $ has_triggered_ending_farmer = True
    $ has_triggered_ending_today = True

    scene bg bedroom with dissolve
    player relieved "I'm so so so tired..."
    player pout "I need a break. A long one."
    player "Just last night, I read about the guy who quit software engineering because he was burnt out."
    player "He went on to become a farmer. Told the journalist a year later that he had no intention of returning to tech."
    player neutral "Maybe farming is my calling too?"
    player "But there is probably no going back to where I am if I take up farming. I better think this though..."

    call save_reminder from _call_save_reminder_19

    menu:
        player "Should I really give up on learning to code already and embrace mother nature?"
    
        "Sounds like a plan!":
            pass
    
        "Just kidding!":
            player relieved "Ughhhh... I'm kidding, I hope."
            show mint
            mint "Meow!"
            player smile "Oh Mint. Are you trying to tell me to not to give up?"
            player "Awww thanks Mint. I won't give up if you don't give up on me."
            hide mint
            player neutral "Alright, that was a nice joke, but an impractical one."
            player "Let's just go take a walk in the park to celebrate mother nature."
            call day_activity_park from _call_day_activity_park_2
            $ player_stats.change_stats_random(ENERGY, 5, 20)
            return

    $ calendar_enabled = False
    $ player_base = 'player_overall'
    $ player_glasses = None

    scene bg farm with fade
    player happy "Wow! This farm is huge! Bigger than what I've seen in the movies!"
    player "Guess this is where I'll be calling home now."
    player pout "Too bad Mint couldn't come with me here. I guess I will miss home a lot."
    player smile "I can always go back to visit. Meanwhile, let's take some photos and send them home while I'm here!"

    call screen text_over_black_bg_screen("A year later...")
    scene bg farm with fade
    player happy "Well, I've been on this farm for a year now."
    player "My day starts with milking the cow and collecting eggs from the hen."
    player "Then I take care of the vegetables."
    player "And before I know it, it will be dusk."

    play sound 'audio/sfx/cricket.ogg'
    scene bg farm dusk with fade
    player laugh "It's so pretty out here on the farm at dusk. The clouds turn a thousand nice warm shades."
    scene bg farm night with fade
    player "Sometimes we have a campfire and s'mores at night."
    player happy "I'm enjoying this farm life so much that I don't think I will return to the city any time soon..."

    play sound 'audio/sfx/alternative_ending.wav'
    call screen text_over_black_bg_screen("{i}Ending: [ending_farmer]{/i}")

    $ add_achievement(
        achievement_name=ending_farmer,
        message=alternative_endind_message
        )
    jump second_chance
    scene bg bedroom with dissolve

    return

label second_chance:
    # stop the regular bgm
    stop music fadeout 1.0

    # this label must be used with jump, not call
    scene bg chaos with dissolve
    # Note to proofreader: this is an omnipotent narrator, so feel free to change their tone
    "Hey [player_name]. Kudos to you for coming this far in the game."
    "That wasn't a bad way to end the story. Not bad at all."
    "But if you think about it, would you have wanted something different?"
    "Would it be possible to teach yourself to code and fulfill your dream of becoming a developer?"
    "Do you wish for an ending like that?"
    "Okay, I'm going to let you in on a little secret."
    "If you like, you can wind back the clock and revisit the choices you've made."
    "If I may ask, did you remember to {b}Save{/b} your progress before making this choice that has taken you here?"
    call screen confirm(_("Did you SAVE your progress and wish to LOAD and get back in time? (It's okay if you answer no. I'll let you in on another secret.)"), 
        yes_action=[ShowMenu('load'), Return()], 
        no_action=Return())

    # if the player didn't load, they get down here
    "Interesting. It looks I have no choice but to let you in on my other little secret."
    "Listen up, alright? I can offer you a second chance to go back to the day you made the choice that took you here."
    "That is, if you so wish."
    "Now answer me this, would you like to get a second chance?"
    menu:
        "Would you like to go back in time and revisit your choice?"
    
        "Time traveling! Let's do it.":
            "You know the rocket ship saying? 'If you're offered a seat on a rocket ship, don't ask what seat.'"
            "Let's rollback in time, brave traveler."
            scene bg tunnel with fadehold

            play sound 'audio/sfx/rewind.wav' # 5 sec
            pause 4.0

            if not plot_rewind_time in persistent.achievements:
                $ add_achievement(plot_rewind_time)

            $ player_base = 'player_base'
            $ player_glasses = 'player_glasses'
            $ calendar_enabled = True
            # resume the bgm
            # $ continue_looping_music = True
            $ random.shuffle(all_music_files)
            $ renpy.music.queue(all_music_files, loop=True, fadein=1.0, tight=True)

            return # return control to the ending label that it jumped from
    
        "Nah. I'm happy with what I have now.":
            "Well, the Buddha said 'There is no path to happiness; happiness is the path.'"
            "I'm glad that you are happy with where you are."
            "I hope this has been a pleasant ride for you, brave traveler."
            "Until next time!"
            stop music
            jump ending_splash

    return

label ending_splash: # alternative endings also jump to here
    $ quick_menu = False
    $ calendar_enabled = False
    # Learn to Code RPG logo
    scene gray90 with Pause(1)
    play sound 'audio/sfx/title_fire_swoosh.ogg'
    show learn_to_code_rpg_logo at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    # freeCodeCamp logo
    scene gray90 with Pause(1)
    play sound 'audio/sfx/title_fire_swoosh.ogg'
    show fcc_logo at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    # Credits, like in the About section from options.rpy
    # use a lighter background because the hyperlinks are dark blue
    scene main_menu overlay with dissolve
    pause 1
    show text _("{size=48}Thanks for playing {b}Learn to Code RPG{/b}!\n\n[about!t]{/size}")
    with dissolve 
    show screen ctc() # click to continue
    pause
    hide text with dissolve

    show text "{size=48}[credits!t]{/size}"
    with dissolve 
    pause
    hide screen ctc
    hide text with dissolve

    $ quick_menu = True
    scene main_menu sepia with dissolve

    "Hey [player_name]. Congratulations on reaching the end of the game!"
    "Hope you enjoyed the ride!"
    "You might be wondering, what's next?"
    "Well, here are a bunch of things you can do."

    default post_game_choices = set()
    menu post_game_choice:
        set post_game_choices
        "Here are some fun things that you can do now that you've finished the game. Select an option to learn more."

        "Check out your achievements and tweet {icon=icon-twitter}":
            "Let's get social! You've made a lot of progress throughout the game and it's time to spread the words."
            "You can view your achievements on the {b}Bonus > Achievements{/b} screen. Click on the {b}Tweet{/b} button next to the achievement to tweet it."
            "If you see a lock next to the achievement, backtrack to some point in the game, try different choices, and see if you can unlock it."
            call screen achievements_screen()
            "Will you be able to unlock all of the achievements? Now that's a dare."
            jump post_game_choice

        "Rate and review this game on itch.io {icon=icon-thumbs-up}":
            "Help us improve the game by rating and reviewing [learn_to_code_rpg_on_itch]."
            show itch_rate at truecenter with zoomin
            "You can find the {b}Rate Game{/b} button in the top right corner of the itch.io game page."
            "Refer to {a=https://itch.io/updates/you-can-now-rate-games}this itch.io article{/a} for more details."
            hide itch_rate
            menu:
                "Would you mind taking a minute to rate and review us?"
                "Sure thing! Take me to the page.":
                    "Thanks! Here's the link to [learn_to_code_rpg_on_itch]."
                "I've done that already!" if not persistent.has_rated_and_reviewed_on_itch:
                    "Awesome. Thank you for your input!"
                    $ persistent.has_rated_and_reviewed_on_itch = True
                "Maybe next time :)":
                    "Of course! Take your time to explore and enjoy the game. You can visit this link anytime from the {b}Bonus{/b} screen."
            jump post_game_choice

        "Star the game's source code on GitHub {icon=icon-star}":
            "Interested in learning about how this game is built? Take a peek into our source code by visiting [learn_to_code_rpg_on_github]."
            show github_star at truecenter with zoomin
            "Better yet, {b}Star{/b} our repository for your reference and {b}Watch{/b} for updates!"
            "Refer to {a=https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars}this GitHub article{/a} for more details."
            hide github_star
            menu:
                "Would you like to check out our GitHub repository?"
                "Sure thing! Take me to the page.":
                    "Thanks! Here's the link to [learn_to_code_rpg_on_github]."
                "I've done that already!" if not persistent.has_visited_github:
                    "Awesome. Enjoy digging through the source code!"
                    $ persistent.has_visited_github = True
                "Maybe next time :)":
                    "Of course! Take your time to explore and enjoy the game. You can visit this link anytime from the {b}Bonus{/b} screen."
            jump post_game_choice

        # "Support this game and other freeCodeCamp.org projects by donating {icon=icon-heart}":
        #     "This game was made possible by all the kind people who donate to support [freeCodeCamp]."
        #     "You can help support our nonprofit's mission {a=https://www.freecodecamp.org/news/how-to-donate-to-free-code-camp/}by donating to us here{/a}."
        #     "Remember you can visit link anytime from the {b}Bonus{/b} screen."
        #     jump post_game_choice
        
        # "Check out the bonus screen for minigames, resources, and more {icon=icon-award}":
        #     "Did you have the chance to enjoy the rhythm minigame while you were busy learning to code, visiting the Hacker Space, and serving coffee?"
        #     "Are you interested in checking out the actual [freeCodeCamp] curriculum and teach yourself to code in real life?"
        #     "Well, you are in luck. The {b}Bonus{/b} screen has everything that you'll possibly need."
        #     # go to the bonus screen
        #     call screen bonus_screen()
        #     "I'm sure you will make good use of the bonus content!"
        #     jump post_game_choice

        "Discover alternative endings {icon=icon-map}":
            "Which ending took you here, if I may ask?"
            "Did you become a developer like you've always dreamed to be? Or did you take up some other job?"
            "Perhaps you discovered that Mint, your adorable home cat, is better at coding than you?"
            "Psssst... Did I just spoil the fact that there are several alternative endings hidden in the game?"
            "The endings you unlocked will be displayed on the {b}Bonus > Achievements{/b} screen."
            "Make sure to {b}Save{/b} your progress often if you want to unlock all of them!"
            jump post_game_choice

        "Gotcha. I'm ready to explore on my own!":
            "Great to hear! Hope you enjoyed the ride!"
            
    return # return to main menu
