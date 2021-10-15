label start:
    # stop main menu music
    stop music fadeout 3.0

    $ player_stats = PlayerStats()
    scene bg laptop_screen

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
    with pixellate
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
            pass
    
        "Career fair":
            pass

        "Job posting websites":
            pass

        "Referral":
            $ referral_name = renpy.input("What is the full name of your referral? (Type something and hit Enter)")
            # Easter egg :)
            if referral_name in ['Quincy', 'Quincy Larson', 'Lynn', 'Lynn Zheng', 'Abbey', 'Abbey Rennemeyer']:
                "System processing...{w}Looks like you were referred by a VIP team member. That's awesome!"
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
    
    window hide
    with pixellate
    "Thanks for completing your information. We will be in touch about next steps."

    with fade
    player "(Sigh....)"
    player "That was exhausting. There's no doubt that I bombed the questions."
    player "Geez, coding interviews are hard..."
    with vpunch
    player "What made me think I'm capable of getting a software job in the first place?"
    player "Well, it all started some time ago when I first decided to learn to code and get a real job..."

    # start the music here
    $ continue_looping_music = True

label stage1:
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 1: Let's learn to code!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve

    scene bg kid_home with fade

    # Stage 1. player background
    player "Okay, so that's it for today's session."
    kid "Uhh okay, so that's what trigonometry is about?"
    player "Yep. That's the basics of trigonometry."
    player confused "(I still can't believe I'm working this gig tutoring high school kids.)"
    player "(I just graduated from college but it's so hard to get a serious full-time job.)"
    player "(I did apply to some consulting firms and banks. And I've heard back from None.)"
    player "(It's not like I don't enjoy tutoring kids. I actually enjoy explaining concepts to others. I just need a full-time job that is more intellectually fulfilling.)"
    player "(Better yet if it pays better.)"
    kid "Hey [persistent.player_name]?"
    player neutral "Oh. {w}I just spaced out for a bit."
    player "Do you have any more questions before we wrap up?"
    kid "Nope! I think my project report is good to go. Thanks!"
    player "Good. I'll see you next week."
    kid "Oh sorry, can we do the week after the next?"
    kid "I just heard about a new class that teaches you how to code and build robots and I need to check that out next week."
    player "Sure, no problem. See you then."

label stage2:
    # Stage 2. player's decision to learn to code
    # player returns home
    scene bg livingroom night with dissolve

    player "I'm home!"
    mom "Hey sweetie. Welcome back!"
    dad "Welcome home, pumpkin. How was your day?"
    player "(That's my mom and dad. {w} Mom is a high school teacher, which is why she could find me this tutoring gig. {w}Dad is a mechanical engineer, but I never got too into engineering.)"
    player "Good. I'm tutoring this smart kid who wants to take up coding classes. I can't believe that came from a high school student."
    mom "That's interesting. I heard that a lot of high schools are rolling out coding curriculum."
    mom "That must be a trendy thing right now."
    dad "Yeah, remember our neighbor, the guy who moved away last month? I heard his kid is majoring in Computer Science at college."
    dad "The kid is only a junior but is already interning for large companies during summer break."
    player "Wow. Haha. That's pretty cool."

    # TODO: kitchen timer rings

    mom "Dinner's ready! I made your favorites."
    player "Thanks mom! You are the best!"

    # TODO: sound of kitchen utensils

    scene bg bedroom night with dissolve
    player happy "That was a stuffing dinner. Mom's the best cook I know."
    player "..."
    player neutral "Hmmm..."

    # TODO: sound of social media ding
    player "Must be something on social media."
    menu:
        "Check phone":
            pass

        "Ignore":
            jump stage2_after_social_media_ding

    player "Looks like someone from my junior high school. I don't even remember who they are."
    player "What did they post to get this crazy many likes?"
    player "{bt}\"Proud intern at {b}DonutDB{\b}. Check out my swaaaag!\"{/bt}"
    player "Oh. wow."
    player "Should I leave a like or comment on their post?"
    # no consequence
    menu:
        "Leave a like":
            pass
    
        "Post a comment":
            pass

        "Do nothing":
            pass

