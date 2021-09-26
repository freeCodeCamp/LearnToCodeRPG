label start:
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
    menu:
        "How do you explain how the Internet works to a five-year old?"
    
        "Banana nuts":
            pass
    
        "I don't know":
            pass
    
        "...":
            pass

    $ timeout_label = None    
    with vpunch

    "Thanks for taking the time to complete our coding interview."
    "Before you go, please take some time to complete your basic information so we can get to know you better."
    "The fields marked with {color=#f00}*{/color} are required."

    # TODO: more customization like gender, pronouns, life story 
    python:
        # init player stats but we won't show the stats screen until the label `stage1_intro`
        player_stats = PlayerStats()

        player_name = renpy.input("What's your name? {color=#f00}*{/color} (Type something and hit Enter)")
        player_name = player_name.strip()
        if not player_name:
            player_name = "Lydia"
        persistent.player_name = player_name

        player_pronouns = renpy.input("What's your preferred pronoun?")
    
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

label stage1:
    scene black with dissolve
    pause 1
    show text "{size=48}{color=#fff}{i}Chapter 1: Where It All Started{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve

    # play music "audio/bgm/bgm_loop.wav" fadein 1.0 volume 0.5
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
    scene bg bedroom night with dissolve
    player confused "It's crazy how everyone these days is learning to code. High school students even."
    player "Six months then a six-figure job? That's even crazier."
    player "Hmm, but I can see the appeal in that."
    player awe "Maybe I can learn to code as well."

    show screen player_stats_screen(player_stats)

    player neutral "A bit of research won't hurt. Where shall we start? Maybe a coding bootcamp?"
    player distress "These bootcamp programs are expensive."
    player "Maybe I can go with free online resources first."
    player neutral "Let's see, what should we learn first? Python? JavaScript? Web Dev?"
    player awe "Oh here's a video about the top 10 tech skills worth learning in 2021. Let's check that out!"

    # player starts learning to code, so we initialize CS knowledge to 0
    $ player_stats.init_stats('CS Knowledge')

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

    player confused "Learn to code? Haha. I know it can't be that easy."
    player "There might be people who are cut out to do this, but definitely not me."
    player "I guess I better call it a day and go to bed."

    with fade
    player "I can't sleep with all these thoughts floating around in my head."
    player "What can I do if the kid I'm tutoring cuts down our sessions for his coding classes?"
    player "Ugh. I still need to pay the bills. Let's see if the coffee shop next door is hiring."

label stage3:
    # Stage 3. Annika
    scene black with dissolve
    pause 1
    show text "{size=48}{color=#fff}{i}Chapter 2: Annika from College{i}{/color}{/size}" with dissolve 
    pause 1
    hide text with dissolve

    $ player_stats.day_counter += 1
    scene bg bedroom day with fade
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    player confused "Here goes my phone at this early hour."
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    player "Do I merit a personal rejection call from the neighborhood coffee shop?"

    show annika
    annika "[persistent.player_name]! How have you been?"
    player happy "Annika! Geez. When was the last time you called me? When we were moving out after graduation?"
    player laugh "Anyways, it's really nice to hear from you again!"
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
            call stage4_wrong_name
            jump stage4_guess_name
        "coolCodersCamp":
            call stage4_wrong_name
            jump stage4_guess_name
        "freeCodeCamp":
            pass

    player "[freeCodeCamp]. That sounds right! Let's check it out!"

    $ player_stats.day_counter += 3
    scene bg bedroom day with fade
    show annika neutral
    player happy "Hey Annika. So I've been checking out [freeCodeCamp] as you suggested."
    player "I think its curriculum looks solid and I'd love to give it a try."
    player confused "It's honest hard work, though. And I'm not sure if I can make it through on my own..."
    player "What if I run into something that I can't understand? What if there is an issue I can't solve?"
    player "What if it gets too hard again and I lose my motivation?"
    show annika happy
    annika "That's totally okay! In fact, what I love about [freeCodeCamp] is that they have an entire community that can help you out and cheer you on."
    annika "And I can be your go-to accountability buddy as well! Ping me anytime if anything comes up."
    player happy "Thanks Annika. I know I can count on you."
    player laugh "Best of luck with your new job by the way! Let me know how it goes."

