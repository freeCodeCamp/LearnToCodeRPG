label start:
    stop music fadeout 2.0
    scene bg laptop_screen with dissolve

    # get some action and conflict in here :)
    interviewer "So - are you feeling excited?"
    player "U-um... I definitely am. I'm just a bit nervous..."
    interviewer "Don't sweat it! Everyone gets nervous during the interviews - even the pros."
    interviewer "How about we start with your name?"
    # TODO: more customization like gender, pronouns, life story

    $ player_name = renpy.input(_("What is your name? {color=[red]}*{/color} (Type your name and hit Enter. This name will be used throughout the game and you cannot change it unless you start a new game.)"), default=_("Lydia"))
    $ player_name = player_name.strip()
    if player_name in vip_names:
        $ vip_profile_url = vip_names[player_name]
        "[player_name]? What a coincidence! Our VIP team member {a=[vip_profile_url]}[player_name]{/a} will be honored to hear that."
        # TODO: Easter Egg
    # handle empty string case by assigning default name
    if not player_name:
        $ player_name = _("[player_name]")

    interviewer "It's nice to meet you, [player_name]! So I understand that you're here for our coding interview?"
    player "I am!"

    menu:
        interviewer "Great! We'll start whenever you're ready."

        "Guess I have no other options. Let's start!":
            pass

    # timed menu
    $ timeout = 5.0
    # Set the label that is jumped to if the player doesn't make a decision.
    $ timeout_label = "start_interview_question2"
    interviewer "First question."
    menu:
        interviewer "Assuming P = NP, how many raccoons is too many raccoons?"

        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

label start_interview_question2:
    play sound 'audio/sfx/punch.wav'
    with vpunch
    $ timeout_label = "start_interview_question3"
    "Second question."
    menu:
        interviewer "In Python, what is a generator?"
    
        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

label start_interview_question3:
    play sound 'audio/sfx/punch.wav'
    with hpunch
    $ timeout_label = "start_after_interview"
    "Third question."
    menu:
        interviewer "How do you think Sasquatch feels about APIs?"
    
        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

label start_after_interview:
    # reset to non-timed choices
    $ timeout_label = None
    play sound 'audio/sfx/punch.wav'
    with vpunch

    interviewer "Thanks for taking the time to complete our coding interview."
    interviewer "Before you go, please take some time to fill in your basic information so we can get to know you better."
    interviewer "The fields marked with {color=[red]}*{/color} are required."

    # TODO: birthday Easter Egg
    # "What is your birthday?"

    # TODO
    # player_pronouns = renpy.input("What's your preferred pronoun?")

    # questions with no substantial consequences
    menu:
        interviewer "How did you hear about this opportunity?"
    
        "Email":
            interviewer "Cool! We're glad that you're here!"
    
        "Career fair":
            interviewer "Awesome! Career fairs are great places to find opportunities."

        "Job posting websites":
            interviewer "Ah - I knew it'd be worth getting our recruiters to post on those sites!"

        "Referral":
            $ referral_name = renpy.input(_("What is the first name of your referral? (Type something and hit Enter)"))
            # Easter egg :)
            if referral_name in vip_names:
                $ vip_profile_url = vip_names[referral_name]
                play sound 'audio/sfx/system_processing.wav'
                "System processing... Looks like you were referred by a VIP team member. That's awesome! We'll highlight this on your profile."
                "And we'll make sure to let our VIP team member {a=[vip_profile_url]}[referral_name]{/a} know!"
           
                $ add_achievement(plot_vip)
            else:
                "Hmmm... We aren't able to locate that person in our employee database. Maybe you made a typo?"

        "Others (Please specify)":
            $ renpy.input(_("How did you hear about us? (Type something and hit Enter)"))
            "Well, we aren't sure how you came across this opportunity through the portal you specified, but we're glad you're here!"

    menu:
        interviewer "Would you like to opt in to our recruiting email list?"
    
        "Yes":
            "Way to go! We'll notify you about all the events and opportunities."
    
        "No":
            "Maybe next time?"
    
    interviewer "And that'll be all! Thanks so much for coming, [player_name]."
    player "N-no, thank you - I appreciate your time."
    interviewer "We'll call you if we decide we'd like to move you forward to the offer stage."
    player "Thank you..."
    player "(Jeez... I'm really not sure how I did in that interview!)"
    player "(To be fair, it wasn't that long ago that I was a total newbie. And look at where I am now!)"
    player "(It feels like it was only yesterday that I decided to teach myself programming...)"

label stage1:
    # use call instead of show b/c the screen will return after the timer finishes
    call screen text_over_black_bg_screen(_('About three months ago...'))
    call screen text_over_black_bg_screen(_("{i}Prologue: Chapter 1 - We're just getting started!{/i}"))

    scene bg kid_home
    $ calendar_enabled = True
    # start the music here
    # $ continue_looping_music = True
    $ renpy.music.queue(all_music_files, loop=True, fadein=1.0, tight=True)

    # Stage 1. player background
    show boy orange
    player smile "Okay, we can pick up from here tomorrow."
    kid "Okay - thanks [player_name]! I appreciate the help."
    kid "By the way, I'm going to miss my tutoring session tomorrow, so don't wait up."
    player "What? Mason, are you sure? Your science grades could really use some work."
    player worry "I don't think we should be missing any sessions."
    kid "Nah, you've got it all wrong, Ms. Wallflower - I AM taking science classes!"
    kid "I'm learning how to code in my robotics club after school!"
    player surprised "Robotics? Jeez... that sounds harder than your advanced physics class."
    kid "I know - I was surprised too, but it's actually WAY easier - and way more fun!"
    kid "I get to learn to program, like my older brother. He's a software engineer."
    kid "My teachers told me that if I take this elective, I'm off the hook for advanced physics."
    player "Oh yeah?"
    kid "Yep! And I've been thinking... I really like this stuff. Maybe I'll do it when I grow up?"
    kid "Anyway, see you Ms. Wallflower!"
    player smile "Bye Mason."
    player neutral "(Man... Mason is only 16, and already knows what he wants to do?)"
    player worry "(I graduated from college 8 months ago and I STILL feel like I don't know where I'm going.)"
    player "(It seems like everyone from my year is settling into their careers.)"
    player sweat "(This tutoring job is okay, and definitely keeps me busy, but I don't make as much as I'd like...)"
    player -sweat neutral "(It's been a long day. I'm just going to head home.)"

label stage2:
    # Stage 2. player's decision to learn to code
    # player returns home
    scene bg living_room night with blinds

    player "Mom, Dad, I'm home!"
    dad "[player_name]! How's my little Tulip?"
    player sweat "Dad! Aren't I a bit old for you to be calling me that?"
    dad "Aw, you're never too old! I still call your mom “Rosie”, don't I dear?"
    mom "You sure do! I love it as much as I did when we first started going steady..."
    player "(Jeez. Those two are as lovey-dovey as ever.)"
    player "(Maybe I can change the subject.)"
    player -sweat smile "So! What have you two been up to today?"
    dad "Oh! I was just over at the Anderson's house, chatting about Jerry - you remember Jerry?"
    player surprised "I do. He stole my crayons when I was four."
    player "Are we talking about crayon-stealing Jerry?"
    mom "Sweetheart, you've got to get over that."
    dad "Well, Jerry just landed his first job out of college. You'll never guess what he does!”"
    player sweat smile "... steals crayons for a living?"
    mom "He's a software engineer!"
    player -sweat surprised "Really? Jerry? Jerry Anderson?"
    mom "He is! His parents say that he really likes the work. I've always wondered what those computer whizzes do."
    mom "Something amazing, I'm sure!"
    mom "Anyway, ready for dinner?"
    player "(Hm... another programmer? Strange. Seems like everyone's getting some kind of bug...)"
    player smile "(Heh. A computer bug.)"
    mom "[player_name]? I asked if you were hungry?"
    player "Oh, right! Sure Mom, thanks."

    play sound 'audio/sfx/kitchen_beep.ogg'

    # dinner scene
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    $ show_random_dinner_image()
    dad "So here's the best part about my day..."
    player laugh "Haha that's hilarious!"
    mom "What plans do we have for the weekend?"
    player "I'm up for anything!"

    scene bg bedroom with blinds
    player "Phew - I'm stuffed!"
    mint "Mew!"
    player "Oh hey, Mint! How's my favorite kitty doing?"
    mint "Meow!"
    mint "Meow?"
    player "Yeah... I'm feeling a little down in the dumps today."
    player "I'm beginning to think this tutoring stuff isn't enough, Mint."
    player "Mom and Dad don't mind me living here at all, but want to be able to help out, at least a little."
    player worry "I'm barely making enough to cover stuff like my phone bill."
    player worry "Maybe I ought to look for another job in addition to my tutoring work. It's only a few times a week right now."
    player neutral "I guess I'll sign up for a job hunting site and set up notifications."
    player "..."
    player "..."
    player surprised "Whoa - is that a response already?"
    player surprised "Should I pick up?"
    menu:
        "Check phone":
            show smartphone
            player smile "Looks like I was right - the local cafe down the street is hiring right now."
            player smile "It looks like they'd like me to come in for an interview. Maybe I can work there?"
            player "It's right down the road, so I'd just have to walk."
            hide smartphone
            "(Congratulations! You just made your first choice.)"
            "(Choices can affect gameplay, and how stories progress.)"
            "(There aren't necessarily right or wrong choices... just consequences or rewards!)"
        "Ignore":
            mint "Mew!"
            player "You're right Mint."
            player "As tired as I am, I really do think I need to check this. Let me take a look..."
            show smartphone
            player "Looks like I was right - the local cafe down the street is hiring right now."
            player "It looks like they'd like me to come in for an interview. Maybe I can work there?"
            player "If it's only right down the road, I'd just have to walk."
            hide smartphone
            "(Congratulations! You just made your first choice.)"
            "(Choices can affect gameplay, and how stories progress.)"
            "(There aren't necessarily right or wrong choices... just consequences or rewards!)"
    player relieved "Phew! I guess it's a good thing that I answered!"
    player "I could have missed that opportunity and stayed in a funk like I have been all day."
    "([player_name] is right: It may be a good idea to save your progress when you're about to make a choice, start a new chapter, or just to be safe.)"
    "(You can save by clicking the {b}Save{/b} button at the bottom-right of the screen.)"
    "(Would you like to save your progress now?)"
    "(Thanks for entertaining your friendly Save Reminder! Now back to the story...)"
    play sound 'audio/sfx/social_media_notification.wav'
    show smartphone at truecenter
    player "What? Another notification?"
    player "..."
    player "Oh - it's Jerry."
    player "It looks like he's posting a selfie from his new office."
    player "It looks pretty cool... and what a view!"
    player "First Mason, and now Jerry? It seems like everyone is learning to program."
    player "I mean, six months of self-paced learning, and then an almost six-figure job?"
    player "If Mason is only 16 and he's learning,"
    player "and Jerry Anderson is..."
    player "... JERRY,"
    player "then maybe it's something I can do, too?"
    mint "Mew!"
    player "Aw. Do you believe in me, Mint?"
    player "Thanks."
    player "(Mom and Dad are super supportive, but Mint is probably the biggest reason I decided to move back home.)"
    player smile "(Look at those little eyes. And her little toe beans!)"
    player smile "(It's hard to tell her “no” most of the time. Not that I want to.)"
    player "(Alright - I think I've made a decision.)"
    player smile "(I'm going to do it! I'm going to learn to program, too.)"
    player "(I'll start tomorrow morning.)"
    player "Welp, Mint - let's get to bed. It looks like I have an interview tomorrow."
    player "I've got to fund myself somehow while I learn, right?"
    mint "Mew!"

    call save_reminder from _call_save_reminder

    call screen text_over_black_bg_screen(_('{i}Prologue: Chapter 2 - Piping hot!{/i}'))
    $ calendar.next()
    scene black
    scene bg bedroom with eyeopen

    player neutral "Yawn"
    play sound "audio/sfx/meow1.wav"
    show mint
    player "Good morning Mint!"
    mint "Meow!"
    hide mint
    player "Today is the day that my programming journey begins!"
    player smile "Now that I've had time to sleep on it, I'm getting pretty excited."
    player "I think I even have a bit of time before my interview. Starting with a bit of research wouldn't hurt!"
    player neutral "Where shall we start? Maybe I should find some free online resources like everyone else is doing?"
    player "Oh - here's a video about the top 10 tech skills worth learning this year. Let's check that out!"

    # now the quick menu screen show the button to access stats
    $ stats_unlocked = True

    player smile "I'll keep track of my progress on my phone."
    show smartphone at truecenter
    "(Click on the {icon=icon-smartphone} {b}Stats{/b} button on the bottom-right corner of the textbox to view your progress.)"
    "(There, you can keep track of what you've been learning, your energy, and other useful pieces of information.)"

    hide smartphone
    player "Alrighty. Here goes nothing..."
    player "..."