label stage2_after_social_media_ding:
    player confused "It's crazy how everyone these days is learning to code. High school students even."
    player "And what's with these boot camp programs? Six months then a six-figure job? That's even crazier."
    player "Hmm, but I can see the appeal in that."
    player awe "Maybe I can learn to code as well."
    mint "Meow meow"
    player "Haha, you think so as well, Mint?"
    player "(Mint, our home cat, is a real sweetie.)"
    player "(I mean, mom and dad are sweet and understanding enough, but Mint is definitely one of the reasons that I decided to move back home.)"

    player neutral "Alright, let's do this."
    player "A bit of research won't hurt. Where shall we start? Maybe a coding boot camp like everyone else is doing?"

    player distress "These boot camp programs are expensive."
    player "Maybe I can go with free online resources first."
    player neutral "Let's see, what should we learn first? Python? JavaScript? Web Dev?"
    player awe "Oh here's a video about the top 10 tech skills worth learning in 2021. Let's check that out!"

    # player starts learning to code, so we initialize CS knowledge to 0
    $ player_stats.init_stats('CS Knowledge')
    show screen player_stats_screen(player_stats)

    player "So Java and JavaScript are different languages? Wait, which one is for web dev again?"
    $ player_stats.change_stats('CS Knowledge', 1)
    $ player_stats.change_stats('Sanity', -5)

    player confused "And there are print statements and print() functions. Which is for Python 2 and which is for Python 3? I remember one video saying that Python 2 is outdated but does that mean that I don't have to learn it?"
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
    player "But what is front-end, back-end, or full-stack? What are the differences?"
    player "DevOps?"
    player "Why is this company using their pet coding language that nobody else uses?"

    # hard-reset player's CS knowledge :)
    python:
        player_stats.set_stats('CS Knowledge', 0)

    play sound 'audio/sfx/stats_change_doom.wav'
    player cry "Ugh. This is so frustrating."
    mint "Meow meow"
    player confused "Awww thanks Mint. I'm okay."
    player confused "Learn to code? Haha. I know it can't be that easy."
    player "There might be people who are cut out to do this, but definitely not me."
    player "I guess I better call it a day and go to bed."

    with fadehold
    player "... {w}I can't sleep with all these thoughts floating around in my head."
    player "What can I do if the kid I'm tutoring cuts down our sessions for his coding classes?"
    player "Ugh. I still need to pay the bills even if my parents are nice enough not to ask me for rent."
    player "Let's check out the coffee shop next door tomorrow and see if they are hiring."

