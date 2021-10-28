label start:
    default player_stats = PlayerStats()
    default todo_list = ToDoList()

    stop music fadeout 2.0
    scene bg laptop_screen with dissolve

    # get some action and conflict in here :)
    "Hi there. Thanks for applying to our software engineering role! {w}We've reviewed your resume and as a first step in our recruiting process, we'd like you to invite you to complete an online assessment."
    "Press start whenever you are ready."

    menu:
        "Start":
            pass

    # timed menu
    $ timeout = 5.0
    # Set the label that is jumped to if the player doesn't make a decision.
    $ timeout_label = "start_interview_question2"
    menu:
        "How do you prove that P = NP in one sentence?"

        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

label start_interview_question2:
    with vpunch
    $ timeout_label = "start_interview_question3"
    menu:
        "In Python, what is a generator?"
    
        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

label start_interview_question3:
    with hpunch
    $ timeout_label = "start_after_interview"
    menu:
        "How do you explain how the Internet works to a five-year old?"
    
        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

label start_after_interview:
    # reset to non-timed choices
    $ timeout_label = None    
    with vpunch

    "Thanks for taking the time to complete our coding interview."
    "Before you go, please take some time to complete your basic information so we can get to know you better."
    "The fields marked with {color=[red]}*{/color} are required."

    # TODO: more customization like gender, pronouns, life story 
    python:
        player_name = renpy.input("What is your name? {color=[red]}*{/color} (Type something and hit Enter)", default="Lydia")
        player_name = player_name.strip()
        if not player_name:
            player_name = "Lydia"
        persistent.player_name = player_name

        # TODO
        # player_pronouns = renpy.input("What's your preferred pronoun?")

    # questions with no substantial consequences
    menu:
        "How did you hear about this opportunity?"
    
        "Email":
            "Cool! We are glad that you are here!"
    
        "Career fair":
            "Cool! We are glad that you are here!"

        "Job posting websites":
            "Cool! We are glad that you are here!"

        "Referral":
            $ referral_name = renpy.input("What is the full name of your referral? (Type something and hit Enter)")
            # Easter egg :)
            if referral_name in ['Quincy', 'Quincy Larson', 'Lynn', 'Lynn Zheng', 'Abbey', 'Abbey Rennemeyer']:
                "System processing... {w}Looks like you were referred by a VIP team member. That's awesome! We'll highlight this on your profile."
            else:
                "Hmmm... We aren't able to locate that person in our employee database. Maybe you had a typo?"

        "Others (Please specify)":
            $ renpy.input("How did you hear about us? (Type something and hit Enter)")
            "Well, we aren't sure how you came across this opportunity through the portal you specified, but we are glad you are here!"

    menu:
        "Would you like to opt into our recruiting email list?"
    
        "Yes":
            pass
    
        "No":
            pass
    
    "Thanks for completing your information. We will be in touch about next steps."

    with fade
    player "(Sigh....)"
    player "That was exhausting. There's no doubt that I bombed the questions."
    player "Geez, coding interviews are hard..."
    with vpunch
    player "What made me think I'm capable of getting a software job in the first place?"
    player "Well... {w}it all started some time ago when I first decided to learn to code and get a real job..."

    # start the music here
    $ continue_looping_music = True

label stage1:
    $ quick_menu = False
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 1: Let's learn to code!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    $ quick_menu = True

    $ stats_unlocked = True
    scene bg kid_home with dissolve

    # Stage 1. player background
    player "Okay, so that's it for today's session."
    kid "Uhh okay, so that's what trigonometry is about?"
    player "Yep. That's the basics of trigonometry."
    kid "Okay... I need to reread my notes to make sure I have everything for the day."
    player "Sure. Take your time."
    player pout "(I still can't believe I'm working this gig tutoring high school kids.)"
    player "(I just graduated from college but it's so hard to get a serious full-time job.)"
    player "(I did apply to some consulting firms and banks. And I've heard back from none.)"
    player "(It's not like I don't enjoy tutoring kids. I actually enjoy explaining concepts to others. I just need a full-time job that is more intellectually fulfilling.)"
    player "(Better yet if it pays better...){p=0.5}{nw}"
    kid "Hey [persistent.player_name]?"
    player neutral "Oh. {w}Hey. {w}Sorry I just spaced out for a bit."
    player "Do you have any more questions before we wrap up?"
    kid "Nope! I think my project report is good to go. Thanks!"
    player "Good. I'll see you next week."
    kid "Oh sorry, can we do the week after the next?"
    kid "I just heard about a new class that teaches you how to code and build robots and I need to check that out next week."
    player "Sure, no problem. See you then."

