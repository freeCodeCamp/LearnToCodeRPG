label ending_barista:
    # this has a certain probability of being triggered during the day
    pass

label ending_cat_who_codes:
    # this has a certain probability of being triggered during the night
    scene bg bedroom night with fade
    play sound 'audio/sfx/keyboard_typing.wav'
    player relieved "Yawwwn...."
    player worry "I heard some strange noise coming from under my bed. Maybe Mint is hungry and woke up?"
    player surprised "Mint? Is that you?"
    player neutral "..."
    player worry "Mint didn't show up. Shall I check what's happening?"
    menu:
        player "Shall I check what's happening?"

        "Check under the bed.":
            pass # continue with the plot

        "Just go back to sleep.":
            player "Nah. Mint's a good cat and won't do damage."
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
    player pout "(Geez... I don't even know if I'm more curious about what Mint has coded up or how a cat is able to do any of these in the first place.)"
    player surprised "(Oh! The website is coming up live!)"
    player "(Wait. I think I know this interface...)"
    player "(Isn't that just [developerquiz]?!)"
    player "(Wait wait wait. So Mint was the one who coded up [developerquiz], the go-to website for aspiring developers?)"
    player pout "(My logic is failing me at this stage...)"
    player relieved "(Maybe this is all a dream?)"
    menu:
        player "Maybe this is all a dream?"

        "I must be dreaming. Let's go back to sleep.":
            player worry "I must be too exhausted and anxious about the coding stuff that I'm hallucinating about Mint writing code."
            player relieved "Let's go get more sleep before my {b}Sanity{/b} hits the ground."
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
    menu:
        player "Shall I keep this as a secret just between Mint and me?"
    
        "Let's keep this a secret and say goodnight to Mint.":
            player "Alright Mint. You are awesome. Keep up what you are doing."
            player "One day I'll catch up to you."
            player laugh "Good night!"
            hide mint_with_pixel_sunglasses
            return
    
        "But it's such a loss for the world if people don't know about Mint!":
            pass

    player happy "(It's a waste if Mint's talent goes unnoticed. Together we can make history!)"
    player "Hey Mint! Mind if I join you and learn to code from you?"
    player "Here, here. I even got matching sunglasses."

    $ player_pixelsunglasses = True
    player laugh "How does that look on me?"
    mint "Meow! (Looks great!)"
    player "You like it? Thanks Mint!"
    mint "Meow! (Now let's get to work!)"
    player "And you are telling me to get to work now? Okay, I'll give it my best shot!"
    $ calendar_enabled = False

    call screen text_over_black_bg_screen("A month later...")
    scene bg hall with fade
    host "And now let's give a round of applause to our hackathon winner: {b}Cat Who Codes{/b}!"
    play sound 'audio/sfx/applause.ogg'
    show mint_with_pixel_sunglasses
    player laugh "Wow... We managed to win the first place all thanks to Mint. This is awesome!"
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
    call screen text_over_black_bg_screen("{i}Ending: Cat Who Codes{/i}")

    # TODO: Twitter share
    
    $ player_pixelsunglasses = False
    jump ending_splash # return to main menu

label ending_cs_tutor:
    # this has a certain prob of being triggered during dinner
    pass

label ending_office_worker:
    # this has a certain prob of being tiggered during the day once the player has failed a coding interview once
    pass

label ending_farmer:
    # this is triggered if sanity is too low
    pass