label stage6_trials:
    # Stage 4, 5, 6. Trials
    scene bg bedroom day with fade
    player "Okay, let's sit down to actually learn something."
    player "I'll start with the video lessons and then answer their multiple choice questions to check my understanding."
    call study_menu_choices from _call_study_menu_choices
    jump end_of_day_script

    show annika
    annika "Hey [persistent.player_name]! How did studying go?"
    player "Hey Annika!"
    player "I felt pretty productive today. It's nice how the curriculum gives you end-of-chapter tests for frequent feedback."
    player "How was work?"
    annika "It went well! I'm learning to use the custom framework that my company uses."
    player "That sounds like fun!"
    annika "It is pretty fun. I've heard about that tech stack from my friends at Hacker Space but I've never tried it."
    player "What is this Hacker Space you are talking about?"
    annika "It's just a casual meetup place for people interested in tech."
    annika "I highly recommend checking it out if you have time!"
    player "Hmmm..."
    annika "Haha don't worry. I know what you must be thinking about. It's not like nerds hanging out playing board games."
    annika "It's a chill space for people to gather, work, and build cool projects."
    player "That sounds nice. I will check it out."
    annika "Yay! And we should go together some time if you enjoy it!"

    jump end_of_day_script

label study_menu_choices:
    # correct choices increments CS knowledge
    # ask 4 questions each time
    $ num_questions = 4
    while num_questions > 0:
        if num_questions == 4:
            player "First question. Three more to go!"
        elif num_questions == 3:
            player "Second question. Halfway through!"
        elif num_questions == 2:
            player "Third question. Almost there!"
        elif num_questions == 1:
            player "Last question. Hang in there!"

        $ num_questions -= 1

        window hide
        # see cs_questions.rpy
        $ choices = renpy.random.choice(cs_questions)
        # result is True or False
        $ result = renpy.display_menu(choices)

        if result == True:
            $ player_stats.change_stats('CS Knowledge', 1)
            player "Correct!"
        else:
            player "Wrong..."

    return

label day_activity_choices:
    $ player_stats.day_counter += 1
    scene bg bedroom day with fade

    player "A new day!"
    player "Okay, so what shall we do for the day?"

label study_menu:
    menu:
        "Study CS fundamentals":
            player "Let's crunch some more code."
            call study_menu_choices from _call_study_menu_choices_1
            jump end_of_day_script
        "Take a walk":
            player "Let's head out to the park."
            call choice_walk from _call_choice_walk
            jump end_of_day_script
        "Work gig as a barista":
            player "I can do some shifts to cover my bills."
            call barista from _call_barista
            jump end_of_day_script
        "Hang out at Hacker Space":
            call hacker_space from _call_hacker_space
            jump end_of_day_script
        "Work on open-source projects":
            player "Annika mentioned that contributing to open-source project is a good way to learn."
            
            if player_stats.player_stats_map['CS Knowledge'] > 3: # can proceed
                player "Let's see, what are the newest Pull Requests?"
                call open_source from _call_open_source
                jump end_of_day_script
            else:
                player "Ehhh... I don't think my technical skills are solid enough for open-source projects yet. Maybe we can learn Git first?"
                call study_menu from _call_study_menu # re-enter choice screen

label open_source:
    scene bg laptop_screen
    player "Hmm... I don't know how to solve this but I can re-assign it to the original author."
    player "It's cool how people volunteer their time and energy to make software accessible."
    $ player_stats.change_stats('CS Knowledge', 1)
    return

label hacker_space:
    scene bg hacker_space
    player "Let's check out what cool projects people are working on."
    $ player_stats.change_stats('CS Knowledge', 1)
    return

label barista:
    scene bg cafe
    player "Here's your matcha latte. Enjoy your day!"
    player "Hmm... There are a group of kids in the back with their computers."
    kid "So I have this hackathon idea..."
    player "I don't mean to eavesdrop, but did they mention a hackathon?"
    player "Geez, kids these days are intense."
    player "But a hackathon? That sounds cool. I should give it a try when I know more about coding."
    return

label choice_walk:
    scene bg park
    player happy "It always soothe my nerves to take a walk in the park."
    player "I almost feel like it restores my sanity."
    $ player_stats.change_stats('Sanity', 10)
    return

label end_of_day_script:
    scene bg bedroom night with dissolve
    # TODO: rewrite logic
    $ player_stats.change_stats('Sanity', -10)
    player "Phew... That was a long day."

    if player_stats.player_stats_map['CS Knowledge'] > 5 and player_stats.day_counter > 8:
        jump stage7_ryan
    else:
        jump day_activity_choices # a new day