label stage2:
    # Stage 2. player's decision to learn to code
    # player returns home
    scene bg living_room night with pushright

    player "I'm home!"
    mom "Hey sweetie. Welcome back!"
    dad "Welcome home, pumpkin. How was your day?"
    player "(That's my mom and dad. {w} Mom is a high school teacher, which is why she could find me this tutoring gig. {w}Dad is a mechanical engineer, but I never got too into engineering.)"
    player "(Not bragging but they are the nicest parents I know.)"
    player "My day is okay. I'm tutoring this smart kid who wants to take up coding classes. I can't believe that came from a high school student."
    mom "That's interesting. I heard that a lot of high schools are rolling out coding curriculum."
    mom "That must be a trendy thing right now."
    dad "Yeah, remember our neighbor, the guy who moved away last month? I heard his kid is majoring in Computer Science at college."
    dad "The kid is only a junior but is already interning for large companies during summer break."
    player "Wow. Haha. That's pretty cool."

    play sound 'audio/sfx/kitchen_beep.ogg'

    mom "Dinner's ready! I made your favorites."
    player "Thanks mom! You are the best!"

    # dinner scene
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    dad "So here's the best part about my day...{p=0.5}{nw}"
    player "Haha that's hilarious!{p=0.5}{nw}"
    mom "So what plans do we have for the weekend?{p=0.5}{nw}"
    player "I'm up to anything!{p=0.5}{nw}"

    scene bg bedroom night with blinds
    player happy "That was a stuffing dinner. Mom's the best cook I know."
    player "..."

    play sound 'audio/sfx/social_media_notification.wav'
    player neutral "Hmmm... A notification from my phone?  Must be something on social media."

    menu:
        "Check phone":
            pass

        "Ignore":
            player "Let's make this evening distraction-free for my sanity."
            jump stage2_after_social_media_ding

    player "Looks like someone from my junior high school. I don't even remember who they are."
    player "What did they post to get this crazy many likes?"
    player "{bt}\"Proud intern at {b}DonutDB{/b}. Check out my swaaaag!\"{/bt}"
    player "Oh. wow."
    player "Should I leave a like or comment on their post?"
    # no consequence
    menu:
        "Leave a like":
            player "Liked. Wow. They've got 1k+ likes already? Guess I'm one of them now."
    
        "Post a comment":
            player "{i}Congrats!{/i} {w}Posted. Now I'm one of their 100+ comments."

        "Do nothing":
            player "Meh, they are just bragging. I don't even know them that well."

label stage2_after_social_media_ding:
    player pout "It's crazy how everyone these days is learning to code and getting high-paying jobs in software."
    player "College itself has been crazy enough for me, and now people are going back to school to complete an online master's program in Computer Science?"
    player "Six months of self-paced learning and then a six-figure job? Talk about the end of craziness."
    player "Hmm, but I can see the appeal in that."
    player awe "Maybe I can learn to code as well."

    show mint
    mint "Meow meow~"
    player "Haha, you think so as well, Mint?"
    player "(Mint, our home cat, is a real sweetie.)"
    player "(I mean, mom and dad are sweet and understanding enough, but Mint is definitely one of the reasons that I decided to move back home.)"
    hide mint

    player neutral "Alright, let's do this."
    player "A bit of research won't hurt. Where shall we start? Maybe some free online resources like everyone else is doing?"
    player awe "Oh here's a video about the top 10 tech skills worth learning in 2021. Let's check that out!"

    # player starts learning to code, so we initialize CS knowledge to 0
    $ player_stats.set_stats('Sanity', 100)
    $ player_stats.set_stats('CS Knowledge', 0)
    # now the screen should be showing

    player "I'll keep track of my progress on my phone."

    "(Click on the phone icon {icon=ico-phone} on the bottom-right corner of the textbox to show or hide your progress.)"

    player "So Java and JavaScript are different languages? Wait, which one is for web dev again?"
    $ player_stats.change_stats('CS Knowledge', 1)
    $ player_stats.change_stats('Sanity', -5)

    player pout "And there are print statements and print() functions. Which is for Python 2 and which is for Python 3? I remember one video saying that Python 2 is outdated but does that mean that I don't have to learn it?"
    $ player_stats.change_stats('CS Knowledge', 1)
    $ player_stats.change_stats('Sanity', -5)

    player "Maybe I shouldn't bother with learning Python 3 even. Someone may just decide that Python 3 is too old-fashioned before I even get a chance to learn it."
    $ player_stats.change_stats('CS Knowledge', 1)
    $ player_stats.change_stats('Sanity', -5)

    player "Java doesn't sound like a good idea either. People are so hyped about Kotlin."
    $ player_stats.change_stats('CS Knowledge', 1)
    $ player_stats.change_stats('Sanity', -5)

    player distress "JavaScript? TypeScript?"
    $ player_stats.change_stats('CS Knowledge', 1)
    $ player_stats.change_stats('Sanity', -5)

    player "Maybe I can find a job posting I like and start learning their required skills."
    with hpunch
    player "But what is front-end, back-end, or full-stack? What are the differences?"
    with hpunch
    player "What are DevOps and Site Reliability Engineering?"
    with hpunch
    player "And why is this company using their pet coding language that nobody else uses?"

    # hard-reset player's CS knowledge :)
    $ player_stats.set_stats('CS Knowledge', 0)

    with vpunch
    play sound 'audio/sfx/stats_change_doom.wav'
    player cry "Ugh. This is so frustrating."

    show mint
    mint "Meow meow~"
    player pout "Awww thanks Mint. I'm okay."
    hide mint

    player pout "Learn to code? Haha. I know it can't be that easy."
    player "There might be people who are cut out to do this, but definitely not me."
    player "I guess I better call it a day and go to bed."

    hide screen player_stats_screen
    with fadehold
    player "... {w}I can't sleep with all these thoughts floating around in my head."
    player "What can I do if the kid I'm tutoring cuts down our sessions for his coding classes?"
    player "Ugh. I still need to pay the bills even if my parents are nice enough not to ask me for rent."
    player "Let's check out the coffee shop next door tomorrow and see if they are hiring."