label stage2_stats_change:
    player surprised "Okay... so JavaScript and Java are different languages? Really?"
    $ player_stats.change_stats(CS_KNOWLEDGE, 1)
    player neutral "Oh - and one of them is for web dev and the other is for making phone apps. Which is which?"
    $ player_stats.change_stats(ENERGY, -5)

    player "And there are print statements and print() functions. One is for Python 2, and one is for Python 3?"
    player "How many Pythons {i}are{/i} there, exactly?"
    player "Two snakes are already too many snakes..."
    $ player_stats.change_stats(CS_KNOWLEDGE, 1)
    player "I remember one video saying that Python 2 is outdated. Does that mean that I don't have to learn it?"
    $ player_stats.change_stats(ENERGY, -5)

    player "Maybe I shouldn't even bother with learning Python 3."
    $ player_stats.change_stats(CS_KNOWLEDGE, 1)
    player "Soooo this video says that Python 2 is outdated. Does that mean I don't have to learn it?"
    player worry "Maybe I should just skip Python 3, too? When do we go to Python 4?"
    player "Someone may just decide that Python 3 is too old-fashioned before I even get a chance to learn it."
    $ player_stats.change_stats(ENERGY, -5)

    player "Hmm... and by the looks of it, maybe I shouldn't learn Java for the same reason. It's really old. Right?"
    $ player_stats.change_stats(CS_KNOWLEDGE, 1)
    player 'It says on this website that people nowadays are hyped up about something called, "Kotlin"?'
    player "Sounds like over-the-counter medication for when you get the sniffles."
    $ player_stats.change_stats(ENERGY, -5)

    player surprised "Wait... there's JavaScript AND TypeScript? How many of these are there?"
    $ player_stats.change_stats(CS_KNOWLEDGE, 1)
    player worry "Are they all cousins or something?"
    $ player_stats.change_stats(ENERGY, -5)

    player "Maybe I can find a job posting I like and start learning those required skills."
    play sound 'audio/sfx/punch.wav'
    with hpunch
    player pout "But what is front end, back end, or full stack? What are the differences?"
    player "When I try to look any of them up, I find two more words I don't know. Then when I look those up, there are even MORE pieces of vocabulary I don't recognize."
    play sound 'audio/sfx/punch.wav'
    with hpunch
    player "What are DevOps and Cyber Security?"
    play sound 'audio/sfx/punch.wav'
    with hpunch
    player "And it says here that this one company is using their own programming language that no one else is even using?"
    player "Why would they do that?"

    # hard-reset player's CS knowledge :)
    $ player_stats.set_stats(CS_KNOWLEDGE, 0)

    with vpunch
    play sound 'audio/sfx/stats_change_doom.wav'
    player "Ugh... this is so frustrating!" 
    player worry "Jeez... maybe this coding thing isn't for me? Maybe it's too hard?"
    show mint 
    mint "Meow!"
    player neutral "What's wrong Mint? Did I scare you? I'm sorry..."
    mint "Meow!"
    player "Hm...? Oh! I'm going to be late! I've got to hurry to that interview - thanks for the heads up, Mint!"
    mint "Meow."
    hide mint

label stage3:
    # Stage 3. Annika
    call screen text_over_black_bg_screen(_('{i}Prologue: Chapter 3 - Everyone could use a friend like Annika.{/i}'))
    call screen text_over_black_bg_screen(_('Four days later...'))
    scene bg cafe with fadehold

    player smile "Thanks! Come again!"
    player neutral "(Wow - it's only been a few days, and I feel like I know how to make every coffee in existence.)"
    player "(The free coffee is nice, but after smelling it for so many hours, it gets to be a bit much. Maybe I should go on my break?)"

    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"

    player "Perfect timing. I wonder who this is?"
    annika "[player_name]!"
    hide smartphone
    show annika
    player smile "Annika?"
    player happy "Wow, it's been so long! How have you been, girlie?"
    player neutral "I haven't seen you since we were moving out after graduation! Mom and Dad miss having you over!"
    annika laugh "Please - they saw me enough while were growing up! I bet your mom is glad I'm not tracking mud into your house like I used to whenever I visited."
    player laugh "Hey, it was a team effort. You didn't make all those stains yourself!"
    player neutral "So what have you been up to? Has your job search been going well?"
    annika "Things have been so well - like you have no idea how well!"
    player happy "Well don't keep me in suspense! What's going on?"
    annika "I just got a job offer!"
    player happy "Oh?" 
    annika "Yeah! And not just any job offer - a WEB DEVELOPMENT job offer!"
    player surprised "Web development? Seriously?!"
    player neutral "(What is UP with everyone learning to program, lately?)"
    player "I thought your degree was in graphic design?"
    annika "It was! But then I was kind of messing around with user interface design for a website I was dreaming up. When I posted it online, a recruiter saw it!"
    annika "We got to talking, and after going through their screenings, they decided they wanted me for the position!"
    player smile "Whoa!"
    player neutral "What's user interface design? And what do they have you doing all day?"
    annika "Oh, it's SO cool! Basically, it involves..."
    "(You listen to Annika excitedly talk about her new position. You're incredibly happy for her, but still have a sinking feeling in your chest.)"
    player surprised "Wow."
    player pout "That's... great."
    annika "Hey - what's wrong?"
    annika "You sound like you just dropped your ice cream on the floor."
    player  "Ice cream would be great right about now."
    player "I'm currently working at a coffee shop - it's all I've been smelling all day!"
    player "I'm just upset because... well..."
    player "You and a few other people that I know or keep crossing paths with are getting into programming."
    player "But I spent a bit of time looking things up last night, and NOTHING was sticking."
    player "I think I'm just not cut out for it."
    annika @ laugh "What?! [player_name], no!"
    annika "You're legitimately one of the smartest people I know! The last I checked, I thought you landed a tutoring position?"
    annika "You HAVE to be smart to do that."
    player pout "I don't know... it's just hard to feel good about something when you're not excited about it." 
    player pout "You just lit up while you were talking about your job. I definitely want something like that myself." 
    annika "[player_name]..."
    annika "Look - you'd be a GREAT programmer. And if it's really what you want to do,"
    annika "I'll support you every step of the way!"
    player smile "Wow... really? You'd do that for me?"
    annika "Of course! You took the fall for me that time I knocked over your mom's nice vase."
    player laugh "I had to!"
    player neutral "She would have banned you from the house for a week if I hadn't!"
    annika "Everything is going to be just fine, [player_name]. In fact - I've got something super cool to show you."
    annika "I'm not going to be freed up from work for about three days, but once I am, I've got something that'll help you with your programming goals!"
    annika "Do ya trust me?"
    player neutral "..."
    player laugh "It's hard not to with all that energy!"
    annika "Good!"
    annika "I've gotta go - my lunch break is almost over."
    annika "But until we meet up in a few days, here's what you should do - there's this awesome website called developerquiz.org."
    annika "It's got free practice programming questions - I think that you should go there and do a few questions a day to get your feet wet!"
    player neutral "Okay. But what if I don't know the answers?"
    annika "Easy! freeCodeCamp!"
    player "Free... what?"
    annika "freeCodeCamp! It's this amazing website where you can learn to program, completely free!"
    annika "It's what I used to get my job now." 
    annika "I took their Responsive Web Design course, and within a few months of intense study, I was ready to start interviewing."
    player "Really? Just a few months?"
    annika "Well... learning to program is less of a race and more of a marathon. You get what you put into it."
    annika "Welp! Anyway - like I said, I've gotta go."
    annika "Try out the website! And if you hear any techy buzzwords, be sure to ask me about them when we meet up, okay?"
    player smile "Okay. Thanks, Annika." 
    annika "Anytime, Wallflower!"

    scene bg cafe with dissolve

    player neutral "(Alright... my shift is almost over.)"
    player "(Talking with Annika has actually got me excited again, I think!)"
    player "(She said to ask her to explain if I hear something I don't understand,)"
    player "(but what did she say right before she got off the phone?)"
    player "(Responsive web design?)"
    player "(I know what web design is, but what does it mean when something is responsive?)"

    "(You just collected a Buzzword! Buzzwords are words that are really popular in the IT scene.)" 
    "(When you hear a Buzzword, be sure to add it to your to-do list, and ask Annika about it later.)"
    player "Come to think of it, maybe I'm in an ideal position. There are a lot of people here with computers every single day."
    player "I used to come to coffee shops to get work done in college. Maybe developers like doing that, too?"

    show girl flipped red at left
    show boy orange at right
    girl "Hey! Did you hear that our school is getting a computer club?"
    boy "What? No way - what do you do at a computer club? Play a lot of video games?"
    girl "Even better - we get to learn to code stuff, and maybe even make our own video games!"
    boy "Cool! What is the club learning about now?"
    girl "We're learning about Python! Mr. Stevens runs the club, and he says that we should have a {bt}Hackathon{/bt} so we can all practice."
    boy "Hackathon? What's that...?"
    girl "Well, from what I understand..."
    hide girl
    hide boy

    player surprised "Oops! I wasn't intentionally eavesdropping on those kids. But I think I remember reading about HTML and CSS - I just don't know exactly what they have to do with each other."
    player smile "I know! I'll make another To-Do list item to ask Annika about it." 

    $ todo_list.add_todo(todo_ask_hackathon)
    $ topics_to_ask.add('Hackathon')
    player "Alright! Back to my shift."

    $ add_achievement(plot_barista_discover)

    player neutral "Alright - it's about time to go home!"

    call save_reminder from _call_save_reminder_1

label stage4:
    # player goes back home
    scene bg bedroom with fadehold
    player relieved "Phew... It's been a long day at work."

    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    player "Hm? I wonder who that could be?"
    pause 2.0
    hide smartphone

    show annika
    pause 1.0
    annika "Hey, superstar! Is now a good time to talk?"
    player laugh "Sure! I just got off of my shift. What's up? Miss me already?"
    annika "Ha-ha. You're acting like you don't want the link to the {bt}best programming resource{/bt} that I know!"
    player laugh "Okay, okay! No more teasing - what is it called?"
    annika "It's this website called [freeCodeCamp]. I know you said you wanted to study tonight, so I wanted to make sure you had the name of it!"
    player laugh "Thanks Annika, I will. You're the best!"
    hide smartphone
    hide annika

    player "(Let's add it to my To-Do list.)"

    $ todo_unlocked = True
    $ todo_list.add_todo(todo_check_fcc)
    "(On the {icon=icon-smartphone} {b}Stats{/b} screen, you can toggle between showing your stats and showing your To-Do list.)"

    scene bg laptop_screen night with dissolve
    player neutral "Let's check out this awesome resource that Annika was talking about."

    menu stage4_guess_name:
        player "What was it called again?"

        "freebieGoodie":
            player pout "That doesn't sound like the right name."
            player "My memory must be playing tricks on me."
            jump stage4_guess_name

        "coolCodersCamp":
            player pout "That doesn't sound like the right name."
            player "My memory must be playing tricks on me."
            jump stage4_guess_name

        "freeCodeCamp":
            pass