label stage7_ryan:
    # Stage 7. Ryan
    scene bg bedroom day with fade
    player "So I found this person's profile online. He taught himself to code with [freeCodeCamp]."
    player "He is now a senior software engineer and has decided to give back to the community."
    player "He said I can ask him anything so let's give it a shot."

    scene bg desk with dissolve
    show ryan

    ryan "Hi [persistent.player_name]. I'm Ryan. I'm a senior engineer at Colordeck."
    player "Hi Ryan. Nice to meet you! I'm [persistent.player_name], a recent grad and developer wannabe."
    ryan "That sounds good."
    ryan "Why don't I start by telling you a bit about myself? Then ask whatever you want to know about me, my job, or tech in general."
    player "Sounds good."
    ryan "It's a long story and a bumpy ride. So buckle up."
    ryan "I graduated from college some ten years ago. I majored in music and design so I worked as a freelance designer straight out of college."
    ryan "Freelancing gives me some freedom and flexibility at first, but I soon discovered that my skills weren't honed enough to attract large, established clients. And working with small, less established clients doesn't pay well and puts a lot of stress on a newbie freelancer."
    ryan "So I decided to upgrade my skills and try something new."
    ryan "I learned to design websites and got a job designing websites at a small local company."
    ryan "You know, at small companies, everyone does a little bit of everything."
    ryan "I was hired for my web design skills, but occasionally I would be asked to write some HTML, CSS, JavaScript to showcase the design I have in mind in action, not just on paper."
    ryan "I picked up a little HTML, CSS, JavaScript in those years and found them to be quite interesting."
    ryan "I then found out that there is a term for these skills, front-end development."
    ryan "I thought, cool, I've done some front-end development, maybe I can become a full-time front-end developer?"
    ryan "I started researching and teaching myself front-end dev. The Internet in my days didn't have nearly as many resources as nowadays. So I had to be extremely resourceful and develop my own learning path."
    ryan "It all paid off when I got my front-end development job at my current company. I've been with the company since. Nice culture, smart people, interesting work."
    player "Wow."
    ryan "Yeah, I know. Looking back it's like a blur."
    ryan "So that's my story. Anything you'd like to learn more about?"

    # initialize all choices to False
    $ ryan_story_choices = [False, False, False, False]
    label ryan_story_choices:
        menu:
            "What are you up to nowadays?" if not ryan_story_choices[0]:
                player "What are you up to nowadays?"
                ryan "If you are looking for a one-word answer, then it's “learning.” Everyone else I know will probably give you the same answer if you ask."
                $ ryan_story_choices[0] = True
                jump ryan_story_choices

            "Do you still have much to learn as a senior engineer?" if not ryan_story_choices[1]:
                player "Do you still have much to learn as a senior engineer?"
                ryan "Of course! I still run into technologies that are novel to me in my day-to-day."
                $ ryan_story_choices[1] = True
                jump ryan_story_choices

            "What is your experience working with people who have a CS degree versus who don't?" if not ryan_story_choices[2]:
                player "What is your experience working with people who have a CS degree versus who don't?"
                ryan "I'd say it's not too different. A CS degree may give you a headstart in your first year as a junior developer, but after then, it is up to you to learn, grow, and adapt continuously to new technology."
                $ ryan_story_choices[2] = True
                jump ryan_story_choices

            "Do you have a favorite side project?" if not ryan_story_choices[3]:
                player "Do you have a favorite side project?"
                ryan "There is one I'm working on right now. Top secret. You will know when you see it."
                ryan "Like I said, I majored in design and music in college. Design and music are two things that get me up in the morning."
                ryan "Now that I've also learned to code, I think it's prime time to put my passion into use to create something awesome, like a video game. I get to do the art, music, and coding all by myself."
                player "That sure sounds like fun! I'd love to see it one day!"
                $ ryan_story_choices[3] = True
                jump ryan_story_choices

            "I'm done asking!":
                player "I'm done asking! That's all I want to know. Thanks so much for sharing!"
                ryan "Anytime, [persistent.player_name]. Have fun coding and keep me updated on your progress!"