label stage3:
    # Stage 3. Annika

    ## standard for a chapter openin screen
    # hide screen player_stats_screen
    $ quick_menu = False
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 2: A learning buddy to make it better!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    $ quick_menu = True
    ## standard for a chapter openin screen

    scene bg bedroom with dissolve
    $ player_stats.day_counter += 1
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    player pout "Here goes my phone at this early hour."
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    player "Do I merit a personal rejection call from the neighborhood coffee shop?"

    show annika
    annika "[persistent.player_name]!"
    player happy "Annika! Geez. When was the last time you called me? When we were moving out after graduation?"
    player laugh "Anyways, it's really nice to hear from you again!"
    annika "Same! How have you been?"
    player netural "I've been okay. Just new grad blues. You?"

    annika "Things are going pretty well for me! I just got my job offer!"
    annika "And, like, it's not just any job! It's a web development job!"
    annika "Can you believe it? I get paid generously for building cool websites."
    annika "It's almost like getting paid for being creative and doing art!"
    player laugh "Yeah. Wow. {bt}Congrats!{/bt}"
    annika "Thanks!"
    player netural "Hey, if I may ask, how hard was it for you to learn to develop websites?"
    player pout "I also tried to learn to code for some time but it got too hard and I quit."

    annika "I'm sorry to hear that but you should give coding another try!"
    annika "Hey, hear me out."
    annika "It wasn't like easy peasy for me either. Like neither of us majored in CS. The CS kids have a way easier time getting a tech job."
    player "You did take some CS electives in school, no?"
    annika "Yeah but they are pretty rusty. And honestly, what you learn in school is so much different from real-world software engineering."

    annika "I mean, in school you learn about theories and stuff. Like I did take a Web Dev 101 back in school but we never built an entire website from scratch."
    annika "I never gave web design a second thought after the final exam."
    annika "I've been self-studying all these months with the help of some awesome free resources. I even built a pet adoption website for a side project and that's when I applied everything I learned about user experience, data models, and so on."
    annika "And there was this bug that I had no idea how to fix until..."
    annika "..."

    annika "Oh sorry I've been talking all the time. I must have bored you with this tech talk stuff."
    player "No worries. It does look like you are doing something you enjoy!"
    player "That must be really cool. I wish I could be like you."
    annika "You totally can! Did I give you the link to the {bt}awesome resource{/bt} that I've been using?"
    annika "It's called [freeCodeCamp]. Check that out!"
    player laugh "Thanks. I will."
    player "(Let's add it to my to-do list.)"

    $ todo_unlocked = True
    $ todo_list.add_todo('Check out [freeCodeCamp]')
    "(Click on the To-Do icon {icon=list} to show or hide your To-Do items.)"

    annika "Anyways, what's your plan for the day?"
    player "Um, I need to check out the cafe around the neighborhood."
    annika "Cool! Let's catch up some time and get coffee!"
    player "Sure! Chat later!"
    hide screen player_stats_screen

label stage4:
    scene bg cafe with fadehold
    player "I'm glad that this coffee shop happens to need a part-time barista."
    player "Now at least I have some pocket money for necessities."
    player "This reminds me so much of college. I used to work part-time as a barista at the school library cafe as well."
    player "It was always nice to see my peers socializing and doing work at the cafe."
    player "An additional perk is that I get first-hand knowledge of interesting things happening on campus."
    player "That might also be true for this place. Looking around, I see quite a few people with their laptop."
    player "It's totally possible that some of them are working on the next million-dollar startup"
    player "Not totally out of scope given that the tech scene is booming in our quite little town."
    player "Or at least they might be talking about something interesting happening in the tech industry."

    girl "Hey hey! Did you hear that our school will soon have a computer club?"
    boy "Wow. Really? What do you plan to do at a computer club? Play video games?"
    girl "That, and much better! We can code stuff, maybe build a video game ourselves!"
    girl "I heard that we will have a dedicated teacher to lead the club. They will even host hackathons and stuff."
    boy "Hmmm, what are hackathons for?"
    girl "You know, like a marathon, but you hack away at some project instead of running around."
    boy "That sounds like fun. Do you have any project idea already?"
    girl "Emmm... Do you know this thing called a visual novel game?"
    boy "Tell me about it."

    player "Oops. I wasn't intentionally eavesdropping on high school kids, but the {b}hackathon{/b} idea they mentioned is new."
    player "I believe I can use this piece of information to my advantage. Let's make it a to-do item to ask Annika if she knows about events like this."

    $ todo_list.add_todo('Ask Annika about hackathons')
    player "Alright! Going back to my shift."
    hide screen player_stats_screen

    # player goes back home
    scene bg bedroom night with fadehold

    player dark "Phew... It's been a long day at work."

    scene bg laptop_screen night with dissolve
    player dim "Let's check out the awesome resource Annika's been talking about."

    menu stage4_guess_name:
        player "What was it called again?"

        "freebieGoodie":
            player "That doesn't sound like the right name."
            player "My memory must be playing a trick on me."
            jump stage4_guess_name

        "coolCodersCamp":
            player "That doesn't sound like the right name."
            player "My memory must be playing a trick on me."
            jump stage4_guess_name

        "freeCodeCamp":
            pass