label stage3:
    # Stage 3. Annika
    hide screen player_stats_screen
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 2: A learning buddy to make it better!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    show screen player_stats_screen(player_stats)
    # the above is standard for a chapter opening screen

    $ player_stats.day_counter += 1
    scene bg bedroom day with fade
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    player confused "Here goes my phone at this early hour."
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    player "Do I merit a personal rejection call from the neighborhood coffee shop?"

    show annika
    annika "[persistent.player_name]!"
    player happy "Annika! Geez. When was the last time you called me? When we were moving out after graduation?"
    player laugh "Anyways, it's really nice to hear from you again!"
    annika "Same! How have you been?"
    player netural "I've been okay. Just new grad blues. You?"

    show annika happy
    annika "Things are going pretty well for me! I just got my job offer!"
    annika "And, like, it's not just any job! It's a web development job!"
    annika "Can you believe it? I get paid generously for building cool websites."
    annika "It's almost like getting paid for being creative and doing art!"
    player laugh "Yeah. Wow. {bt}Congrats!{/bt}"
    annika "Thanks!"
    player netural "Hey, if I may ask, how hard was it for you to learn to develop websites?"
    player confused "I also tried to learn to code for some time but it got too hard and I quit."

    show annika confused
    annika "I'm sorry to hear that but you should give coding another try!"
    annika "Hey, hear me out."
    annika "It wasn't like easy peasy for me either. Like neither of us majored in CS. The CS kids have a way easier time getting a tech job."
    player "You did take some CS electives in school, no?"
    annika "Yeah but they are pretty rusty. And honestly, what you learn in school is so much different from real-world software engineering."

    show annika neutral
    annika "I mean, in school you learn about theories and stuff. Like I did take a Web Dev 101 back in school but we never built an entire website from scratch."
    annika "I never gave web design a second thought after the final exam."
    annika "I've been self-studying all these months with the help of some awesome free resources. I even built a pet adoption website for a side project and that's when I applied everything I learned about user experience, data models, and so on."
    annika "And there was this bug that I had no idea how to fix until..."
    annika "..."

    show annika happy
    annika "Oh sorry I've been talking all the time. I must have bored you with this tech talk stuff."
    player "No worries. It does look like you are doing something you enjoy!"
    player "That must be really cool. I wish I could be like you."
    annika "You totally can! Did I give you the link to the {bt}awesome resource{/bt} that I've been using?"
    annika "It's called [freeCodeCamp]. Check that out!"
    player laugh "Thanks. I will."

label stage4:
    scene bg bedroom night with fade

    player "Phew. It's been a long day at work. I'm glad that the coffee shop happens to need a part-time barista."
    player "Let's check out the awesome resource Annika's been talking about."
    jump stage4_guess_name

label stage4_wrong_name:
    player "That doesn't sound like the right name."
    player "My memory must be playing a trick on me."
    return

label stage4_guess_name:
    menu:
        player "What was it called again?"

        "freebieGoodie":
            call stage4_wrong_name from _call_stage4_wrong_name
            jump stage4_guess_name
        "coolCodersCamp":
            call stage4_wrong_name from _call_stage4_wrong_name_1
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
    $ stage5_choose_curriculum_visited = [False, ] * 10