label stage5:
    player smile "[freeCodeCamp]. That sounds right! Let's check it out."
    show fcc_curriculum at truecenter with dissolve
    player happy "Wow. Their curriculum is super comprehensive. They also offer certifications that I can showcase on my résumé. Neat!"
    player "What should I start with?"
    hide fcc_curriculum

    # booleans mark whether a choice has been visited
    default stage5_choose_curriculum_visited = set()

    menu stage5_choose_curriculum:
        set stage5_choose_curriculum_visited

        "Responsive Web Design":
            player pout "Hmmm... right. Annika was talking about this one... Will I be able to follow along?"
            player "Maybe let's look some more?"
            jump stage5_choose_curriculum

        "JavaScript Algorithms and Data Structures":
            player pout "I remember hearing about JavaScript. Or wait, maybe that's Java?"
            player "Algorithms and data structures kind of sounds like math... I can do math well enough, but it's not my favorite subject."
            player "What other curriculum options do I have?"
            jump stage5_choose_curriculum

        "Front End Development Libraries" :
            player pout "Front end development? Interesting... if there's a front end, there's got to be a back end, right?"
            player "Could there even be a middle part...?"
            player "Hm... let's see what else there is."
            jump stage5_choose_curriculum

        # not enough space on small devices
        "Data Visualization" if not renpy.variant("small"):
            player pout "I know there's a lot of hype about big data, but can I really do that without a Ph.D.?"
            player 'How big is "big" data anyway? Trucks are big. Maybe it\'s truckloads of data?'
            jump stage5_choose_curriculum

        "Back End Development and APIs":
            player pout "I guess I've found the back end to my front end! They definitely sound like they should go together."
            player "Maybe learning both is biting off more than I can chew? I have no clue what the work entails..."
            player "Let's look for something simpler."
            jump stage5_choose_curriculum

        "Quality Assurance":
            player pout "Quality assurance? That sounds like I'll be on a digital conveyor belt making sure all the cookie packs weigh more or less the same."
            player happy "Nice, warm, and chewy cookies... I love cookies. Hope Mom still keeps some in the kitchen cookie jar."
            show mint
            mint "Meow?"
            player "Hey Mint. You want a cookie as well?"
            mint "Meow meow~"
            hide mint
            menu:
                "Let's go grab a cookie from the kitchen":
                    call stage5_cookie from _call_stage5_cookie

                "Enough cookie talk! Let's go back to studying":
                    pass

            with vpunch
            player pout "Wait. I got distracted. Where was I? Was I browsing the course categories or something? Oh. I have this quality assurance tab open."
            player "At any rate, I don't think quality assurance is something I want to learn."
            jump stage5_choose_curriculum

        # "Scientific Computing with Python":
        #     player pout "Scientific computing? I'm not that much of a science person and I don't see myself becoming a scientist either."
        #     player "Plus I don't know anything about Python yet."
        #     jump stage5_choose_curriculum

        "Data Analysis with Python":
            player "Data analysis sounds cool..."
            player pout "But I'm not a fan of snakes. I know they're not supposed to be slimy, but they look that way..."
            jump stage5_choose_curriculum

        # "Information Security":
        #     player pout "What can I do after learning about information security?"
        #     player "Hack into others' computers? Stop attackers from hacking into other people's computers?"
        #     player "That sounds pretty intense. I'm not sure if I can handle that."
        #     player "Is there something more neutral on the list?"
        #     jump stage5_choose_curriculum

        "Machine Learning with Python":
            player happy "Machine learning. Wow. That sounds cool."
            player "I'm really interested in teaching machines to learn."
            player "Just think about it. Teaching machines to chat like humans... Maybe I could get one to make my doctor's appointments for me?"
            player "No wonder everyone is hyped about artificial intelligence these days."
            player "..."
            player pout "But it looks hard. I know nothing about machine learning, except that there are so many memes about how machine learning is nothing but math."
            player "Math... linear algebra... that kind of thing."
            player "I'm certain I could do it. But the question is, do I want to do it all day?"
            player "Maybe I should start with something more basic?"
            jump stage5_choose_curriculum

        "Let's just wait until tomorrow and ask Annika for advice":
            player pout "Hmmm... So I've done about as much research as I could on my own."
            player neutral "Now that I'm starting to hit a brick wall, I should probably get Annika involved."
            $ todo_list.add_todo(todo_ask_curriculum)
            player smile "Added it to my To-Do list!"
            player "Well, I did accomplish something today. Now at least I know what [freeCodeCamp]'s curriculum is about. That's one item off my To-Do list."
            $ todo_list.complete_todo(todo_check_fcc)
            show mint
            mint "Meow!"
            player smile "You think that's a good idea too, Mint?"
            player relieved "Okay, let's get some rest. Tomorrow is another day."
            hide mint

            call save_reminder from _call_save_reminder_2

            jump stage5_annika

label stage5_cookie:
    scene bg kitchen night with blinds
    dad "Hey Tulip - taking a break from all the studying?"
    mom "Your dad and I are really glad that you're continuing to learn new things after college, but don't push yourself too hard, okay?"
    player happy "Haha thanks Mom. I'm doing just fine."
    player "I'm just deciding on what CS topic to learn so I can get a job in tech like Annika."
    dad "Ooh, Annika has a job in computer science now? Good for her!"
    mom "I'm absolutely sure you can do it, too. Just know that we are always here if you'd like to talk, or vent, or get a hug."
    player "I will. Thanks Mom."
    mom "Now before you go to bed - I've made cookies! Why don't you take some back to your room to study?"

    scene bg bedroom with blinds
    show cookie at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player laugh "Mmmm... Mom's cookies are the best."
    hide cookie

    $ add_achievement(plot_cookie)
    return

label stage5_annika:
    # the next day
    $ calendar.next()
    scene black
    scene bg bedroom with eyeopen

    show smartphone at truecenter
    play sound 'audio/sfx/alarm.wav'
    pause 1.0
    hide smartphone
    
    player pout "Ahhh... my alarm... It's a new day already?"
    player smile "What's on our To-Do list today?"
    $ renpy.show_screen(PLAYER_PHONE_SCREEN, _layer='transient', tab_showing=TODO)
    player happy "Right - Let's give Annika a call and ask about the CS curriculum."
    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    hide smartphone

    show annika

    player happy "Morning, Annika!"
    annika @ laugh "Morning! As energetic as ever, I see."
    player "Haha all thanks to you!"
    annika "What's up?"
    player "So I've been checking out [freeCodeCamp] as you suggested."
    player "I think its curriculum looks solid."
    player pout "The thing is, I have no idea what to learn. Web dev, data science, machine learning..."
    player "They all look super complicated. I bet you put in a lot of hard work to finish each certification."
    player "Remind me - which one did you do again?"

    annika "Oh, I did the web design one. What was it? {a=https://www.freecodecamp.org/learn/responsive-web-design/}Responsive Web Design{/a}?"
    annika "If I remembered anything from my college CS minor, it's those web markup languages."
    player "Ahh I see."
    player pout "(So Annika managed to pull through the curriculum because she had some experience from college. Plus she has a real gift for design.)"
    player worry "(I'm not like that... There's no way I can do this...)"

    annika "Whoa there Wallflower - I know what you're thinkin'."
    annika '"She went to college for something tangentially related - it must have been so easy for her!"'
    player "..."
    player sweat smile "You caught me."
    player "(I hate when she does that!)"
    annika "Look - checking out their curriculum is a huge step forward."
    annika "You're getting your feet wet! You're deciding if you like this or not."

    show annika serious
    annika "Trust me, I was just like you when I first started."
    annika "I was clueless, so I reached out to [freeCodeCamp]'s online community."
    annika "Remember that resource, [developerquiz] that I told you about?"
    annika "Have you gotten started on it yet? It's what my college recommended I do."
    annika "I found those bite-sized quizzes fun and easier to digest."
    annika "Plus these quizzes cover a lot of fundamental CS knowledge. You can think of it as an intro curriculum to CS for complete noobs."
    annika "How does that sound?"

    player worry "Ehh... Even with that, I'm not sure if I can make it through all the quizzes and CS concepts on my own..."
    player pout "What if I run into something that I can't understand?"
    player worry "What if the quizzes get too hard like they always did in college, and I lose my motivation?"

    show annika
    annika "That's totally okay! In fact, what I love about [freeCodeCamp] is that they have an entire community that can help you out and cheer you on."
    show annika laugh
    annika "And I already told you - {b}we're accountability buddies!{/b}! You're not going at this all alone."
    player happy "Thanks Annika. I know I can count on you."
    annika "Any time!"

    show annika
    annika "Well, I'm about to head out to work. Talk later!"
    player laugh "Best of luck with work! Let me know how it goes."

    play sound 'audio/sfx/phone_hangup.wav'
    hide annika

    player smile "Okay. Now I've asked about the curriculum. One To-Do item off the list."
    $ todo_list.complete_todo(todo_ask_curriculum)
    player "I can ask Annika about other topics another day."
    player "Now my new To-Do would be to ramp up my CS knowledge."
    $ todo_list.add_todo(todo_learn_cs)
    player happy "Sounds like a plan!"
    player "Time to go work my barista shift."

    call save_reminder from _call_save_reminder_3

    # I think that we should have more to this scene rather than just adding it in to have content.
    # We want to see something happen here. We can add something on a second pass :)
    # scene bg cafe with fadehold
    # play sound 'audio/sfx/cafe_pour.wav'
    # show coffee at truecenter
    # pause 5
    # hide coffee

    # player neutral "Weird... I don't see too many people in the cafe today."
    # player relieved "Maybe because it's a work day? Oh well."
    # player laugh "More coffee for me!"

    # scene bg cafe dusk with fadehold
    # play sound 'audio/sfx/cafe_pour.wav'
    # show coffee at truecenter
    # pause 5
    # hide coffee
    # player "That's about it for my shift. Not much happened."
    # player "Let's head home early to squeeze in some studying tonight, just to keep up the momentum!"