label stage5:
    player "[freeCodeCamp]. That sounds right! Let's check it out!"
    show fcc_curriculum at truecenter with dissolve
    player "Wow. Their curriculum is sure comprehensive. {w}They also offer certifications that I can showcase on my resume. Neat!"
    player "What shall we start with?"
    hide fcc_curriculum

    # booleans mark whether a choice has been visited
    default stage5_choose_curriculum_visited = set()

    menu stage5_choose_curriculum:
        set stage5_choose_curriculum_visited

        "Responsive Web Design":
            player pout "Ehhh... what even is web design? And I'm not a design person... Will I be able to follow along?"
            player "Maybe let's look some more?"
            jump stage5_choose_curriculum

        "JavaScript Algorithms and Data Structures":
            player pout "I remember having heard about JavaScript. Or wait, that's perhaps Java."
            player "What are algorithms and data structures? That sounds like math, which is not my favorite subject."
            player "What other curriculum options do I have?"
            jump stage5_choose_curriculum

        "Front End Development Libraries" :
            player pout "Front end development? That sounds so complicated."
            player "Maybe I should go for some beginner topics?"
            jump stage5_choose_curriculum

        "Data Visualization":
            player pout "I know there is some hype about big data, but can I really do that without a Ph.D.?"
            player "This doesn't look like it's for me."
            jump stage5_choose_curriculum

        "Back End Development and APIs":
            player pout "Back end, front end. What are the differences? They definitely sound like they should go together."
            player "But I don't have the time or energy to learn both..."
            player "Let's look for something simpler."
            jump stage5_choose_curriculum

        "Quality Assurance":
            player pout "Quality assurance? That sounds like I will be on a digital conveyor belt making sure all cookie packs weigh more or less the same."
            player awe "Nice, warm, and chewy cookies... I love cookies. Hope mom still keeps some in the kitchen cookie jar."
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
            player pout "Wait. {w}I got distracted. Where was I? Was I browsing the course category or something? Oh. I have this quality assurance tab open."
            player "At any rate, I don't think quality assurance is something I want to learn."
            jump stage5_choose_curriculum

        "Scientific Computing with Python":
            player pout "Scientific computing? I'm not that much of a science person and I don't see myself becoming a scientist either."
            player "Plus I don't know anything about Python yet."
            jump stage5_choose_curriculum

        "Data Analysis with Python":
            player "Data analysis sounds cool..."
            player pout "But I don't know anything about Python. Plus I didn't do a lot of math in college."
            player "That's probably too hard for me right now."
            player "Let's find something else."
            jump stage5_choose_curriculum

        "Information Security":
            player pout "What can I do after learning about information security?"
            player "Hack into others' computers? Stop bad guys from hacking into others' computers?"
            player "That sounds like a lot of moral commitment. I'm not sure if I can handle that."
            player "Is there something more neutral on the list?"
            jump stage5_choose_curriculum

        "Machine Learning with Python":
            player awe "Machine Learning. Wow. That sounds cool."
            player "I'm really interested in teaching machines to learn."
            player "Just think about it. Teaching machines to chat like humans. {w}Wow."
            player "No wonder everyone is hyped about Artificial Intelligence these days."
            player "..."
            player pout "That said, it looks hard. I know nothing about machine learning, except that there are so many memes about how machine learning is nothing but math."
            player "Math... linear algebra... that kind of thing."
            player "That's probably out of the league for me."
            player "Maybe I should start with something more basic?"
            jump stage5_choose_curriculum

        "Let's just wait until tomorrow and ask Annika for advice":
            player pout "Hmmm... I don't know. They all look equally hard. Let's ask Annika for advice tomorrow."
            $ todo_list.add_todo('Ask Annika about CS curriculum')
            player "Added it to my To-Do!"
            player "Well, I did accomplish something today. Now at least I know what [freeCodeCamp]'s curriculum is about. That's one item off my To-Do list."
            $ todo_list.complete_todo('Check out [freeCodeCamp]')
            show mint
            mint "Meow!"
            player neutral "You think that's a good idea too, Mint?"
            player "Okay, let's get some rest today. Tomorrow is another day."
            hide mint
            hide screen player_stats_screen
            jump stage5_annika

label stage5_cookie:
    scene bg kitchen night with blinds
    mom "Hey honey, taking a break from all the studying?"
    mom "Your dad and I are really glad that you continue to learn new things after college, but don't push yourself too hard, okay?"
    player "Haha thanks Mom. I'm doing just fine."
    player "I'm just deciding on what CS topic to learn so I can get a job in tech like Annika."
    mom "Alright, know that we are always here if you'd like to talk or anything."
    player "I will. Thanks Mom."

    scene bg bedroom night with blinds
    show cookie at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Mmmm... Mom's cookies are the best."
    hide cookie
    return