label stage5_choose_curriculum:
    # this choice actually has no consequences on what the player will learn :)
    # show unavailable choices as greyed out
    $ config.menu_include_disabled = True
    menu:
        "Responsive Web Design" if not stage5_choose_curriculum_visited[0]:
            player confused "Ehhh... what even is web design? And I'm not a design person... Will I be able to follow along?"
            player "Maybe let's look some more?"
            $ stage5_choose_curriculum_visited[0] = True
            jump stage5_choose_curriculum
        "JavaScript Algorithms and Data Structures" if not stage5_choose_curriculum_visited[1]:
            player confused "I remember having heard about JavaScript. Or wait, that's perhaps Java."
            player "What are algorithms and data structures? That sounds like math, which is not my favorite subject."
            player "What other curriculum options do I have?"
            $ stage5_choose_curriculum_visited[1] = True
            jump stage5_choose_curriculum
        "Front End Development Libraries" if not stage5_choose_curriculum_visited[2]:
            player confused "Front end development? That sounds so complicated."
            player "Maybe I should go for some beginner topics?"
            $ stage5_choose_curriculum_visited[2] = True
            jump stage5_choose_curriculum

        "Data Visualization" if not stage5_choose_curriculum_visited[3]:
            player confused "I know there is some hype about big data, but can I really do that without a Ph.D.?"
            player "This doesn't look like it's for me."
            $ stage5_choose_curriculum_visited[3] = True
            jump stage5_choose_curriculum

        "Back End Development and APIs" if not stage5_choose_curriculum_visited[4]:
            player confused "Back end, front end. What are the differences? They definitely sound like they should go together."
            player "But I don't have the time or energy to learn both..."
            player "Let's look for something simpler."
            $ stage5_choose_curriculum_visited[4] = True
            jump stage5_choose_curriculum

        "Quality Assurance" if not stage5_choose_curriculum_visited[5]:
            player confused "Quality assurance? That sounds like I will be on a digital conveyor belt making sure all cookie packs weigh more or less the same."
            player awe "Nice, warm, and chewy cookies... I love cookies. Hope mom still keeps some in the kitchen cookie jar."
            mint "Meow?"
            player "Hey Mint. You want a cookie as well?"
            mint "Meow meow"
            menu:
                "Let's go grab a cookie from the kitchen":
                    call stage5_cookie from _call_stage5_cookie

                "Enough cookie talk! Let's go back to studying":
                    pass

            with vpunch
            player confused "Wait. {w}I got distracted. Where was I? Was I browsing the course category or something? Oh. I have this quality assurance tab open."
            player "At any rate, I don't think quality assurance is something I want to learn."
            $ stage5_choose_curriculum_visited[5] = True
            jump stage5_choose_curriculum

        "Scientific Computing with Python" if not stage5_choose_curriculum_visited[6]:
            player confused "Scientific computing? I'm not that much of a science person and I don't see myself becoming a scientist either."
            player "Plus I don't know anything about Python yet."
            player "I guess I'll pass."
            $ stage5_choose_curriculum_visited[6] = True
            jump stage5_choose_curriculum

        "Data Analysis with Python" if not stage5_choose_curriculum_visited[7]:
            player "Data analysis sounds cool..."
            player confused "But I don't know anything about Python. Plus I didn't do a lot of math in college."
            player "That's probably too hard for me right now."
            player "Let's find something else."
            $ stage5_choose_curriculum_visited[7] = True
            jump stage5_choose_curriculum

        "Information Security" if not stage5_choose_curriculum_visited[8]:
            player confused "What can I do after learning about information security?"
            player "Hack into others' computers? Stop bad guys from hacking into others' computers?"
            player "That sounds like a lot of moral commitment. I'm not sure if I can handle that."
            player "Is there something more neutral on the list?"
            $ stage5_choose_curriculum_visited[8] = True
            jump stage5_choose_curriculum

        "Machine Learning with Python" if not stage5_choose_curriculum_visited[9]:
            player awe "Machine Learning. Wow. That sounds cool."
            player "I'm really interested in teaching machines to learn."
            player "Just think about it. Teaching machines to chat like humans. {w}Wow."
            player "No wonder everyone is hyped about Artificial Intelligence these days."
            player "..."
            player confused "That said, it looks hard. I know nothing about machine learning, except that there are so many memes about how machine learning is nothing but math."
            player "Math... linear algebra... that kind of thing."
            player "That's probably out of the league for me."
            player "Maybe I should start with something more basic?"
            $ stage5_choose_curriculum_visited[9] = True
            jump stage5_choose_curriculum

        "Let's just wait until tomorrow and ask Annika for advice":
            player confused "Hmmm... I don't know. They all look equally hard. Let's ask Annika for advice tomorrow."
            mint "Meow!"
            player neutral "You think that's a good idea too, Mint?"
            player "Okay, let's get some rest today. Tomorrow is another day."
            jump stage5_annika

label stage5_cookie:
    scene kitchen night with dissolve
    mom "Hey honey, taking a break from all the studying?"
    mom "Your dad and I are really glad that you continue to learn new things after college, but don't push yourself too hard, okay?"
    player "Haha thanks Mom. I'm doing just fine."
    player "I'm just deciding on what CS topic to learn so I can get a job in tech like Annika."
    mom "Alright, know that we are always here if you'd like to talk or anything."
    player "I will. Thanks Mom."

    scene bedroom night with dissolve
    # sound of chewing on cookie
    player "Mmmm... Mom's cookies are the best."
    return

