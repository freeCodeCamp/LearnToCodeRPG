label sanity_event_player:
    player "Ugh I feel burnt out."
    player "Maybe we need to take it slow."
    player "Let's call it a day early."

label sanity_event_player_pet:
    player "My eyes hurt. My brain even more so."
    player "I wish I could get a pet."
    player "Let's go check out some pets."
    scene bg pet_shop

label sanity_event_annika_boba:
    player "I'm soooo tired. I could barely keep my eyes open."
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    player "(A call from Annika? Hmmm... I could use a break)"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    annika "Hey [persistent.player_name]!"
    annika "Just wanna call and check up on you."
    annika "I know you've been studying hard and all that, so I think you totally deserve a treat!"
    annika "What do you say if we grab boba tea together? There is a new place nearby."
    player "That'd be... nice..."
    player "(I really want to go, but I have work...)"
    annika "Come on. You need a break. Don't burn yourself out grinding code."
    annika "Otherwise it'll be no fun!"
    player "Haha you are right."
    player "What's the place called?"
    annika "Shhhh it's a surprise. I'll be at your place in 10 and we can go together."
    player "Sounds good!"

    scene bg boba_shop
    annika "So I was watching this really fun coding tutorial where they built an AI chatbot."
    player "Wow that sounds fun..."
    annika "I know! I'm picking up some Machine Learning myself. Maybe I will be able to build a chatbot that speaks like a movie star."
    player "That'd be awesome!"

    scene bg bedroom_night
    player "Annika and I ended up chatting the whole afternoon."
    player "It felt really nice, though. I feel so much more refreshed."
    
    $ player_stats.change_stats('Sanity', 10)