label stage6:
    # Stage 6. Trials
    call screen text_over_black_bg_screen(_("{i}Prologue: Chapter 4 - Feeding the study bug{/i}"))

    scene bg bedroom with fade
    player smile "I'm finally home! Let's head over to [developerquiz] and try out some quiz questions."
    scene bg laptop_screen with dissolve
    player surprised "Looks like they even divided the questions into subcategories like HTML, CSS, and JavaScript."

    # unlock CS Knowledge subcategories here
    $ player_stats.subcategory_stats_map = {stats_name: 0 for stats_name in v1_skills}
    $ renpy.show_screen(PLAYER_PHONE_SCREEN, _layer='transient')

    player smile "Well, guess I need to track my progress for each subcategory."
    "(Your {b}CS Knowledge{/b} is calculated as the average of all subcategories. So make sure to study for each of the categories!)"
    player "For each session, I'll need to complete four multiple choice questions from the chosen category."
    player happy "Let's give it a go!"

    call study_session_choose_topic from _call_study_session_choose_topic_2
    call study_session from _call_study_session

    $ add_achievement(milestone_start_curriculum)

    "(Congratulations on starting your coding journey! The path will be long, but worth it in the end.)" 
    "(Whether you're learning to program to land a new job, transition into a new career path, build your dream app, or just for fun, the freeCodeCamp RPG (and the freeCodeCamp community!) are here to help.)"
    "(To use this game most effectively, we suggest studying alongside playing! By answering quiz question each day with [player_name], you have the opportunity both to learn, and learn where you need improvement.)" 
    "(If you get a question wrong and don't understand a concept, don't be discouraged!)"
    "(Just click the “Learn More” button if you get a question wrong. We recommend clicking it when you get something right, too - it never hurts to review!)"
    "(If you get stuck, or feel discouraged, feel free to reach out to your freeCodeCamp community on our forum.)"
    "(Remember - your journey with [player_name], as well as your own personal programming journey, have just begun! Carpe that Diem!)"
    "(Happy coding!)"

    scene bg bedroom with dissolve
    player relieved "Phew... I'm finally done with these questions. What a day..."
    player "I'm tired... and I may not be a developer yet,"
    player smile "but I'm feeling more fired up than ever about making positive change!"
    player "Maybe it's best for my productivity if I take an entire day off to study?"
    player "Let's give that a try tomorrow."
    show mint
    mint "Meow~"
    player smile "Are you trying to say 'Good job' to me? Awww thanks, Mint."
    player "Good night, Mint."
    hide mint

    scene black with eyeclose

    call save_reminder from _call_save_reminder_4

    # a new day, player studies in the morning, and hangs out with Annika at night
    $ calendar.next()
    scene black
    scene bg bedroom with eyeopen

    show smartphone at truecenter
    play sound 'audio/sfx/alarm.wav'
    pause 1.0
    hide smartphone

    show mint
    mint "Meow~"
    player relieved "Yawwwwwn... Good morning to you too, Mint."
    player smile "Okay, let's grab a quick breakfast and jump into studying."
    hide mint

    scene bg kitchen with blinds
    player happy "Morning, Mom. Morning, Dad."
    dad "Morning, pumpkin."
    mom "Morning, honey. Did you sleep well?"
    player laugh "Yep. I'm recharged for a new day."
    dad "Good! Working yourself too hard without rest is how you get diminishing returns."
    mom "Why don't you join us for breakfast? Tell us a bit about what you've been learning."

    show toast at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Yum yum."
    hide toast

    scene bg bedroom with blinds

    player smile "Okay. Breakfast's done. Let's get to work."
    player "Hopefully I can get more questions correct today."

    call study_session_choose_topic from _call_study_session_choose_topic_3
    call study_session from _call_study_session_2

    scene bg bedroom with dissolve

    player happy "Alright! That's about it for the morning. I feel like I'm much more productive if I can focus on one thing for an entire day."    
    player "Let's alternate between working whole-day shifts and spending whole days studying."
    player "I can call Annika this afternoon when she's done with her work. It'll be good to chat and ask her about things."

    scene bg bedroom with fadehold

    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0
    hide smartphone

    show annika
    pause 1.0
    player smile "Hey Annika! Is now a good time to talk?"

    show annika laugh
    annika "Heya [player_name]! Now's perfect. I just got back from work."
    annika "How did your first day of studying go?"
    player "I felt pretty productive today. It's nice how the quiz questions give you instant feedback."
    player happy "What about your day? How was work?"
    annika "It went well! I'm learning to use the custom web dev framework that my company uses."
    annika "It's pretty different from what I've been using in my own projects, and a little confusing at times, but my colleagues say it gets better with practice."
    player "That sounds like fun!"

    show annika
    annika "Yeah! And I've heard good things about this framework. Mostly from people I ran into at the local Hacker Space."
    annika "It looks like a popular tool for people who want to test out project ideas at hackathons."
    player neutral "({b}Hackathons{/b}! That reminds me, I should probably ask Annika about this topic.)"
    player "(And she also just mentioned something called a {b}Hacker Space{/b}. That's something worth asking about as well.)"

    show annika laugh
    annika "Hello? Earth to [player_name]?"
    player happy "Haha no worries I'm here. Just wondering about something."

    show annika
    annika "What is it?"

    # booleans mark whether a choice has been visited
    default stage6_annika_questions_visited = set()

    menu stage6_annika_questions:
        set stage6_annika_questions_visited

        "What topic to ask Annika about?"

        "Hackathon":
            call ask_hackathon from _call_ask_hackathon
            jump stage6_annika_questions

        "Hacker Space":
            player "What is this Hacker Space you were talking about?"
            annika "It's just a casual meetup place for people interested in tech."
            annika "I highly recommend checking it out if you have time!"
            player worry "Hmmm..."
            annika @ laugh "Haha don't worry. I know what you must be thinking. A Hacker Space isn't for the cyber criminal type of hackers."
            annika "It's a chill space for people to gather, work, and build cool projects."
            annika "You know what? At the Hacker Space, you might actually find someone like you who's also learning to code. You can totally become study buddies!"
            player smile "That sounds nice. I'll go there sometime."
            annika "Yay! We should go together."

            jump stage6_annika_questions

        "That's everything I need to know":
            jump stage6_after_annika_questions

label stage6_after_annika_questions:
    player laugh "That's all I want to know. Thanks so much for answering my questions!"
    annika @ laugh "Any time! You'll become a pro with these tech culture terms in no time."
    annika "Welp, I guess you must be tired after a day's studying. Enjoy a relaxing evening!"
    player happy "Haha thanks Annika. You as well. Have a good night and a great day at work tomorrow!"

    hide annika
    play sound 'audio/sfx/phone_hangup.wav'

    player smile "Whew. That's a lot of knowledge to unpack."
    dad "Dinner's ready, [player_name]!"
    player surprised "(Wow. Dad is cooking tonight? He cooks maybe once or twice a month, but when he cooks, it's usually really good.)"
    player laugh "Coming!"

    # dinner scene
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    $ show_random_dinner_image()
    mom "Hey honey, how do you like working as a barista? You don't have to go if it distracts too much from your studies, you know."
    dad "Your mom's right. We are here to support you if you ever need us."
    player smile "Thanks folks, but no worries. I can use an occasional break from studying."
    player "Plus, a lot of tech people visit the cafe and they talk about a loads of cool stuff."
    player "Like I heard people talking about a type of event called a hackathon the other day, and I had the chance to ask Annika about it today."
    dad "That's great to hear, pumpkin. What's Annika been up to? You two were really close at college, weren't you?"
    player happy "You won't believe it! She didn't major in CS but now she has this cool tech job..."
    player "... And she taught herself everything..."
    with vpunch
    player laugh "... I'm gonna work hard just like she did!"
    dad "That's the spirit!"
    scene bg kitchen night with fadehold

    scene bg bedroom with blinds
    player pout "Yawwwwwn... What a day. My brain certainly enjoyed a great workout today."
    player "I can barely keep my eyes open. Let's call it a day."
    player smile "Good night, Mint."
    show mint
    mint "Meow~"
    hide mint

    scene black with eyeclose

    call save_reminder from _call_save_reminder_5

    # two days of activity of the player's choosing
    call day_start from _call_day_start
    call day_activity_choices from _call_day_activity_choices

    call day_start from _call_day_start_1
    call day_activity_choices from _call_day_activity_choices_1

    call save_reminder from _call_save_reminder_6

    # hacker space story
    $ calendar.next()
    scene black
    scene bg bedroom with eyeopen

    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0
    hide smartphone

    pause 1.0
    annika @ laugh "Morning, sleepy head!"
    player relieved "Man, you are up {i}early{/i}."
    player "I only see you this excited on half-off pastry days at the donut shack."
    annika "I {i}am{/i} a donut fiend. What can I say?"
    annika "But we're not up for donuts today! I told you we are going to check out the Hacker Space together, remember?"
    annika "You ready for the ride?"
    player laugh "Yes! Lead the way."

    scene bg hacker_space with blinds
    play sound 'audio/sfx/office_ambient.wav'

    show annika
    annika @ laugh "Here we are!"
    player surprised "Wow. This place is huge. Nice and modern."
    annika "Yeah! That's why local hackers love to hang out here."
    annika "Why don't we go around and check out what people are working on?"
    player laugh "Sounds good!"

    scene bg hacker_space with fade
    show boy red
    college_boy "So I was reading this research paper and it occurs to me that we might be able to implement this idea in code..."

    scene bg hacker_space with fade
    show girl purple flipped at left
    show boy orange at right
    girl "The last hackathon was fun!"
    boy "It was! I feel like we might be able to grow our prototype into something even better."
    girl "Yeah for sure - tell me what you're thinking."
    boy "Okay, here's the plan..."

    scene bg hacker_space with fade
    show girl red flipped at left
    show woman blue at right
    college_girl "I had an interview the other day and it was kinda scary..."
    college_girl "They asked me to write code on the whiteboard and then eyeball-test it without a compiler..."
    female "Don't worry! I'm sure you did well!"
    college_girl "..."
    female "I've worked in recruiting, so I'll let you in on some interviewer secrets..."

    scene bg hacker_space dusk with fadehold
    show annika
    annika "What do you think about this place, [player_name]?"
    player laugh "It's amazing!"
    player "This place is alive with energy... It's like you can't take a step without seeing something interesting."
    annika @ laugh "That's the spirit!"
    annika "Do you think you'll come here now and then?"
    player happy "Definitely!"
    player "Thanks for taking me here!"
    annika "Any time!"

    $ add_achievement(plot_hackerspace_discover)

    scene bg bedroom with blinds
    player smile "Wow. I'm amazed. Hacker Space sure is a cool place. I'll have to check it out on my own someday."
    player "Now let's call it a day and get some rest."

    $ has_visited_hacker_space_with_annika = True

    call save_reminder from _call_save_reminder_7

    # two days of activity of the player's choosing
    call day_start from _call_day_start_2
    call day_activity_choices from _call_day_activity_choices_2

    call day_start from _call_day_start_3
    call day_activity_choices from _call_day_activity_choices_3

    call save_reminder from _call_save_reminder_8

    # two days of activity of the player's choosing
    call day_start from _call_day_start_9
    call day_activity_choices from _call_day_activity_choices_12

    call day_start from _call_day_start_11
    call day_activity_choices from _call_day_activity_choices_13

    call save_reminder from _call_save_reminder_20

    $ calendar.next_week()
    scene bg bedroom with dissolve
    player smile "Now that I've been learning to code for some time, not only have I been making progress on the curriculum and visiting Hacker Space, but I've also been engaging with the [freeCodeCamp] community online."
    player "I found this person who taught himself to code from scratch with [freeCodeCamp]."
    player "That's truly a from-zero-to-hero story."
    player "He is now a senior software engineer and has decided to give back to the community."
    player happy "He said I can ask him anything so let's give it a shot."    