label stage5_annika:
    # the next day
    $ player_stats.day_counter += 1
    scene bg bedroom day with fade
    show annika neutral
    player happy "Hey Annika. So I've been checking out [freeCodeCamp] as you suggested."
    player "I think its curriculum looks solid."
    player confused "The thing is, I have no idea what to learn."
    player "They all look super complicated. I bet you put in honest hard work to complete them."
    player "Which one did you do, by the way?"

    annika "Oh, I did the web design one. What was it? {a=https://www.freecodecamp.org/learn/responsive-web-design/}Responsive Web Design?{/a}"
    annika "If I remembered anything from my college CS minor, it's those web markup languages."
    player confused "(So Annika managed to pull through the curriculum because she had some existing experience from college. Plus she has really good designer eyes.)"
    player "(I'm not like that... There's no way I can do this...)"

    annika "Hey [persistent.player_name], don't get discouraged, okay?"
    annika happy "It's already a big step forward now that you've checked out their curriculum!"
    annika "Trust me, I was just like you when I first started."
    annika "I was clueless, but then I decided to just go with their general introduction to computer science quizzes and start from there."
    annika "I found those bite-sized quizzes fun and easier to digest."
    annika "How does that sound?"

    player "Ehh... Even that, I'm not sure if I can make it through all the quizzes and CS concepts on my own..."
    player "What if I run into something that I can't understand?"
    player "What if the quizzes gets too hard like they always do at college, and I lose my motivation?"

    annika laugh "That's totally okay! In fact, what I love about [freeCodeCamp] is that they have an entire community that can help you out and cheer you on."
    annika "And I can be your go-to accountability buddy as well! Ping me anytime if anything comes up."
    player happy "Thanks Annika. I know I can count on you."
    player laugh "Best of luck with your new job by the way! Let me know how it goes."