label stage5_annika:
    # the next day
    $ player_stats.day_counter += 1
    scene bg bedroom with fade

    play sound 'audio/sfx/alarm.wav'
    player "Ahhh... my alarm... It's a new day already?"
    player "What's on our To-Do today?"
    show screen player_stats_screen
    player "Right. Let's give Annika a call and ask about the CS curriculum."
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"

    show annika

    player happy "Morning Annika!"
    annika "Morning! As energetic as ever, I see."
    player "Haha all thanks to you!"
    annika "What's up?"
    player "So I've been checking out [freeCodeCamp] as you suggested."
    player "I think its curriculum looks solid."
    player pout "The thing is, I have no idea what to learn. Web dev, data science, machine learning..."
    player "They all look super complicated. I bet you put in honest hard work to complete them."
    player "Which one did you do, by the way?"

    annika "Oh, I did the web design one. What was it? {a=https://www.freecodecamp.org/learn/responsive-web-design/}Responsive Web Design{/a}?"
    annika "If I remembered anything from my college CS minor, it's those web markup languages."
    player "Ahh I see."
    player pout "(So Annika managed to pull through the curriculum because she had some existing experience from college. Plus she has really good designer eyes.)"
    player "(I'm not like that... There's no way I can do this...)"

    annika "Hey [persistent.player_name], don't get discouraged, okay?"
    annika "It's already a big step forward now that you've checked out their curriculum!"
    annika "Trust me, I was just like you when I first started."
    annika "I was clueless, so I reached out to [freeCodeCamp]'s online community."
    annika "They recommended that I start with some general introduction to computer science quizzes on a site named [developerquiz]."
    annika "I found those bite-sized quizzes fun and easier to digest."
    annika "How does that sound?"

    player "Ehh... Even that, I'm not sure if I can make it through all the quizzes and CS concepts on my own..."
    player "What if I run into something that I can't understand?"
    player "What if the quizzes gets too hard like they always do at college, and I lose my motivation?"

    annika "That's totally okay! In fact, what I love about [freeCodeCamp] is that they have an entire community that can help you out and cheer you on."
    annika "And I can be your go-to accountability buddy as well! Ping me anytime if anything comes up."
    player happy "Thanks Annika. I know I can count on you."
    annika "Anytime!"
    annika "Well, I'm about to head out to work. Talk later!"
    player laugh "Best of luck with work! Let me know how it goes."

    play sound 'audio/sfx/phone_hangup.wav'
    hide annika

    player "Okay. Now I've asked about the curriculum. One To-Do item off the list."
    $ todo_list.complete_todo('Ask Annika about CS curriculum')
    player "I can ask Annika about other topics another day."
    player "Now my new To-Do would be to ramp up my CS knowledge."
    $ todo_list.add_todo('Ramp up CS knowledge')
    player "Sounds like a plan!"
    player "Time to go work my barista shift."
    hide screen player_stats_screen

    scene bg cafe with fadehold
    play sound 'audio/sfx/cafe_pour.wav'
    pause 5

    player "I don't see too many people in the cafe today. Maybe because it's a work day?"

    scene bg cafe dusk with fadehold
    play sound 'audio/sfx/cafe_pour.wav'
    pause 5
    player "That's about it for my shift. Not much happened."
    player "Let's head home early to squeeze in some studying tonight, just to keep up the momentum."