label stage7:
    # Stage 7. Marco
    call screen text_over_black_bg_screen(_('{i}Prologue: Chapter 5 - Oh mentor, my mentor!{/i}'))

    $ has_met_marco = True # unlocks Marco's topics_to_ask

    scene bg desk with blinds
    show marco laugh
    marco "Hi [player_name]. I'm Marco. I'm a senior engineer at {b}QuicheQubit{/b}."
    player smile "Hi Marco. Nice to meet you! I'm [player_name], a recent grad and developer wannabe."
    marco "That sounds good."

    show marco neutral
    marco "Why don't I start by telling you a bit about myself? Then ask whatever you want to know about me, my job, or tech in general."
    player "Sounds good."

    show marco laugh
    marco "It's a long story and a bumpy ride. So buckle up."

    show marco neutral
    marco "I graduated from college about ten years ago. I majored in music so I worked as a freelance audio engineer straight out of college."
    marco "Freelancing gave me some freedom and flexibility at first, but I soon discovered that my skills weren't honed enough to attract large, established clients."
    show marco serious
    marco "And working with small, less established clients doesn't pay well and puts a lot of stress on a newbie freelancer."
    player worry "(That's so true... That's how I feel about my tutoring gig...)"
    marco "So I decided to upgrade my skills and try something new."
    marco "I learned to design websites and got a job doing that at a small local company."
    player surprised "(Now that's a nice turn of the story!)"
    show marco neutral
    marco "You know, in small companies, everyone does a little bit of everything."
    marco "I was hired for my web design skills, but occasionally I would be asked to write some HTML, CSS, and JavaScript to showcase the design in action, not just on paper."
    marco "I picked up a little HTML, CSS, and JavaScript in those years and found them to be quite interesting."
    marco "I then found out that there is a term for these skills – front-end development."
    marco "I thought, cool, I've done some front-end development, maybe I can become a full-time front-end developer."
    marco "I started researching and teaching myself front-end dev. The Internet in my days didn't have nearly as many resources as today. So I had to be extremely self-sufficient and develop my own learning path."
    player "(Working out an entire learning path sounds really intense to me, but for some reason Marco made it sound easy...)"
    marco "It all paid off when I got my front-end development job at my current company. I've been with the company since. Nice culture, smart people, interesting work."
    show marco laugh
    marco "Even better, my job constantly challenges me to learn new skills and grow."
    marco "Just a year into my role, I found out that my team needed a mobile developer."
    marco "I thought mobile is really fun, so I talked to my manager and was able to take some paid time off work to learn about mobile development."
    marco "And after a few pet projects, I switched over to mobile development. So here I am, a mobile developer."
    player laugh "Wow! That's awesome!"
    show marco neutral
    marco "Yeah, I know. Looking back it's like a blur."
    marco "So that's my story. Anything you'd like to learn more about?"
    player smile "(Now it's my chance to ask questions!)"

    # initialize all choices to False
    default marco_story_choices = set()
    menu marco_story_choices:
        set marco_story_choices
        "What are you up to nowadays?":
            player "What are you up to nowadays?"
            marco 'You want a one-word answer? Learning. Everyone I know would probably give you the same answer if you asked.'
            marco 'There should never be a point that you want to stop!'
            jump marco_story_choices

        "Do you still have much to learn as a senior engineer?":
            player "Do you still have much to learn as a senior engineer?"
            marco "Of course! I still run into technologies and tools that I don't know in my day-to-day work."
            jump marco_story_choices

        "What is your experience working with people who have a CS degree versus those who don't?":
            player "What is your experience working with people who have a CS degree versus those who don't?"
            marco "I'd say it's not too different. A CS degree may give you a head start in your first year as a junior developer, but after then, it is up to you to learn, grow, and adapt continuously to new technology."
            jump marco_story_choices

        "Do you have a favorite side project?":
            player "Do you have a favorite side project?"
            marco "There is one I'm working on right now. Top secret. You will know it when you see it."
            marco "Like I said, I majored in design and music in college. Those are two things that get me up in the morning."
            marco "Now that I've also learned to code, I think it's the perfect time to put my passion to work and create something awesome, like a video game. I get to do the art, music, and coding all by myself."
            player "That sure sounds like fun! I'd love to see it one day!"
            jump marco_story_choices

        "I'm done asking!":
            player laugh "I'm done asking! That's all I want to know. Thanks so much for sharing!"
            show marco laugh
            marco "Any time, [player_name]. Have fun coding and keep me updated on your progress!"

    scene bg bedroom with blinds
    player smile "Marco was certainly a cool guy. I'm so lucky to have him as my mentor."
    player "Now if I have questions about anything, I can either talk to Annika or Marco."
    show mint
    player laugh "Awww Mint, are you proud of me for making friends in the tech bubble?"
    mint "Meow!"
    player "Haha, good night, Mint."
    hide mint

    scene black with eyeclose

    call save_reminder from _call_save_reminder_9

    $ num_three_day_sessions = 0
    while num_three_day_sessions < 3:
        $ num_three_day_sessions += 1
        # three days of activity of the player's choosing
        call day_start from _call_day_start_4
        call day_activity_choices from _call_day_activity_choices_4

        call day_start from _call_day_start_5
        call day_activity_choices from _call_day_activity_choices_5

        call day_start from _call_day_start_12
        call day_activity_choices from _call_day_activity_choices_14

        call save_reminder from _call_save_reminder_10

    $ calendar.next_month()
    $ renpy.show_screen(PLAYER_PHONE_SCREEN, _layer='transient')
    scene bg bedroom with fadehold
    player smile "It's been almost two months since I started learning to code. Time really flies."
    player "I feel like I'm so much more knowledgeable than when I started."

    window hide
    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0
    hide smartphone

    show annika
    pause 1.0
    annika "Hey [player_name]! Are you free today?"
    player smile "Hey Annika. Yep, I'm down to hang out. What's up?"

    annika @ laugh "Guess what? It's almost {bt}Hacktober{/bt}. The Hacker Space is holding a special hackathon for high school students."

    show annika
    annika "They could use some volunteers to help out."
    annika "Wanna come with me to check it out today?"
    player @ laugh "Sounds good! See you in a bit!"

    scene bg hacker_space with blinds
    play sound 'audio/sfx/office_ambient.wav'
    player surprised "It's even more crowded than usual..."
    annika @ laugh "Looks like high school kids are all hyped up for the event!"

    scene bg hacker_space with blinds
    show boy blue flipped at left with moveinleft
    show girl red at right with moveinright
    boy "Now it's finally time for us to give shape to this awesome idea!"
    girl "Yeah yeah, it's been pie in the sky since forever."
    boy "This time we are finally going to code it all up!"
    girl "Hmmm... Yeah... We probably need some advice. I heard they have mentors here to guide us..."

    $ has_met_layla = True
    show layla with moveinleft
    layla @ laugh "Hey everyone! I heard that you're looking for some help from mentors."
    layla "I'm Layla, one of today's mentors. I'd be glad to work with you."
    boy "Cool! Thanks!"
    girl "Now I really feel like this is going to come together well!"

    scene bg hacker_space with blinds
    show annika with moveinright
    annika "Did you see that woman over there mentoring the high school kids?"
    annika "She looks like she has tons of experience."
    player surprised "And energy! It took a lot to get me to pay attention in high school."
    annika "Me too! Mentoring kids looks like fun. I hope one day I get to do that."
    player smile "Yay! Pass on the torch and give back. I feel like this is a culture thing in tech already."
    annika @ laugh "Haha now you are talking like you've been in tech forever. Not a bad thing since you've only been learning to code for two months."
    annika "You've certainly internalized a lot of the tech culture and values."
    player "Those trips to Hacker Space definitely helped. All thanks to you and my online mentor, Marco."
    annika "Yeah, that reminds me, how's things going with Marco? Are you still regularly checking in?"
    player "Yep. Lately we've been talking about coding interviews. He said I could start applying to jobs once I'm comfortable with my skill level."
    player "Oh and I meant to ask, what was your interview experience like?"
    annika @ laugh "Haha that's a long story. Let's go grab some coffee first"

    scene bg hacker_space_cafe with fadehold

    show annika serious
    annika "Okay, so here's my experience with interviewing."
    annika "I polished my résumé and applied to as many online positions as I could."
    annika "I also had to highlight parts of my résumé that were specific to the requirements of the jobs I was applying to."
    annika "Then it was a long wait, so during that time I practiced coding up interview questions on a white board."
    player surprised "A whiteboard?"
    annika @ neutral "Yeah, I almost forgot to mention that. You might think tech companies use super fancy tools to screen candidates, right?"
    annika "It turns out that a lot of tech companies actually want to test your ability to write code without any assistance."
    annika "Like without code search, documentation, or support from your IDEs."
    player "Huh?"
    menu:    
        "Wait, what even is an IDE?":
            annika "It's short for Integrated Development Environment. You know, like PyCharm for Python, IntelliJ for Java, etc."
            player smile "Okay, got it."
    
        "Hmmm... Interesting":
            pass
    annika @ neutral "Coding on a whiteboard means that you have to be familiar with the syntax, but don't worry, the company will usually allow you to choose a programming language you're comfortable with."
    annika "What's more tricky about coding on a whiteboard is that you might need to come up with test cases yourself, walk through the execution line-by-line, and validate your results."
    annika "If there is a bug in your code, you need to be able to debug on the whiteboard as well, without the convenience of IDE debuggers."
    player worry "(That sounds intense...)"
    annika @ laugh "Haha don't be scared. That's basically the scariest part about coding interviews. Nothing scarier than that!"
    annika "There's no shortcut to coding interview prep though, I'd say. I know it's cliché but I'll leave you with the phrase, practice makes perfect."
    player neutral "Hmmm... I see."

    show annika
    annika "Any more questions about coding interviews?"

    # booleans mark whether a choice has been visited
    default stage7_coding_interview_questions_visited = set()
    menu stage7_coding_interview_questions:
        set stage7_coding_interview_questions_visited

        "Any more questions about coding interviews?"
    
        "What's the entire interview pipeline like?":
            annika "It depends. A company might have multiple rounds of interviews and different recruitment processes."
            annika "Their interview pipeline might start with an online assessment, usually called an OA."
            annika "This is just like an online IDE where you'll solve the problems they give you."
            annika "If you manage to solve the problems and perform well on the online assessment, you might get an update from the recruiter about moving forward to a phone screen."
            annika "This could either be an information session, a behavior interview with the recruiter or an engineer, or a technical interview with an engineer."
            annika "If you perform well, you'll move on to the next steps. Usually, a company will give out more than one round of technical interviews over the phone."
            annika "And finally, once you manage to pull through these phone screens, the ultimate challenge would be an onsite interview."
            annika "Usually you will interview for an entire day onsite, with engineers and engineering managers."
            annika "Onsite interviews might sound daunting, but it's actually a good way for you to learn about the company's culture and the engineer's day-to-day."
            annika "That's about it for the pipeline."
            jump stage7_coding_interview_questions
    
        "What happens after an interview?":
            annika "Usually, you can expect to hear back from the recruiter in a few days."
            annika "It's best to just wait and not rush to email the recruiter for results if you don't hear back immediately. But there is an exception."
            annika "If you need an immediate response because of pending offers or other concurrent interviews, feel free to reach out to the recruiter."
            annika "That's what happened to me. I had an offer with another company but was still in the interview pipeline with my current one, so I reached out to ask them to expedite the proces. And here I am, at my dream company!"
            jump stage7_coding_interview_questions

        "I'm done asking!":
            pass

    player smile "Thanks, that's all I need to know!"
    annika "No problem! Good luck preparing for those interviews!"
    hide annika

    call save_reminder from _call_save_reminder_11

    scene bg bedroom with blinds
    player relieved "I feel like I've learned so much about the coding interview process from Annika today."
    player laugh "So much that I can't wait to wrap up my curriculum and jump in to see what a real coding interview is like!"
    player smile "I heard that [developerquiz] will send an email notification to people who have made significant progress in their curriculum."
    player "Let's check to see my progress."
    if player_stats.player_stats_map[CS_KNOWLEDGE] < cs_knowledge_threshold:
        player "Hmmm... I think I still need to ramp up more on my CS knowledge. I'll get back to studying tomorrow."
        "(Try bumping your {b}CS Knowledge{/b} to above [cs_knowledge_threshold] by completing more quizzes.)"

    while player_stats.player_stats_map[CS_KNOWLEDGE] < cs_knowledge_threshold:
        call day_start from _call_day_start_6
        call day_activity_choices from _call_day_activity_choices_6

    call save_reminder from _call_save_reminder_12

    # once we are down here, we should have player_stats.player_stats_map[CS_KNOWLEDGE] >= cs_knowledge_threshold
    player laugh "Looks like I've made quite a bit of progress! I wonder when I can expect to receive that email."
    player "But let's first have a movie night to celebrate what I've gotten done!"

    scene bg bedroom with fadehold
    $ renpy.show_screen(PLAYER_PHONE_SCREEN, _layer='transient')

label stage7_complete_curriculum:
    play sound 'audio/sfx/social_media_notification.wav'
    player surprised "Hmm... A notification from my phone? This early in the morning?"
    player "It says {bt}Congratulations!{/bt}...?"
    $ has_completed_curriculum = True

    $ completed_curriculum_date = date(calendar.year, calendar.month, calendar.day)
    $ days_between_start_and_curriculum_completion = (completed_curriculum_date - start_date).days

    $ add_achievement(
        achievement_name=milestone_complete_curriculum,
        title=_("{bt}Congratulations!{/bt}"),
        message=_("You completed the coding curriculum in {b}{color=#002ead}[days_between_start_and_curriculum_completion]{/color}{/b} days.\nNow you are ready to rock your coding interviews and realize your dream of becoming a software engineer.\n Feel free to share your progress with the world!"),
        ok_text=_("Let's crush those interviews!"),
        show_achievements_count=False
        )

    player laugh "This is great! Let's check the curriculum off my To-Do list."
    $ todo_list.complete_todo(todo_learn_cs)
    player smile "(Let's also make it a To-Do item to start preparing for coding interviews.)"
    $ todo_list.add_todo(todo_interview_prep)
    player happy "(And to start applying to jobs as well!)"
    $ todo_list.add_todo(todo_apply_to_jobs)
    player laugh "I'm feeling great about my decision to learn to code!"
    player "Let's crush the interviews!"