label stage6:
    # Stage 6. Trials
    hide screen player_stats_screen
    scene black with dissolve
    pause 1
    show text "{size=48}{color=[white]}{i}Chapter 3: Let's hit the books!{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve
    show screen player_stats_screen(player_stats)

    scene bg bedroom day with fade

    # this first day has this fixed dialogue
    # after this, the start-of-day dialogue will be randomly drawn from start_of_day_event_labels.rpy
    # TODO: play sound of alarm
    player "Ahhh here goes my alarm."
    mint "Meow Meow"
    player "Ahhh good morning, Mint."
    player "..."
    player "Okay, let's do this. Let's sit down to actually learn something."
    player "I'll start with the video lessons and then answer their multiple choice questions to check my understanding."
    call study_session from _call_study_session

    # fixed dialogue for this first day
    scene bedroom night with dissolve
    player "Phew... I'm finally done with these questions. What a day..."
   
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"

    show annika
    annika "Heyya [persistent.player_name]! How did your first day of studying go?"
    player "Hey Annika! Thanks for checking in on me."
    player "I felt pretty productive today. It's nice how the curriculum gives you end-of-chapter tests for frequent feedback."
    player "What about your day? How was work?"
    annika "It went well! I'm learning to use the custom web dev framework that my company uses."
    annika "It's pretty different from what I've been using in my own projects, and a little confusing at times, but my colleagues said it gets better with time."
    player "That sounds like fun!"
    annika "It is pretty fun. Like it's not the first time I've heard about this framework. My friends at Hacker Space keep telling me how rad it is and I've been curious about it for a while."
    player "What is this {b}Hacker Space{/b} you are talking about?"
    annika "It's just a casual meetup place for people interested in tech."
    annika "I highly recommend checking it out if you have time!"
    player "Hmmm..."
    annika "Haha don't worry. I know what you must be thinking about. It's not like nerds hanging out playing board games."
    annika "It's a chill space for people to gather, work, and build cool projects."
    annika "You know what? At Hacker Space, you might actually find someone like you who's also learning to code. You can totally become study buddies!"
    player "That sounds nice. I will visit there some time."
    annika "Yay! And we should go together some time!"
    annika "Whelp, I guess you must be tired. Sleep tight and keep up your productive streak!"
    player "Haha thanks Annika. You as well. Have a good night and a great day at work tomorrow!"
    # TODO: play sound of hanging up phone

    player "Yawwwwwn... I can barely keep my eyes open. Today's been quite a workout day for my brain."
    player "Good night, Mint."
    mint "Meow"
    scene black with dissolve

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
    show screen player_stats_screen(player_stats)

    scene bg bedroom day with fade
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
    marco "Freelancing gives me some freedom and flexibility at first, but I soon discovered that my skills weren't honed enough to attract large, established clients. And working with small, less established clients doesn't pay well and puts a lot of stress on a newbie freelancer."
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
    $ marco_story_choices = [False, ] * 4
    # show unavailable choices as greyed out
    $ config.menu_include_disabled = True
    label marco_story_choices:
        menu:
            "What are you up to nowadays?" if not marco_story_choices[0]:
                player "What are you up to nowadays?"
                marco "If you are looking for a one-word answer, then it's “learning.” Everyone else I know will probably give you the same answer if you ask."
                $ marco_story_choices[0] = True
                jump marco_story_choices

            "Do you still have much to learn as a senior engineer?" if not marco_story_choices[1]:
                player "Do you still have much to learn as a senior engineer?"
                marco "Of course! I still run into technologies that are novel to me in my day-to-day."
                $ marco_story_choices[1] = True
                jump marco_story_choices

            "What is your experience working with people who have a CS degree versus who don't?" if not marco_story_choices[2]:
                player "What is your experience working with people who have a CS degree versus who don't?"
                marco "I'd say it's not too different. A CS degree may give you a head start in your first year as a junior developer, but after then, it is up to you to learn, grow, and adapt continuously to new technology."
                $ marco_story_choices[2] = True
                jump marco_story_choices

            "Do you have a favorite side project?" if not marco_story_choices[3]:
                player "Do you have a favorite side project?"
                marco "There is one I'm working on right now. Top secret. You will know when you see it."
                marco "Like I said, I majored in design and music in college. Design and music are two things that get me up in the morning."
                marco "Now that I've also learned to code, I think it's prime time to put my passion into use to create something awesome, like a video game. I get to do the art, music, and coding all by myself."
                player "That sure sounds like fun! I'd love to see it one day!"
                $ marco_story_choices[3] = True
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
    show screen player_stats_screen(player_stats)

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
    show screen player_stats_screen(player_stats)

    scene bg office with dissolve
    show layla

    layla "Hey [persistent.player_name]. I'm Layla. I'm your onboarding buddy. Feel free to ask me anything."

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

    layla "So how's work going? Have you worked your way through our codebase already?"
    player "... Um..."
    layla "Something on your mind?"
    player "I'm kind of stuck... Or, I guess a more accurate way to put this is, I don't even know where to start."
    layla "No worries! Onboarding could be daunting."
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
    show text "{size=48}{color=[white]}Learn To Code RPG was made possible by all the kind people who donate to support freeCodeCamp.org. You can help support our nonprofit's mission {a=https://www.freecodecamp.org/news/how-to-donate-to-free-code-camp/}{color=[blue]}here{/color}{/a}.\n\nThis project is open source. You can make suggestions and report bugs {a=https://github.com/freeCodeCamp/LearnToCodeRPG}{color=[blue]}here on GitHub{/color}{/a}.{/color}{/size}"
    with dissolve 
    pause 3
    hide text with dissolve

    scene gray90 with dissolve
    pause 1
    show text "{size=48}{color=[white]}Production & Music          {a=}{color=[blue]}Quincy Larson{/color}{/a}\nCoding & Writing            {a=https://ruolinzheng08.github.io/}{color=[blue]}Lynn Zheng{/color}{/a}\nArt                         {a=}{color=[blue]}Noa Trinh{/color}{/a}\nProofreading                {a=}{color=[blue]}Abbey Rennemeyer{/color}{/a}{/color}{/size}"
    with dissolve 
    pause 3
    hide text with dissolve

    # end of this game
    $ MainMenu(confirm=False)()
    return