label stage8_interviews:
    # Stage 8. Coding interviews

    call screen confirm_and_share(
        "{bt}{size=[gui.name_text_size]}Congratulations!{/size}{/bt}\n\nYou completed the coding curriculum in {b}[player_stats.day_counter]{/b} days.\nNow you are ready to rock the coding interview and realize your dream of becoming a software engineer.\n Feel free to share your progress with the world!",
        ok_text="Let's go!"
        )

    scene bg bedroom night with dissolve
    player "I read that technical jobs ask candidates to complete coding interviews."
    player "I know how to code, so these interviews shouldn't be too hard if I study, right?"
    player "Let's do this."
    player "Hmm? What is a heap? I remember learning about lists and dictionaries in my course, but definitely not heaps."
    player "And heaps are under data structure fundamentals. Does that mean that I need to learn to implement a heap from scratch?"
    player "What is time complexity? What about space complexity? Does that mean that my code needs to run fast in addition to being correct?"
    player "Coding interviews are so different from coding..."
    player "Maybe I need to take some more courses specifically for coding interviews?"
    player "So I've applied to over 30 jobs this week."
    player "Submitted my resume, a cover letter, and whatnot."
    player "Yet nothing has happened."
    player "Let's maybe wait this out."
    player "Is there something wrong with my application?"
    player "I heard that some companies first screen resumes using AI, so maybe my resume never got to a recruiter..."
    player "I know I don't have the strongest resume, but still..."
    player "I've done what I could.I don't have a CS degree, so I took a quite comprehensive course. It is 300 hours! I even completed the end-of-curriculum project and put it on my GitHub."
    player "Maybe they threw my resume away as soon as they saw that I'm not a CS major."
    player "There is nothing I can do about that..."
    player "I guess the best I can do is to apply to more companies."
    player "That aside, in case I do hear back from anyone, what's next?"
    player "I read that the next step is usually an online assessment that features LeetCode-style questions."
    player "My coding interview skills are still pretty shaky. So let's keep grinding LeetCode while I wait."
    player "Oh, an email!"
    player "DevWire just sent me an online assessment!"
    player "They said I have a week to complete it and must do it in a 90-minute sitting."
    player "Well, here goes nothing."
    player "How come I have no idea what these questions are trying to get at?"
    player "They do look similar to some questions I saw on LeetCode, but I still have zero clue."

label stage14_becca:
    # Stage 14. New hire player
    scene bg office with dissolve
    show becca
    becca "Hey [persistent.player_name]. I'm Becca. I'm your onboarding buddy. Feel free to ask me anything."
    player "Hi Becca. Nice to meet you."
    player "... Um..."
    becca "Something on your mind?"
    player "I'm kind of stuck... Or, I guess a more accurate way to put this is, I don't even know where to start."
    becca "No worries! Onboarding could be daunting."
    becca "Think about it. Teams of talented developers spent months, even years, building out this codebase."
    player "Haha, thanks. That does make me feel better."
    becca "How about this? Let's take your mind off this code for a while and go grab coffee?"
    player "Sure, I'd love to!"
    player "Hey Becca. Mind if I ask how long you've been with this company and team?"
    becca "Of course not! I've been here for two years. I interned here when I was in college and returned full-time right after graduation."
    player "So you were a CS major?"
    becca "Yep."
    becca "Oh please I know that look. CS kids must have had it the easy way."
    becca "That's not true, you know."
    player "Oops, sorry."
    becca "No big deal."
    becca "Have you heard of the word, imposter syndrome?"
    player "Yeah. I feel that quite often."
    becca "You are good. That's almost the norm for people in tech."
    becca "Hah. Would you believe me if I tell you that imposter syndrome hits CS students equally hard, if not harder?"
    player "... Um... Tell me about it."
    becca "It starts the first time we step into a CS classroom, maybe earlier. There is always that kid that sits in the front row, who has been coding since five and knows everything the professor has yet to talk about."
    player "That's... intense."
    becca "And there is the expectation that CS kids should get big-names internships as early as their freshman year summer. Definitely not later than their junior year summer. Otherwise, the myth goes that they are unhirable."
    becca "I spent my freshman and sophomore summers volunteering at a local school teaching kids to code. I don't see any problems with that. I mean, I love coding and I love teaching, and being able to convey that to the next generation is an awesome opportunity for me."
    becca "But my friends were either interning for big names or building their own startups during the summer. They are nice enough not to say anything to my face, but I always feel a strange sense of hollowness when I see them post about their intern perks or startup progress."
    becca "It was a rough time, but my friends and my college advisors were supportive, and I eventually come to terms with being who I am and contributing to causes that I care about."
    becca "Haha sorry for the rant. I didn't mean to scare you away from continuing working in tech."
    becca "It's just that the battle with imposter syndrome is a continuous battle. Every little win is a win. In fact, I still grapple with imposter syndrome and have to stop myself from banging my head on the desk whenever I run into a bug I can't fix."
    player "Wow. Haha. Thanks for sharing. That actually makes me feel a lot better."
    becca "So are we ready to go back and squash some bugs?"
    player "Lead the way!"

    return