label stage6:
    # Stage 6. Trials
    hide screen player_stats_screen
    $ quick_menu = False
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 3: Let's hit the books!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    $ quick_menu = True

    scene bg bedroom dusk with fade
    player "I'm finally home! {w}Let's head over to [developerquiz] and try out some quiz questions."
    scene bg laptop_screen with dissolve
    player "Looks like I will need to complete four multiple choice questions per session."
    player "Let's do it."

    call study_session

    scene bg bedroom night with dissolve
    player "Phew... I'm finally done with these questions. What a day..."
    player "I think I did okay, but I do feel tired after a day at work."
    player "Maybe it's best for my productivity if I take an entire day off to study?"
    player "Let's give that a try tomorrow."
    show mint
    mint "Meow~"
    player "Good night, Mint."
    hide mint

    scene bg bedroom with fadehold
    
    # a new day, player studies in the morning, and hangs out with Annika at night
    play sound 'audio/sfx/alarm.wav'
    show mint
    mint "Meow~"
    player "Yawwwwwn... Good morning to you too, Mint."
    player "Okay, let's grab a quick breakfast and jump into studying."
    hide mint

    scene bg kitchen with blinds
    player "Morning, mom. Morning, dad."
    dad "Morning, pumpkin."
    mom "Morning, honey. Did you sleep well?"
    player "Yep. I'm recharged for a new day."
    dad "That's great. Let's start the morning with a nice family breakfast."

    show toast at truecenter
    pause 0.2
    play sound 'audio/sfx/chew_food.wav'
    player "Yum yum."
    hide toast

    scene bg bedroom with blinds

    player "Okay. Breakfast's done. Let's get to work."
    player "Hopefully I can get more questions correct today."

    call study_session

    scene bg bedroom with dissolve

    player "That's about it for the morning. I feel like I'm much more productive if I can focus on one thing for an entire day."    
    player "Let's alternate between working whole-day shifts and spending whole days studying."
    player "I can call Annika this afternoon when she's done with her work to chat and ask about things."

    scene bg bedroom dusk with fadehold

    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0

    show annika
    pause 1.0
    player "Hey Annika! Is now a good time to talk?"
    annika "Heyya [persistent.player_name]! Now's perfect. I just got back from work."
    annika "How did your first day of studying go?"
    player "I felt pretty productive today. It's nice how the quiz questions give you frequent feedback."
    player "What about your day? How was work?"
    annika "It went well! I'm learning to use the custom web dev framework that my company uses."
    annika "It's pretty different from what I've been using in my own projects, and a little confusing at times, but my colleagues said it gets better with practice."
    player "That sounds like fun!"
    annika "Yeah! And I've heard good things about this framework. Mostly from people I ran into at the local Hacker Space."
    annika "It looks like a popular tool for people who want to test out project ideas at hackathons."
    player "({b}Hackathons{/b}! That reminds me, I should probably ask Annika about this topic.)"
    player "(And she also just mentioned something called {b}Hacker Space{/b}. That's something worth asking about as well.){p=1.0}{nw}"
    annika "Hello? Earth to [persistent.player_name]?"
    player "Haha no worries I'm here. Just wondering about something."
    annika "What is it?"

    # booleans mark whether a choice has been visited
    default stage6_annika_questions_visited = set()

    menu stage6_annika_questions:
        set stage6_annika_questions_visited

        "What topic to ask Annika about?"

        "Hackthon":
            player "What is a hackathon?"
            annika "It's a event where people come together to design and implement cool tech projects."
            annika "Hackathons aren't usually too long. Most lasts for one or two days. {w}Now imagine people hacking away at their laptops overnight! You get the idea."
            annika "People usually form small teams to collaborate. It's especially cool when the team consists of people with different expertise, not just software engineers, but graphic designers and product managers as well."
            annika "It's a great way to brainstorm, prototype, and test out ideas that might one day evolve into full-fledged products."
            player "That sounds cool!"
            annika "Yeah! I've only been to one or two of them, but my company has those seasonal innovation events that I'll be checking out soon."
            annika "You should go to some hackathons as well! You will learn to collaborate with other developers and even designers."
            annika "Plus, hackathon projects look great on your resume."
            player "Cool! But how do I find hackathon events?"
            annika "Just search online! You might be surprised by the number of hackathons happening locally near you."
            player "That's awesome! I'll check that out when I get a bit better at coding."

            # TODO: todo_list.add_todo('Try out hackathons'), needs more writing
            $ todo_list.complete_todo('Ask Annika about hackathons')
            hide screen player_stats_screen
            jump stage6_annika_questions

        "Hacker Space":
            player "What is this Hacker Space you are talking about?"
            annika "It's just a casual meetup place for people interested in tech."
            annika "I highly recommend checking it out if you have time!"
            player "Hmmm..."
            annika "Haha don't worry. I know what you must be thinking about. It's not like nerds hanging out playing board games."
            annika "It's a chill space for people to gather, work, and build cool projects."
            annika "You know what? At Hacker Space, you might actually find someone like you who's also learning to code. You can totally become study buddies!"
            player "That sounds nice. I will go there some time."
            annika "Yay! And we should go together some time!"

            jump stage6_annika_questions

        "That's everything I need to know":
            jump stage6_after_annika_questions

label stage6_after_annika_questions:
    player "That's all I want to know. Thanks so much for answering my questions!"
    annika "Any time! You will become a pro in those tech culture terms in no time."
    annika "Whelp, I guess you must be tired after a day's studying. Enjoy a relaxing evening!"
    player "Haha thanks Annika. You as well. Have a good night and a great day at work tomorrow!"

    hide annika
    play sound 'audio/sfx/phone_hangup.wav'

    player "Whew. That's a lot of knowledge to unpack."
    dad "Dinner's ready, [persistent.player_name]!"
    player "(Wow. Dad is cooking tonight? He cooks perhaps once or twice a month, but when he cooks, it's usually really good.)"
    player "Coming!"

    # dinner scene
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    mom "Hey honey, how do you like working as a barista? You don't have to go if it distracts too much from your study, you know."
    dad "Your mom's right. We are here to support you if you ever need us."
    player "Thanks folks, but no worries. I can use an occasional break from studying."
    player "Plus, a lot of tech people visit the cafe and they talk a lot about cool tech stuff."
    player "Like I heard people talking about a type of event called a hackathon the other day, and I had the chance to ask Annika today."
    dad "That's great to hear, pumpkin. {w}What's Annika been up to? You two were really close at college, weren't you?"
    player "You won't believe it! She didn't major in CS but now she has this cool tech job...{p=0.5}{nw}"
    player "... And she taught herself everything...{p=0.5}{nw}"
    player "... I'm gonna work hard just like she did!"
    dad "That's the spirit!"
    scene bg kitchen night with fadehold

    scene bg bedroom night with blinds
    player "Yawwwwwn... What a day. My brain certainly enjoyed a great amount of workout today."
    player "I can barely keep my eyes open. Let's call this a day."
    player "Good night, Mint."
    show mint
    mint "Meow~"
    hide mint
    scene black with dissolve

    # TODO: now what?
    jump day_start