label stage8:
    # Stage 8. Coding interviews
    call screen text_over_black_bg_screen(_("{i}Prologue: Chapter 6 - Let's crush those interviews!{/i}"))

    scene bg bedroom with fadehold
    player smile "Alright! Let's start by applying to jobs!"
    call day_activity_job_search from _call_day_activity_job_search
    player "Now that I've applied to my first job, I can check it off my To-Do list."
    $ todo_list.complete_todo(todo_apply_to_jobs)

    player "What's next on my To-Do? Oh right, let's start preparing for coding interviews."
    # now change the day activity text for studying
    $ day_activity_study = todo_interview_prep
    player surprised "What should I study? I remember some skills mentioned in the job posting included JavaScript, Web Dev, Algorithms, and System Design."

    call study_session_choose_topic from _call_study_session_choose_topic
    call study_session from _call_study_session_3

    $ add_achievement(milestone_start_interview_prep)

    scene bg bedroom with fadehold
    player relieved "Whew... Those questions are harder than CS fundamental questions. Guess I need to put in more studying."
    player smile "But this is still a good start!"
    $ todo_list.complete_todo(todo_interview_prep)
    player "Now the next big thing on my To-Do list will be to actually pass an interview and get a job."
    $ todo_list.add_todo(todo_get_job)

    player "Let's relax for a bit and see if anyone has messaged me while I was away."
    # chat with Marco
    play sound 'audio/sfx/social_media_notification.wav'
    show smartphone at truecenter
    player surprised "Huh. A message from Marco."
    hide smartphone
    show marco
    marco "Heya [player_name]! Was it a busy day?"
    player happy "Hey Marco! Yeah. I just started preparing for interviews and applying to jobs."
    marco @ laugh "That's a good start!"
    marco @ serious "But yeah, companies are usually slow to process the applications. You might need to wait for a week or more to hear back."
    marco "So don't get discouraged if you don't hear back for a while!"
    marco "Keep on applying to jobs, prepping for interviews, and going about your routines."
    marco @ laugh "Once they have processed your application and gotten the interview process rolling, it's your time to shine!"
    player laugh "Haha thanks! I'll keep that in mind."
    player "Have a great rest of your evening!"
    marco "You too."

    play sound 'audio/sfx/phone_hangup.wav'
    hide marco

    player relieved "Yawwwwwn... Let's call it a day and get back to my routine tomorrow."

    scene black with eyeclose

    call save_reminder from _call_save_reminder_13

    call day_start from _call_day_start_8
    call day_activity_choices from _call_day_activity_choices_8
    $ calendar.next_week()

    # loop routine
    # TODO: refactor past demo if we need offer negotiation
    while offer_company_name is None:
        while interview_company_name is None:
            # two free-to-play days in a row
            call day_start from _call_day_start_7
            call day_activity_choices from _call_day_activity_choices_7
            $ calendar.next_week()
            scene black with dissolve
            "(Does it feel like time is flying by without you doing much?)"
            "(Well, this is the reality of navigating the stress of applying to jobs, waiting for application follow-up, going to interviews, waiting for interview follow-up, and {b}Repeat{/b}.)"
            "(Hang in there, alright?)"

            if interview_company_name is None:
                # go back to job search
                scene bg bedroom with fadehold
                player "Let's search for some job postings today."
                player surprised "Looks like there's a new job posting available. Let's check it out."
                call day_activity_job_search from _call_day_activity_job_search_1

                if num_jobs_applied == 1 and not milestone_first_application in persistent.achievements:
                    $ add_achievement(milestone_first_application)

                call day_activity_choices from _call_day_activity_choices_9

        # receives an email
        scene bg bedroom with fadehold
        show smartphone at truecenter
        play sound 'audio/sfx/alarm.wav'
        pause 3.0
        hide smartphone
        play sound 'audio/sfx/social_media_notification.wav'

        player surprised "Huh, an email from {b}[interview_company_name]{/b} first thing in the morning? Right, it's been a while since I applied to their job posting."
        player "The title says 'Application Follow-up'..."
        $ num_jobs_interviewed += 1

        if num_jobs_interviewed == 1 and not milestone_first_interview in persistent.achievements:
            $ add_achievement(milestone_first_interview)

        call screen company_interview_email_screen(interview_company_name)
        player laugh "I made it! I'm going to a coding interview!"
        player "I'm gonna share this with Annika and Marco."
        play sound 'audio/sfx/smartphone_typing.wav'
        player "Alright! Building on this momentum, let's kick start this awesome day!"
        call day_activity_choices from _call_day_activity_choices_10

        # here interview_company_name is not None
        call day_activity_interview from _call_day_activity_interview
        call day_end_interview from _call_day_end_interview

        call day_start from _call_day_start_10
        call day_activity_choices from _call_day_activity_choices_11
        $ calendar.next_week()

        if offer_company_name is None:
            scene bg bedroom with fadehold
            $ num_jobs_rejected += 1
            play sound 'audio/sfx/social_media_notification.wav'
            player surprised "Huh, an email from {b}[interview_company_name]{/b}? Right, it's been a week since my interview with them."
            player "The title says 'Interview Follow-up'..."
            player worry "The last thing I need in my inbox is a rejection letter first thing in the morning..."
            player pout "But I have to face it."
            call screen company_rejection_email_screen(interview_company_name)
            player worry "Well... Guess I need to work harder."
            "(Hey you there, don't look so down, okay? Coding interviews are hard and we know it. That's why you should study for them. Why not try out some more mock questions during your study sessions?)"
            show mint
            mint "Meow..."
            player relieved "Thanks, Mint. I'm a bit disappointed, but I'll be fine."
            hide mint
            player smile "It's no use crying over spilled milk. Let's get some rest today and get on with my routines tomorrow."

            if num_jobs_rejected == 1 and not plot_rejection in persistent.achievements:
                $ add_achievement(plot_rejection)

            elif num_jobs_rejected == 3 and not plot_third_rejection in persistent.achievements:
                $ add_achievement(plot_third_rejection)

        # reset interview_company_name to None so we enter the inner loop again
        $ interview_company_name = None

    # once we break out of this loop, show the offer screen
    play sound 'audio/sfx/social_media_notification.wav'
    player surprised "Huh, an email from {b}[offer_company_name]{/b}? Right, it's been a week since my interview with them."
    player "The title says 'Interview Follow-up'..."
    player worry "The last thing I need in my inbox is a rejection letter first thing in the morning..."
    player "But who knows? It could be a request for follow-up interviews, or even better!"
    player relieved "(Deep breath...)"
    player neutral "Okay, I'm ready to take a look."
    call screen company_offer_email_screen(offer_company_name)
    player surprised "Huh? Is this a dream?"

    show mint with vpunch
    play sound 'audio/sfx/punch.wav'
    mint "Meow!"
    player pout "Owww Mint... You are heavy... Don't just pounce on me like that, okay?"
    player surprised "Wait a minute! Mint just crash-landed on me and I felt the impact. This must mean that I'm not dreaming."
    player "So this is real."
    mint "Meow meow!"
    hide mint

    player laugh "Wow. I did it. I'm now a real developer!"
    play sound 'audio/sfx/applause.ogg'
    $ todo_list.complete_todo(todo_get_job)
    player "Can't forget to check that off the To-Do list."
    $ accepted_offer_date = date(calendar.year, calendar.month, calendar.day)
    $ days_between_start_and_offer = (accepted_offer_date - start_date).days
    $ days_between_curriculum_completion_and_offer = (accepted_offer_date - completed_curriculum_date).days

    $ add_achievement(
        achievement_name=milestone_first_offer,
        title=_("{bt}Congratulations!{/bt}"),
        message=_("You taught yourself to become a developer in {b}{color=[dark_blue]}[days_between_start_and_offer]{/color}{/b} days, [days_between_curriculum_completion_and_offer] days after you've completed the coding curriculum.\nYou have applied to [num_jobs_applied] jobs and interviewed for [num_jobs_interviewed] times before landing this offer.\nNow you are ready to rock your new job!\n Feel free to share your progress with the world!"),
        ok_text=_("Let's rock my new job!"),
        show_achievements_count=False
        )

    player happy "I can't wait to tell my parents! And I should call Annika and Marco to let them know."
    player laugh "Let's get everyone together and throw a big party to celebrate!"
    # TODO: congrats from Annika, Marco, and family

    # should be the last save reminder
    call save_reminder from _call_save_reminder_14 

# actually no stages between 8 and 14