label stage7:
    # this stage is invoked inside label `day_end`
    # Stage 7. Marco
    hide screen player_stats_screen
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 4: A mentor to lead the way!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    show screen player_stats_screen

    scene bg bedroom with fade
    # play sound of typing
    # show a close-up graphic of Marco?
    player "So I found this person's profile online. He taught himself to code with [freeCodeCamp]."
    player "He is now a senior software engineer and has decided to give back to the community."
    player "He said I can ask him anything so let's give it a shot."

    scene bg desk with dissolve
    show marco

    $ has_met_marco = True

    marco "Hi [persistent.player_name]. I'm Marco. I'm a senior engineer at {b}QuicheQueue{\b}."
    player "Hi Marco. Nice to meet you! I'm [persistent.player_name], a recent grad and developer wannabe."
    marco "That sounds good."
    marco "Why don't I start by telling you a bit about myself? Then ask whatever you want to know about me, my job, or tech in general."
    player "Sounds good."
    marco "It's a long story and a bumpy ride. So buckle up."
    marco "I graduated from college some ten years ago. I majored in music and design so I worked as a freelance designer straight out of college."
    marco "Freelancing gives me some freedom and flexibility at first, but I soon discovered that my skills weren't honed enough to attract large, established clients."
    marco "And working with small, less established clients doesn't pay well and puts a lot of stress on a newbie freelancer."
    marco "So I decided to upgrade my skills and try something new."
    marco "I learned to design websites and got a job designing websites at a small local company."
    marco "You know, at small companies, everyone does a little bit of everything."
    marco "I was hired for my web design skills, but occasionally I would be asked to write some HTML, CSS, JavaScript to showcase the design I have in mind in action, not just on paper."
    marco "I picked up a little HTML, CSS, JavaScript in those years and found them to be quite interesting."
    marco "I then found out that there is a term for these skills, front-end development."
    marco "I thought, cool, I've done some front-end development, maybe I can become a full-time front-end developer?"
    marco "I started researching and teaching myself front-end dev. The Internet in my days didn't have nearly as many resources as nowadays. So I had to be extremely resourceful and develop my own learning path."
    marco "It all paid off when I got my front-end development job at my current company. I've been with the company since. Nice culture, smart people, interesting work."
    player "Wow."
    marco "Yeah, I know. Looking back it's like a blur."
    marco "So that's my story. Anything you'd like to learn more about?"

    # initialize all choices to False
    default marco_story_choices = set()
    menu marco_story_choices:
        set marco_story_choices
        "What are you up to nowadays?":
            player "What are you up to nowadays?"
            marco "If you are looking for a one-word answer, then it's “learning.” Everyone else I know will probably give you the same answer if you ask."
            jump marco_story_choices

        "Do you still have much to learn as a senior engineer?":
            player "Do you still have much to learn as a senior engineer?"
            marco "Of course! I still run into technologies that are novel to me in my day-to-day."
            jump marco_story_choices

        "What is your experience working with people who have a CS degree versus who don't?":
            player "What is your experience working with people who have a CS degree versus who don't?"
            marco "I'd say it's not too different. A CS degree may give you a head start in your first year as a junior developer, but after then, it is up to you to learn, grow, and adapt continuously to new technology."
            jump marco_story_choices

        "Do you have a favorite side project?":
            player "Do you have a favorite side project?"
            marco "There is one I'm working on right now. Top secret. You will know when you see it."
            marco "Like I said, I majored in design and music in college. Design and music are two things that get me up in the morning."
            marco "Now that I've also learned to code, I think it's prime time to put my passion into use to create something awesome, like a video game. I get to do the art, music, and coding all by myself."
            player "That sure sounds like fun! I'd love to see it one day!"
            jump marco_story_choices

        "I'm done asking!":
            player "I'm done asking! That's all I want to know. Thanks so much for sharing!"
            marco "Anytime, [persistent.player_name]. Have fun coding and keep me updated on your progress!"

    # go back to our routines
    jump day_start

label stage8:
    # Stage 8. Coding interviews
    hide screen player_stats_screen
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 5: Let's crunch 'em interviews!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    show screen player_stats_screen

    scene bg bedroom night with dissolve
    player "I read that technical jobs ask candidates to complete coding interviews."
    player "I now know how to code, so these interviews shouldn't be too hard if I study, right?"
    player "Let's do this."
    player "Hmm? What is a heap? I remember learning about lists and dictionaries in my course, but definitely not heaps."
    player "And heaps are under data structure fundamentals. Does that mean that I need to learn to implement a heap from scratch?"
    player "What is time complexity? What about space complexity? Does that mean that my code needs to run fast in addition to being correct?"
    player "Coding interviews are so different from coding..."
    player "Maybe I need to tackle more questions specifically for coding interviews?"
    player "Or I could try applying to jobs first."
    player "... {w}I don't know. Should I get some advice from Annika and Marco?"

    menu:
        "Call Annika":
            # TODO
            "Okay I'll write some dialogue w Annika"
    
        "Message Marco":
            # TODO
            "Okay I'll write some dialogue w Marco"
    
        "Research online on my own":
            player "Hmmm... People online recommend applying to jobs as soon as possible."

    player "Okay, let's search for some jobs on the web."

    call day_activity_job_search from _call_day_activity_job_search


    player "Let's call this a day and restart our routines tomorrow."
    # go back to our routines
    jump day_start

# actually no stages between 8 and 14

label stage14:
    # Stage 14. New hire player meets Layla
    # TODO
    hide screen player_stats_screen
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 6: Let's meet my new colleagues!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    show screen player_stats_screen

    scene bg office with dissolve
    show layla

    layla "Hey [persistent.player_name]. I'm Layla. I'm your on boarding buddy. Feel free to ask me anything."

    if not has_met_layla:
        player "Hi Layla. Nice to meet you."
    else:
        player "(Hmmm... I wonder if we have met before. Layla looks familiar somehow.)"
        player "(... {w}Oh! {w}Was that her at Hacker Space?)"
        # TODO: flashback fade

        scene bg hacker_space with fadehold
        layla "So how's everyone's project going? We mentors are here to answer any question you have!"

        scene bg office with dissolve
        layla "[persistent.player_name]? Are you okay? You are spacing out."
        player "Ah! I'm fine. I just remembered that we might have met before."
        player "You know, at Hacker Space. I used to go there to study and work on projects before I get this job."
        layla "Oh, wow. Yeah. I was at various Hacker Space events. {w}Nice to hear that you enjoyed the space!"

    layla "So how's work going? Have you worked your way through our code base already?"
    player "... Um..."
    layla "Something on your mind?"
    player "I'm kind of stuck... Or, I guess a more accurate way to put this is, I don't even know where to start."
    layla "No worries! On boarding could be daunting."
    layla "Think about it. Teams of talented developers spent months, even years, building out this codebase."
    player "Haha, thanks. That does make me feel better."
    layla "How about this? Let's take your mind off this code for a while and go grab coffee?"
    player "Sure, I'd love to!"
    player "Hey Layla. Mind if I ask how long you've been with this company and team?"
    layla "Of course not! I've been here for two years. I interned here when I was in college and returned full-time right after graduation."
    player "So you were a CS major?"
    layla "Yep."
    layla "Oh please I know that look. CS kids must have had it the easy way."
    layla "That's not true, you know."
    player "Oops, sorry."
    layla "No big deal."

    # TODO: Layla AMA session like Marco

    layla "Have you heard of the word, imposter syndrome?"
    player "Yeah. I feel that quite often."
    layla "You are good. That's almost the norm for people in tech."
    layla "Hah. Would you believe me if I tell you that imposter syndrome hits CS students equally hard, if not harder?"
    player "... Um... Tell me about it."
    layla "It starts the first time we step into a CS classroom, maybe earlier. There is always that kid that sits in the front row, who has been coding since five and knows everything the professor has yet to talk about."
    player "That's... intense."
    layla "And there is the expectation that CS kids should get big-names internships as early as their freshman year summer. Definitely not later than their junior year summer. Otherwise, the myth goes that they are unhirable."
    layla "I spent my freshman and sophomore summers volunteering at a local school teaching kids to code. I don't see any problems with that. I mean, I love coding and I love teaching, and being able to convey that to the next generation is an awesome opportunity for me."
    layla "But my friends were either interning for big names or building their own startups during the summer. They are nice enough not to say anything to my face, but I always feel a strange sense of hollowness when I see them post about their intern perks or startup progress."
    layla "It was a rough time, but my friends and my college advisors were supportive, and I eventually come to terms with being who I am and contributing to causes that I care about."
    layla "Haha sorry for the rant. I didn't mean to scare you away from continuing working in tech."
    layla "It's just that the battle with imposter syndrome is a continuous battle. Every little win is a win. In fact, I still grapple with imposter syndrome and have to stop myself from banging my head on the desk whenever I run into a bug I can't fix."
    player "Wow. Haha. Thanks for sharing. That actually makes me feel a lot better."
    layla "So are we ready to go back and squash some bugs?"
    player "Lead the way!"

    jump ending

label ending:
    scene office with dissolve
    player happy "Okay, I think my code is good to go! Let's commit it to the server."
    # TODO: system processing animation
    player "... {w}And nothing happened."

    # stop the music here
    $ continue_looping_music = False
    stop music

    # office red alert animation

    hide screen player_stats_screen
    call screen confirm_and_share(
        title="{color=[red]}{icon=alert} Attention{/color}",
        message="Hey [persistent.player_name]... \nThe thing is, it looks like... {sc}{color=[red]}YOU HAVE BROUGHT DOWN THE PRODUCTION SERVER{/color}{/sc}",
        ok_text="Oopsy... Am I... fired?"
    )

    $ quick_menu = False

    scene black with pixellate
    pause 1
    show text "{bt}{size=48}{color=[white]}{i}Well, that's another chapter :){i}{/color}{/size}{/bt}" with dissolve 
    pause 3
    hide text with dissolve

    # Learn to Code RPG logo
    scene gray90 with Pause(1)
    show learn_to_code_splash at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    # freeCodeCamp logo
    scene gray90 with Pause(1)
    show fcc_splash at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    # Credits, like in the About section from options.rpy
    scene gray90 with dissolve
    pause 1
    show text "{size=48}{color=[white]}[about]{/color}{/size}"
    with dissolve 
    pause 3
    hide text with dissolve

    scene gray90 with dissolve
    pause 1
    show text "{size=48}{color=[white]}[credits]{/color}{/size}"
    with dissolve 
    pause 3
    hide text with dissolve

    # end of this game
    $ MainMenu(confirm=False)()
    return