label stage14:
    # Stage 14. New hire player meets Layla
    call screen text_over_black_bg_screen(_("{i}Prologue: Chapter 7 - Let's meet my new colleagues!{/i}"))

    $ calendar.next_month() # player's start date is in a month

    scene bg office
    player surprised "Wow. I still can't believe that starting today, I'll be working in such a fancy office."
    player smile "My orientation email says that my onboarding buddy will be here to pick me up and show me around the office..."
    show layla

    layla "Hey [player_name]. Welcome to the team! I'm Layla, your onboarding buddy."
    layla @ laugh "Feel free to ask me anything!"
    player surprised "(Hmmm... I wonder if we have met before. Layla looks familiar somehow.)"
    player "(...Oh! Was that her at Hacker Space mentoring the kids?)"
    player "(If I remembered correctly...)"
    # TODO: flashback sepia fade
    scene bg hacker_space with fadehold
    show layla
    layla @ laugh "So how's everyone's project going? We mentors are here to answer any questions you have!"

    scene bg office with fade
    show layla with vpunch
    layla "[player_name]? Are you okay? You are spacing out."
    player smile "Ah! I'm fine. I just remembered that we might have met before."
    player "You know, at Hacker Space. I used to go there to study and work on projects before I got this job."
    layla "Oh, wow. Yeah. I was at a few of those Hacker Space events. Nice to hear that you enjoyed the place!"
    layla @ laugh "Alright, enough small talk! Are you ready to commit your first line of code into production today?"
    player surprised "(Uhhhh that's fast...)"
    player happy "Ahhh... Yes, I'd love to dive into the code base as soon as possible!"
    layla "Way to go! Our team usually sits around that table, next to the whiteboard."
    player "Gotcha! I'll get started right now!"
    play sound 'audio/sfx/keyboard_typing.wav'

    $ add_achievement(milestone_onboarding)

    scene bg office with fadehold
    show layla
    layla "So how's work going? Have you worked your way through our code base already?"
    player pout "... Um..."
    layla "Something on your mind?"
    player "I'm kind of stuck... Or, I guess a more accurate way to put this is, I don't even know where to start."
    layla "No worries! Onboarding can be daunting."
    layla "Think about it. Teams of talented developers spent months, even years, building out this code base."
    player smile "Haha, thanks. That does make me feel better."
    layla @ laugh "How about this? Let's take your mind off this code for a while and go grab coffee."
    player happy "Sure, I'd love to!"

    scene bg office_cafe with blinds
    show layla
    layla @ laugh "Here you go. From bean to coffee, freshly brewed in the office."
    player pout "..."
    player neutral "Hey Layla. Mind if I ask how long you've been with this company and team?"
    layla "Sure thing. I've been here for two years. I interned here when I was in college and returned full-time right after graduation."
    player surprised "So you were a CS major?"
    layla "Yep."
    player worry "(No wonder Layla was able to blend in so well...)"

    show layla serious
    layla "Oh please I know that look. 'CS kids must have had it easy breaking into tech.' Right?"
    layla "That's just not the whole story, you know."
    player pout "Oops, sorry."
    layla @ neutral "No big deal. I can see where you are coming from."
    layla "Have you heard of the term imposter syndrome?"
    menu:
        "Do you know what imposter syndrome is?"
        "Yes.":
            player "Yeah. It's the feeling that everyone is better than you and you are an undeserving fraud."
            player worry  "To be honest, I feel that quite often."
        "Nope.":
            player surprised "Care to explain?"
            layla "It's when you feel like everyone else is smarter and more competent than you."
            layla "That you are a fraud, despite all of your education and achievements."
            player worry "Uhhh... I know that feeling..."
            layla "Not the best feeling, huh?"
    layla @ neutral "No worries, you are good. That's almost the norm for people in tech."
    layla "Hah. Would you believe me if I told you that imposter syndrome hits CS students equally hard, if not harder?"
    player surprised "Ummm... Tell me about it."
    layla "It starts the first time we step into a CS classroom, maybe earlier."
    layla "There is always that kid that sits in the front row, who has been coding since five and knows everything the professor has yet to talk about."
    player pout "That's... intense."
    layla "And there's this expectation that CS kids should get big-name internships as early as their freshman year summer."
    layla "Definitely not later than their junior year summer. Otherwise, the myth goes that they are unhirable."
    layla "I spent my freshman and sophomore summers volunteering at a local school teaching kids to code."
    layla "And I mean I didn't see any problem with that. I love coding and I love teaching, and being able to convey that to the next generation is an awesome opportunity for me."
    player smile "(No wonder Layla's volunteering her time to mentor kids at Hacker Space.)"
    layla "But my friends were either interning for big name companies or building their own startups during the summer."
    layla "They were nice enough not to say anything to my face, but I always felt a strange sense of hollowness when I saw them post about their intern perks or startup progress."
    layla "It was a rough time, but my friends and my college advisors were supportive, and I eventually come to terms with being who I am and contributing to causes that I care about."
    player pout "(Awww... I never imagined how hard imposter syndrome hits everyone.)"

    show layla neutral
    layla "Haha sorry for the rant. I don't want to scare you away from continuing working in tech."
    layla "It's just that the battle with imposter syndrome is a continuous battle. Every little win is a win."
    layla "In fact, I still grapple with imposter syndrome and have to stop myself from banging my head on the desk whenever I run into a bug I can't fix."
    player smile "Wow. Haha. Thanks for sharing. That actually makes me feel a lot better."
    layla @ laugh "You are very welcome."
    layla "So, what else would you like to know about me or my role?"

    default layla_story_choices = set()
    menu layla_story_choices:
        set layla_story_choices
        "What was your experience like when you first joined?":
            player "Would you mind telling me about your experience when you first joined this company?"
            layla @ laugh "Sure thing!"
            layla "Like you, I also had an on boarding buddy. He was a few years ahead of me. Very knowledgeable and chill guy."
            layla "At his suggestion, I started with simple bug fixes. Then after a month, I started building small features and getting them approved by the team."
            layla "As I became more familiar with the code base, I had more confidence to take on bigger features."
            layla "And before I knew it, here I am, two years in already."
            player "Wow. Time sure flies."
            layla "It really does. You'll be navigating our code base like a pro before you realize it."
            jump layla_story_choices
        "How was your transition from college to work?":
            player "How was your transition from college to work? Was it any easier because of your CS background?"
            layla "Yes and no. My CS background helps a little in that it gave me a general sense of what to expect in the workplace."
            layla "But there are few college CS curricula that can cover the modern principles and best practices in the world of software."
            layla "Which is not a surprise since the tech world is constantly evolving."
            layla "But that also means that, for the most part, I had to pick up the important things on the job."
            layla "Not a bad experience given that I had a supportive team behind me."
            player @ happy "Awww that's nice!"
            layla @ laugh "Yep. Now that you're the newbie here, the team and I will be here for you."
            jump layla_story_choices
        "What is our team like?":
            player "So what is our team like?"
            layla "Oh, they are out investigating a customer case today, so it's only you and me here in the office."
            layla "But you will meet them soon. They are all nice and smart people."
            layla "You and I included, we have five developers in total, one scrum manager, one product manager, one UX designer. That makes us a team of eight."
            player @ laugh "Sounds cool! Can't wait to meet the team."
            jump layla_story_choices
        "I'm done asking!":
            player @ laugh "I'm done asking! I feel so much better knowing that everyone started from square one."
            layla @ neutral"Hehe, [player_name], you are a fun one. I'm sure you will enjoy your work as a developer."

    layla @ laugh "Are we now ready to go back and squash some bugs?"
    player laugh "Lead the way!"

label v1_ending:
    scene bg office with fadehold
    player relieved "Okay, finally, I think my code is good to go! Let's commit it to the server."
    player neutral "Hmmm... Maybe it's a good idea to double-check?"

    $ check_counter = 2 # start on double-checking, go thru double, triple, quadruple
    menu ending_check_code:
        player "Should I check my code some more?"

        "Let's double-check the code!" if check_counter == 2:
            $ check_counter += 1
            player "..."
            player "Looks good to me."
            player "But maybe I should still triple-check it?"
            jump ending_check_code

        "Let's triple-check the code!" if check_counter == 3:
            $ check_counter += 1
            player "..."
            player "Looks good to me."
            player "But maybe I should still quadruple-check it?"
            jump ending_check_code

        "Let's quadruple-check the code!" if check_counter == 4:
            $ check_counter += 1
            player "..."
            player "Looks good to me."
            player relieved "I've checked it so many times that I've lost count..."

            $ add_achievement(plot_double_check)
            
            player smile "It should be good to go, right?"
            # proceed with plot

        "Looks good to go!":
            player laugh "I'm confident that it's good to go!"
            # proceed with plot

    player "Let's commit it to the server."
    # TODO: system processing animation
    play sound 'audio/sfx/system_processing.wav'
    player neutral "... And nothing happened."
    player worry "Hmm... my changes should at least do something to the code base. Maybe I can check if Layla is in... "

    # stop the music here
    # $ continue_looping_music = False
    stop music fadeout 1.0

    # office red alert animation
    show red_flash    
    play sound 'audio/sfx/error.wav'
    layla "[player_name]? Was that your change a few seconds ago?"
    layla "Oh don't tell me... I think we have some problems here..."
    window hide
    pause 4.0
    hide red_flash with dissolve

    $ add_achievement(
        achievement_name=ending_dev,
        title=_("{color=[red]}{icon=icon-alert-triangle} Attention{/color}"),
        message=_("Hey [player_name]... \nThe thing is, it looks like... \n{sc}{color=[red]}YOU HAVE BROUGHT DOWN THE PRODUCTION SERVER{/color}{/sc}"),
        ok_text=_("Oopsy... Am I... fired?"),
        show_achievements_count=False
        )

    show main_menu_v1 with fadehold
    pause 5.0
    # fall through to the next label
    $ calendar.next_month()

label v2_start:
    call screen text_over_black_bg_screen(_("{i}Arc I{/i}"))

    scene bg laptop_screen with dissolve
    ## setup for the case where the player started in v2 without filling in the info in v1
    if player_name == '':
        $ player_name = renpy.input(_("What is your name? {color=[red]}*{/color} (Type your name and hit Enter. This name will be used throughout the game and you cannot change it unless you start a new game.)"), default=_("Lydia"))
        $ player_name = player_name.strip()
        if player_name in vip_names:
            $ vip_profile_url = vip_names[player_name]
            "[player_name]? What a coincidence! Our VIP team member {a=[vip_profile_url]}[player_name]{/a} will be honored to hear that."
            # TODO: Easter Egg
        # handle empty string case by assigning default name
        if not player_name:
            $ player_name = _("[player_name]")

    $ stats_unlocked = True
    $ todo_unlocked = True
    $ items_unlocked = True
    $ quiz_session_questions = all_quiz_questions
    $ player_stats.subcategory_stats_map = {stats_name: 0 for stats_name in v1_skills}
    ## end v2 setup

    $ player_stats.set_stats(MONEY, 500)
    $ player_stats.set_stats(RENOWN, 20) # start with a bit of renown

    # transition to v2 plot here
    $ calendar.next_weekday()
    $ calendar_enabled = True
    scene bg bedroom with dissolve
    player relieved "A lot has happened in this past month..."
    "(After you broke prod on the first day of work, Layla, the team, and your manager insisted that it was okay, and you didn't have to worry.)"
    "(That being said, they didn't end up renewing your contract.)"
    "(So after applying for a few more jobs, and more long nights of preparation, you landed a new one!)"
    "(You start today as ConsultMe Consulting Company's newest, fulltime, junior full stack engineer!)"

    scene bg company1_reception with fadehold
    play sound 'audio/sfx/office_ambient.wav'
    player surprised "So this is ConsultMe! Wow... It's enormous."
    player smile "I put in the work to become a developer, and today, it's real... "
    player "I'm going to keep working hard and learn everything I can! Doing that is what got me here, so if I keep it up, I should be okay!"    
    player "Um... hello?"
    show maria
    receptionist @ smile "Hello! How can I help you?"
    player "My name is [player_name], and this is my first day."
    receptionist @ laugh "Ah, the new hire! And so punctual too - it's nice to meet you!"
    receptionist smile "My name is Maria, and I'll be showing you around!"
    player "Got it!"

    scene bg company1_center with blinds
    pause 2.0
    scene bg company1_boardroom with blinds
    pause 2.0
    scene bg company1_breakroom with blinds
    pause 2.0
    scene bg company1_dining with blinds

    "You're taken all around the ConsultMe office. There are lots of snacks in the lunch area, and even a gym downstairs!"
    "There are dozens and dozens of meeting rooms, all named after different countries around the world."
    "There's even a nursing room for new mothers!"

    scene bg company1_lydia_cubicle
    show maria
    maria smile "... And this is your cubicle! We even prepared your name plate!"
    player surprised "Wow... it's made of wood! This is so nice."
    maria laugh "I'm glad you like it! Do you have any questions so far? I know I've been hitting you with a lot of information."
    player smile "No no, everything has been awesome so far!"
    maria "Great! The last leg of our tour involves me handing you off to our engineering manager, Iris!"

    scene bg company1_center with blinds
    show maria at left with moveinleft
    show iris with moveinright
    iris "Hello. And who is this again?"
    maria @ smile "Iris, don't be silly! This is [player_name]! The new hire?"
    iris disgust "Hm... I see."
    player worry sweat "(Jeez... this lady is... scary.)"
    player worry "(I've been in the workforce for a few years now, and yet, this woman makes me feel like a highschool kid who doesn't know what she's doing.)"
    player "Um... hi. My name is... um... [player_name]..."
    iris confused '"Um[player_name]"? What a strange name.'
    player "Um... no, it's -"
    iris "Maria, please introduce... Um[player_name] to Goro. He can get her set up."
    iris "If you'll excuse me. I don't have much time for pleasantries."
    hide iris   
    player "... "
    player -sweat "Ooookay. So. Who's Goro?"
    show goro at right with moveinright
    goro @ smile "That'd be me."
    player surprised "Oh! Hello!"
    goro disgust "Don't mind Iris. She's... prickly on the outside. But she can be really nice once you get to know her."
    player smile "Sure... I'm [player_name]. It's nice to meet you!"
    goro smile "Awesome to meet you, [player_name]! I'm Goro - I'll be your team lead for any projects moving forward."
    goro laugh "I've been around the bend a few times, and I'm a little {i}less prickly{/i} than Iris. So feel free to ask me any questions that you might have."
    player smile "Thanks! I appreciate it."
    goro smile "We've also got the rest of the team to meet too. First there's Mala, and she's probably somewhere around - "
    show mala at center with moveinleft
    mala laugh "I heard my name! What's up old man?"
    goro angry "That's no way to greet our new hire!"
    goro smile "[player_name], this is Mala. Mala, this is our new hire, [player_name]."
    mala smile "Oooh! A freshman! We haven't gotten a new fish in ages!" # Ed: I'm not sure if freshman is the right way to describe a new hire. I've only heard it used for high school and college students.
    player smile sweat "F-fish?"
    mala laugh "Yeah! Hello? You're a freshman! A little fish out of water."
    player laugh -sweat "I wasn't even called a fish in college!"
    goro smile "Don't freak her out, Mala."
    goro "Mala's a big ball of energy. She's a great resource if you need any help."
    player "Gotcha. Thanks for helping me out!"
    mala smile "No problem!"
    mala smile "I've gotta run - but I'll see you two in stand-up, right Goro?"
    goro smile "You know it. See you later, Mala."
    maria laugh "You guys are always good for a laugh! I've gotta go, too."
    maria "I'll be around if you ever have any questions, or just want to grab some lunch, okay [player_name]?"
    maria smile "I'll leave you all to it - have a nice day!"
    player smile "Thanks Maria - see you around!"
    hide maria at right with moveoutright
    hide mala at left with moveoutleft
    player neutral "(Hm... stand-up? I've never heard that term before.)"
    goro "Well that was good timing. But you still haven't met - "
    show darius at left with moveinleft
    darius "Goro! Oliver bet that Mala could get more JIRA tickets done than I could!"
    darius "Can you {i}believe{/i} that man?"
    show oliver at center with moveinright
    oliver "It's nothing personal, mate - I just know who I can count on to get our KPIs met, is all."
    darius "Mhm. Don't come crying back to me when we hit Q4, you have deadlines, and everyone else is on vacation."
    player pout "(Aw man... what are these guys even talking about?)"
    player "(KPIs... Q4... JIRA... what the heck are they {i}talking{/i} about?"
    goro angry "Between you two and Mala, [player_name] is going to think we run a barn instead of a dev shop!"
    goro smile "[player_name], this is Darius and Oliver."
    goro "Oliver here is our product owner - that basically means that he's in charge of running our project,"
    goro "making sure that we hit our deadlines, and discussing requirements for our projects so the customers are happy."
    oliver smile "It's a pleasure to meet you. I'm sure you'll do great here!"
    oliver laugh "You're even newer than Darius, and I bet you'll {i}still{/i} get more tickets done than him."
    darius smile "You think you're funny now, but when I bring pound cake to the office again, you can't have any."
    goro smile "Darius here is a junior - just like you!"
    darius "What's goin' on [player_name]? It's nice to have a fresh face around the office!"
    darius laugh "Being a junior will be way more fun when there's more than one of us!"
    darius "I've only got a year of experience myself, but I know my way around here."
    darius "So feel free to ask me if you need any help!"
    player smile "Thanks!"
    player "(Wow... I don't know exactly what I was expecting, but everyone here is so nice!)"
    player "(I'm happy to be a part of what seems to be like such a nice team, but...)"
    player "(What {i}were{/i} all of those terms they were using earlier?)"
    goro "[player_name]?"
    player smile sweat "O-oh! Sorry - could you repeat what you asked?"
    goro "I was asking if you have any questions for me so far?"
    goro smile "I know that your first day of work can always be a little daunting."
    player surprised "Um..."
    player sweat "Ah..."
    player smile "Nope!"
    goro "You don't?"
    player sweat smile "No! I'm good!"
    goro "Well... okay then! Like I said, I'm here if you need any help."
    player smile -sweat "Thanks!"

    scene bg bedroom with fadehold
    "Later that day..."
    show mint
    mint "Meow!"
    player smile -sweat "Hi Mint! You'll never believe the day I just had. The office was huge!"
    player "I met tons of people, and everyone was really nice."
    player "They even gave me a company laptop and company cellphone! They're both the latest models. Talk about an upgrade!"
    player "..."
    mint "Mew?"
    player worry "Well... It's all super cool, but it's also a little overwhelming. All of the people I met today were nice, but there were so many of them."
    player "How am I supposed to remember all of their names?"
    player "And then I had to spend the rest of the day in meetings. Goro told me that I didn't have to do much but lend an ear, and even that was a lot."
    player "There were a million acronyms that I didn't know... I had no idea what anyone was talking about."
    player "Am I really cut out for this...?"
    mint "...?"
    mint "Meow!"
    player smile "Hm... you're right! I can't give up yet. I worked too hard to get here."
    player "I know! I should give Annika a call. She told me to give her a ring when I finished my first day! Maybe I can ask her some questions?"
    hide mint

    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0
    hide smartphone

    show annika
    pause 1.0
    annika @ laugh "[player_name]! How was your first day, superstar?"
    player smile "Great! Great... but also... like, really overwhelming?"
    annika "That sounds about right! That's about how my first day went, too. What happened?"
    "You explain all of the concerns that you told Mint about."
    annika "Wow, that's definitely a lot! I'm happy to answer any of your questions, though! What do you want to know specifically?"
    player neutral "Well..."

    default first_day_story_choices = set()
    menu first_day_story_choices:
        set first_day_story_choices
        "Ask about acronyms":
            player "So as I said, I had to attend a few meetings today."
            player "It was so mind-boggling because, aside from not knowing what anyone was talking about,"
            player "There were so. Many. Acronyms!"
            player "What is PII? Or ETA? What on earth is PEBCAK?"
            annika laugh "Hehehe... that last one is actually pretty funny."
            player worry "Annika!"
            player pout "This isn't funny at all. I'm freaking out!"
            annika "Sorry, sorry!"
            annika "Things will be okay. The truth is, every industry has their own acronyms. Some companies even have their own acronyms."
            annika "So I could try to tell you what they all are, but I probably won't know them all."
            annika "The good news is, most companies are totally fine with you learning these things as you go!"
            player neutral "Really?"
            annika "Yup! Just make a habit out of asking about them."
            annika "What I do is keep a journal or a note-taking app open, and write down any acronyms I'm not familiar with."
            annika "Then, when we have a bit of free time, I ask my team lead or another developer what each one means."
            annika "Just a few at a time, though. You don't want to approach someone with 10 different acronyms to explain!"
            jump first_day_story_choices

        "Ask about Ruby on Rails":
            player "Okay... so I've always worked with programming languages like Python and JavaScript. But this company uses something called Ruby on Rails."
            player worry "I've never even worked with it before! Sometimes I wonder if I should have even been hired, because I don't know anything about it."
            annika @ neutral "That's totally fine!"
            annika "Ruby on Rails is a framework for the Ruby programming language."
            annika "A framework is more or less a collection of pre-written code that allows you to do things without writing everything from scratch yourself."
            annika "And it's okay that you don't know it! My company uses a Python framework called Django."
            annika "I didn't know Django at all before I came here, but I was given some assignments that helped catch me up to speed."
            annika "Another important thing to remember is that your company knows you don't know Ruby on Rails, right?"
            player neutral "Yeah... I made that very clear during my interviews."
            annika "See? It's not as if you lied to land the job! And let's take a look at your job description too - what does it say?"
            player "Hm..."
            player "Oh! How could I have missed this?"
            player "It says that I'll start off with just frontend work, and slowly be trained to assist with the backend."
            annika "See? That's perfect! Just be sure to spend time studying during and after work to really hone your skills."
            player "I'm... allowed to study?"
            player surprised "At WORK?"
            annika "You sure are! You're in the big leagues now, my friend!"
            annika "You're not just being paid to develop - you're being paid to LEARN now too!"
            annika "Another good thing about your situation is that Ruby on Rails is super well documented. It's been around for 19 years."
            annika "That's ancient by programming standards! So you'll have lots of documentation online that can help you."
            player smile "And... if I get stuck, can I still give you a call now and again?"
            annika @ laugh "Are you kidding? Always! We're accountability buddies, right?"
            jump first_day_story_choices

        "What is JIRA?":
            player "So at work, they kept talking about JIRA... What is that?"
            annika 'Programming assignments are called "tickets".'
            annika "JIRA is just a ticketing management system! It keeps track of who's assigned to what tickets."
            player smile "Oh, I see!"
            player "What does the acronym stand for?"
            annika "Acronym?"
            player "JIRA is usually written in all capital letters. That means it's an acronym, right?"
            annika "No, no - that's just how it's written! The letters don't stand for anything."
            annika @ laugh "Fun Fact The name is actually a shorthand for “Gojira”, which is the Japanese translation of “Godzilla”!"
            player "Whoa, cool! I never would have guessed!"
            annika "You'll be doing tickets every day at work - once you sign in, you can get started immediately!"
            jump first_day_story_choices

        "Ask about getting stuck":
            player "Well, for starters... what if I get stuck? "
            annika "Stuck?"
            player "Sometimes, whenever I'm working on personal projects, I get stuck. That seems to be fine to do on personal projects,"
            player "but this is the real deal! Won't that make me look like I don't know how to do my job?"
            annika @ laugh "Hahaha!"
            annika @ neutral "What do you do when you usually get stuck while you're working on a project?"
            player "Well... I look things up. And I double-check my code."
            player "I also see if I can find any developers that can help online."
            annika "See? You already know what to do!"
            annika "I know your team is all new to you, but you're a junior developer."
            annika "Their job is to help you whenever you're stuck. Not only can you ask them for help, but when you get assigned a task to fix some already existing code, you may even be able to speak to the person that originally wrote it!"
            player "Oh! Is it really that simple...?"
            annika "Yep! The cool part about doing this all professionally is that you're a part of a team now! They expect you to ask as many questions as you need to to get the job done."
            player "Wow - that really does make me feel better!"
            jump first_day_story_choices

        "I think that answers all my questions!":
            player relieved "(Sigh) I feel much, much better!"
            player smile "It looks like you've saved the day again, Annika."
            annika "Any time! Remember, you're a junior developer now - you've got a lot of hard work ahead of you,"
            annika "but you landing this job means that you were CHOSEN!"
            annika "This all seems like a lot, and like things are really overwhelming,"
            annika "but try to remember that your job isn't to learn all of these things in one day."
            annika "Worst case scenario, feel free to talk to your manager for a temperature check!"
            player "A temperature check?"
            annika "Yep! Every so often you can ask about how you're performing. You may even be able to ask for one-on-ones!"
            annika "They're meetings where you chat with your manager, say, once a week, or every other week, or even once a month." # Ed: Are temperature checks and one-on-ones the same thing? If so, we should probably just use one term
            annika "You can talk about your goals as a developer, receive feedback, or just use them as a chance to get to know your manager!"
            player "That actually sounds kind of nice!"
            annika "Don't forget - you're working with people, not a bunch of dragons that want to gobble you up!"
            "You finish up chatting with Annika, and feel a huge weight lifting off of your shoulders."
            "You get ready for bed, wanting to be as well-rested as possible for your first official day of work!"

    hide annika

    $ is_in_v2_arc1 = True
    $ work_session_questions = all_quiz_questions

label v2_days_before_demo:
    $ num_days = 0
    while num_days < 21:
        $ num_days += 1
        call day_start from _call_day_start_13
        call v2_routine from _call_v2_routine

    $ calendar.next_weekday()
    call day_start from _call_day_start_15
    call v2_demo from _call_v2_demo

label v2_days_after_demo:
    $ num_days = 0
    while num_days < 7:
        $ num_days += 1
        call day_start from _call_day_start_14
        call v2_routine from _call_v2_routine_1

    $ calendar.next_weekday()
    call day_start from _call_day_start_17
    call v2_redemption from _call_v2_redemption
    $ add_achievement(milestone_v2_redemption)

    call day_start from _call_day_start_18
    call v2_paying_it_forward_p1 from _call_v2_paying_it_forward_p1

label v2_arc1_devops:
    $ player_stats.subcategory_stats_map[DEVOPS] = 0
    $ quiz_session_questions = devops_questions
    $ num_days = 0
    while num_days < 3:
        $ num_days += 1
        call day_start from _call_day_start_16
        call v2_routine from _call_v2_routine_3

    $ calendar.next_weekday()
    call day_start from _call_day_start_19
    call v2_paying_it_forward_p2 from _call_v2_paying_it_forward_p2
    $ add_achievement(milestone_v2_arc1_complete)
    call screen text_over_black_bg_screen(_("You've reached the end of Arc I. Stay tuned for Arc II!"))

    # start v2 arc2
    $ is_in_v2_arc1 = False

    jump ending_splash