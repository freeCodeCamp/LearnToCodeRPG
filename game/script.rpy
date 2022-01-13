label start:
    default player_stats = PlayerStats(all_skills)
    default todo_list = ToDoList()
    default calendar = Calendar(day=1, month=8, year=2021) # story starts on Aug 1st, 2021
    default start_date = date(2021, 8, 1) # this will be used to calculate how many days it took for the player to learn to code

    $ persistent.has_started_game = True
    $ calendar_enabled = False

    stop music fadeout 2.0
    scene bg laptop_screen with dissolve

    # get some action and conflict in here :)
    "Hi there. Thanks for applying to our software engineering role!"
    "We've reviewed your résumé, and as a first step in our recruiting process, we'd like to invite you to complete an online assessment."

    menu:
        "We'll start whenever you're ready."

        "Guess I have no other options. Let's start!":
            pass

    # timed menu
    $ timeout = 5.0
    # Set the label that is jumped to if the player doesn't make a decision.
    $ timeout_label = "start_interview_question2"
    "First question."
    menu:
        "How do you prove that P = NP in one sentence?"

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
        "In Python, what is a generator?"

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
        "How do you explain how the Internet works to a five year old?"

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

    "Thanks for taking the time to complete our coding interview."
    "Before you go, please take some time to fill in your basic information so we can get to know you better."
    "The fields marked with {color=[red]}*{/color} are required."

    # TODO: more customization like gender, pronouns, life story
    $ player_name = ''
    player pout "(Phew... Looks like I survived the technical questions. Now let's fill in the general information.)"

    $ player_name = renpy.input(_("What is your name? {color=[red]}*{/color} (Type your name and hit Enter. This name will be used throughout the game and you cannot change it unless you start a new game.)"), default=_("Lydia"))
    $ player_name = player_name.strip()
    if player_name in vip_names:
        $ vip_profile_url = vip_names[player_name]
        "[player_name]? What a coincidence! Our VIP team member {a=[vip_profile_url]}[player_name]{/a} will be honored to hear that."
        # TODO: Easter Egg
    # handle empty string case
    if not player_name:
        $ player_name = _("Lydia")

    # TODO: birthday Easter Egg
    # "What is your birthday?"

    # TODO
    # player_pronouns = renpy.input("What's your preferred pronoun?")
    menu:
        "What set of pronouns do you prefer?"

        "She/Her":
            "We will refer to you with she/her pronouns from now on."
            $ player_pronouns = FEMALE_PRONOUNS
        "He/Him":
            "We will refer to you with he/him pronouns from now on."
            $ player_pronouns = MALE_PRONOUNS
        "They/Them":
            "We will refer to you with they/them pronouns from now on."
            $ player_pronouns = NONBINARY_PRONOUNS

    # questions with no substantial consequences
    menu:
        "How did you hear about this opportunity?"

        "Email":
            "Cool! We're glad that you're here!"

        "Career fair":
            "Cool! We're glad that you're here!"

        "Job posting websites":
            "Cool! We're glad that you're here!"

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
        "Would you like to opt in to our recruiting email list?"

        "Yes":
            "Way to go! We'll notify you about all the events and opportunities."

        "No":
            "Maybe next time?"

    "Thanks for filling in your information. We will be in touch about the next steps."

    with fadehold
    player "(Sigh...)"
    player "That was exhausting. There's no doubt that I bombed the questions."
    player "Geez, coding interviews are hard..."
    play sound 'audio/sfx/punch.wav'
    with vpunch
    player pout "What made me think I could get a software job in the first place?"
    player "Well... it all started some time ago when I first decided to learn to code and get a real job..."

label stage1:
    # use call instead of show b/c the screen will return after the timer finishes
    call screen text_over_black_bg_screen(_('About three months ago...'))
    call screen text_over_black_bg_screen(_("{i}Chapter 1: Let's learn to code!{/i}"))

    scene bg kid_home
    $ calendar_enabled = True
    # start the music here
    # $ continue_looping_music = True
    $ renpy.music.queue(all_music_files, loop=True, fadein=1.0, tight=True)

    # Stage 1. player background
    show boy orange
    player smile "Okay, so that's it for today's session."
    kid "Uhh okay, so that's what trigonometry is all about?"
    player "Yep. That's the basics of trigonometry."
    kid "Okay... I need to reread my notes to make sure I have everything for the day."
    player "Sure. Take your time."
    player pout "(I still can't believe I'm working this gig tutoring high school kids.)"
    player "(I just graduated from college but it's so hard to get a serious full-time job.)"
    player "(I did apply to some consulting firms and banks. And I've heard back from none of them.)"
    player "(It's not like I don't enjoy tutoring kids. I actually enjoy explaining concepts to others. I just need a full-time job that is more intellectually fulfilling.)"
    player "(Better yet if it pays more...)"
    kid "Hey [player_name]?"
    player surprised "Oh. Hey. Sorry I just spaced out for a bit."
    player smile "Do you have any more questions before we wrap up?"
    kid "Nope! I think my project report is good to go. Thanks!"
    player "Good. I'll see you next week."
    kid "Oh sorry, can we do the week after next?"
    kid "I just heard about a new class that teaches you how to code and build robots and I need to check that out next week."
    player "Sure, no problem. See you then."

label stage2:
    # Stage 2. player's decision to learn to code
    # player returns home
    scene bg living_room night with slideright

    player laugh "I'm home!"
    mom "Hey sweetie. Welcome back!"
    dad "Welcome home, pumpkin. How was your day?"
    player happy "(That's my mom and dad.  Mom is a high school teacher, which is why she could find me this tutoring gig. Dad is a mechanical engineer, but I never got too into engineering.)"
    player "(Not to brag, but they are the nicest parents I know.)"
    player "I had an okay day."
    player "I'm tutoring this smart kid who wants to take up coding classes. I can't believe that came from a high school student."
    mom "That's interesting. I heard that a lot of high schools are rolling out coding curricula."
    mom "That must be a trendy thing right now."
    dad "Yeah, remember our neighbor, the guy who moved away last month? I heard his kid is majoring in Computer Science at college."
    dad "The kid is only a junior but is already interning for big companies during summer break."
    player "Wow. Haha. That's pretty cool."

    play sound 'audio/sfx/kitchen_beep.ogg'

    mom "Dinner's ready! I made your favorites."
    player "Thanks mom! You are the best!"

    # dinner scene
    scene bg kitchen night with blinds
    play sound 'audio/sfx/dining_ambient.wav'
    $ show_random_dinner_image()
    dad "So here's the best part about my day..."
    player laugh "Haha that's hilarious!"
    mom "What plans do we have for the weekend?"
    player "I'm up for anything!"

    scene bg bedroom night with blinds
    player happy "That was an awesome dinner... I'm stuffed. Mom's the best cook I know."

    play sound 'audio/sfx/social_media_notification.wav'
    show smartphone at truecenter
    player surprised "Hmmm... A notification from my phone?  Must be something on social media."

    menu:
        "Check phone":
            player "Looks like someone from my junior high school. I don't even remember who they are."
            player "What did they post to get this crazy number of likes?"
            hide smartphone
            show swag at truecenter with zoomin
            player "{bt}\"Proud intern at {b}DonutDB{/b}. Check out my swaaaag!\"{/bt}"
            hide swag
            player "Oh. wow."
            player smile "Should I leave a like or comment on their post?"
            # no consequence
            menu:
                "Leave a like":
                    player "Liked. Wow. They've got 1k+ likes already? Guess I'm one of them now."

                "Post a comment":
                    player "{i}Congrats!{/i} Posted. Now I'm one of their 100+ comments."

                "Do nothing":
                    player "Meh, they are just bragging. I don't even know them that well."

        "Ignore":
            hide smartphone
            player relieved "Let's make this evening distraction-free for my sanity."

    "(Hey [player_name]. It looks like you just made your first in-game choice. That is awesome!)"
    "(You will encounter many more choices in this game later on. There are no right or wrong choices, only consequences.)"
    "(So it might be a good idea to save your progress when you are about to make a choice, start a new chapter, or just when you feel like it.)"

    call save_reminder from _call_save_reminder

    player relieved "..."
    player surprised "Oops. Did I just doze off? Geez... Where was I? Something about coding interviews?"
    player pout "It's crazy how everyone these days is learning to code and getting high-paying jobs in software."
    player "College itself was intense enough for me, and now people are going back to school to complete online master's programs in Computer Science?"
    player "Six months of self-paced learning and then a six-figure job? Talk about the end of craziness."
    player "Hmm, but I can see the appeal in that."
    player laugh "Maybe I can learn to code as well."

    show mint
    mint "Meow meow~"
    player "Haha, you think so too, Mint?"
    player "(Mint, our home cat, is a real sweetie.)"
    player "(I mean, mom and dad are sweet and understanding enough, but Mint is definitely one of the reasons that I decided to move back home.)"
    hide mint

    player neutral "Alright, let's do this."
    player "A bit of research won't hurt. Where shall we start? Maybe I should find some free online resources like everyone else is doing?"
    player surprised "Oh here's a video about the top 10 tech skills worth learning this year. Let's check that out!"

    # now the quick menu screen show the button to access stats
    $ stats_unlocked = True
    $ stats_knowledge_unlocked = True

    player smile "I'll keep track of my progress on my phone."
    show smartphone at truecenter
    "(Click on the {icon=icon-smartphone} {b}Stats{/b} button on the bottom-right corner of the textbox to view your progress.)"
    hide smartphone
    player "Alright. Here goes nothing."
    player "..."

label stage2_stats_change:
    player surprised "So Java and JavaScript are different languages?"
    $ player_stats.change_stats('CS Knowledge', 1)
    player "Wait, which one is for web dev again?"
    $ player_stats.change_stats('Sanity', -5)

    player pout "And there are print statements and print() functions. Which is for Python 2 and which is for Python 3?"
    $ player_stats.change_stats('CS Knowledge', 1)
    player "I remember one video saying that Python 2 is outdated. Does that mean that I don't have to learn it?"
    $ player_stats.change_stats('Sanity', -5)

    player "Maybe I shouldn't even bother with learning Python 3."
    $ player_stats.change_stats('CS Knowledge', 1)
    player "Someone may just decide that Python 3 is too old-fashioned before I even get a chance to learn it."
    $ player_stats.change_stats('Sanity', -5)

    player worry "Java doesn't sound like a good idea either. It's really old."
    $ player_stats.change_stats('CS Knowledge', 1)
    player "People nowadays are so hyped about Kotlin."
    $ player_stats.change_stats('Sanity', -5)

    player "JavaScript? TypeScript?"
    $ player_stats.change_stats('CS Knowledge', 1)
    player "Are they like cousins or something?"
    $ player_stats.change_stats('Sanity', -5)

    player "Maybe I can find a job posting I like and start learning their required skills."
    play sound 'audio/sfx/punch.wav'
    with hpunch
    player pout "But what is front-end, back-end, or full-stack? What are the differences?"
    play sound 'audio/sfx/punch.wav'
    with hpunch
    player "What are DevOps and Site Reliability Engineering?"
    play sound 'audio/sfx/punch.wav'
    with hpunch
    player "And why is this company using their pet coding language that nobody else uses?"

    # hard-reset player's CS knowledge :)
    $ player_stats.set_stats('CS Knowledge', 0)

    with vpunch
    play sound 'audio/sfx/stats_change_doom.wav'
    player worry "Ugh. This is so frustrating."

    show mint
    mint "Meow meow~"
    player pout "Awww thanks Mint. I'm okay."
    hide mint

    player "Learn to code, huh? I guess it's not that easy..."
    player "There might be people who are cut out to do this, but definitely not me."
    player "I guess I better call it a day and go to bed."

    scene black with eyeclose

    play sound 'audio/sfx/wake_up_noise.mp3'
    pause 2.0
    scene bg bedroom night with eyeopen
    player worry "... I can't sleep with all these thoughts floating around in my head."
    player "What can I do if the kid I'm tutoring cuts down our sessions for his coding classes?"
    player "Ugh. I still need to pay the bills even if my parents are nice enough not to ask me for rent."
    player relieved "Let's check out the coffee shop next door tomorrow and see if they're hiring."

label stage3:
    # Stage 3. Annika
    call screen text_over_black_bg_screen(_('{i}Chapter 2: A learning buddy to make it better!{/i}'))
    $ calendar.next()
    scene black
    scene bg bedroom with eyeopen

    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    show smartphone at truecenter
    player pout "Here goes my phone at this early hour."
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    player "Do I merit a personal rejection call from the neighborhood coffee shop before I even visit them?"
    hide smartphone

    show annika
    annika "[player_name]!"
    player surprised "Annika! Geez. When was the last time you called me? When we were moving out after graduation?"
    player laugh "Anyways, it's really nice to hear from you again!"
    annika "Same! How have you been?"
    player smile "I've been okay. Just new grad blues. You?"

    show annika laugh
    annika "Things are going pretty well for me. I just got a job offer!"
    annika "And, like, it's not just any job – it's a web development job!"
    annika "Can you believe it? I get paid really well to build cool websites."
    annika "It's almost like getting paid for being creative and doing art!"
    player surprised "Yeah. Wow. {bt}Congrats!{/bt}"
    annika "Thanks!"
    player smile "Hey Annika, how hard was it for you to learn to develop websites?"
    player pout "I also tried to learn to code for a while, but it got too hard and I quit."

    show annika neutral
    annika "I'm sorry to hear that, but you should give coding another try!"
    annika "Hey, hear me out."
    annika "It wasn't like easy peasy for me either. Like neither of us majored in CS. The CS kids have a way easier time getting a tech job."
    player "You did take some CS electives in school, didn't you?"
    annika "Yeah, but those skills are pretty rusty. And, honestly, what you learn in school is so different from real-world software engineering."

    show annika serious
    annika "I mean, in school you learn about theories and stuff. Like I did take Web Dev 101 back in school, but we never built an entire website from scratch."
    annika "I never gave web design a second thought after the final exam."
    annika "I've been self-studying all these months using some awesome free resources."
    annika "I even built a pet adoption website as a side project and that's when I applied everything I learned about user experience, data models, and so on."
    annika "And there was this bug that I had no idea how to fix until..."
    annika "..."

    show annika neutral
    annika "Oh sorry I've been talking for a long time. I must be boring you with this tech talk stuff."
    player "No worries. It does look like you're doing something you enjoy!"
    player pout "That must be really cool. I wish I could be like you."
    annika "You totally can! Did I give you the link to the {bt}awesome resource{/bt} that I've been using?"
    annika "It's called [freeCodeCamp]. Check that out!"
    player laugh "Thanks. I will."
    player "(Let's add it to my To-Do list.)"

    $ todo_unlocked = True
    $ todo_list.add_todo(todo_check_fcc)
    "(On the {icon=icon-smartphone} {b}Stats{/b} screen, you can toggle between showing your stats and showing your To-Do list.)"

    show annika laugh
    annika "Anyways, what's your plan for the day?"
    player "Um, I need to check out the neighborhood coffee shop."
    annika "Cool! Let's catch up sometime and get coffee."
    player "Sure! Chat later!"
    hide annika

    call save_reminder from _call_save_reminder_1

label stage4:
    scene bg cafe with fadehold
    player smile "I'm glad that this coffee shop happens to need a part-time barista."
    player "Now at least I have some pocket money for necessities."
    player "This reminds me so much of college. I used to work part-time as a barista at the school library cafe as well."
    player "It was always nice to see my peers socializing and doing work at the cafe."
    player "An additional perk is that I get first-hand knowledge of interesting things happening on campus."
    player "That might also be true for this place. Looking around, I see quite a few people with their laptops."
    player "It's totally possible that some of them are working on the next million-dollar startup."
    player "Not impossible given that the tech scene is booming in our quiet little town."
    player "Or at least they might be talking about something interesting happening in the tech industry."

    show girl flipped red at left
    show boy orange at right
    girl "Hey hey! Did you hear that our school is getting a computer club?"
    boy "Wow. Really? What would you do at a computer club? Play video games?"
    girl "Well that and more – we can code stuff, maybe build a video game ourselves!"
    girl "I heard that we'll have a dedicated teacher to lead the club. They'll even host hackathons and stuff."
    boy "Hmmm, what are hackathons for?"
    girl "You know, like a marathon, but you hack away at some project instead of running around."
    boy "That sounds like fun. Do you have any project ideas already?"
    girl "Ummm... Do you know about this thing called a visual novel game?"
    boy "Tell me about it."
    girl "Okay here goes..."
    hide girl
    hide boy

    player surprised "Oops. I wasn't intentionally eavesdropping on high school kids, but the {b}hackathon{/b} idea they mentioned is new."
    player happy "I think I can use this piece of information to my advantage. Let's make it a To-Do item to ask Annika if she knows about events like this."

    $ todo_list.add_todo(todo_ask_hackathon)
    $ topics_to_ask.add('Hackathon')
    player "Alright! Going back to my shift."

    $ add_achievement(plot_barista_discover)

    # player goes back home
    scene bg bedroom night with fadehold
    player relieved "Phew... It's been a long day at work."

    scene bg laptop_screen night with dissolve
    player neutral "Let's check out the awesome resource that Annika was talking about."

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
            player pout "Hmmm... What even is web design? And I'm not a design person... Will I be able to follow along?"
            player "Maybe let's look some more?"
            jump stage5_choose_curriculum

        "JavaScript Algorithms and Data Structures":
            player pout "I remember hearing about JavaScript. Or wait, maybe that's Java."
            player "What are algorithms and data structures? That sounds like math, which is not my favorite subject."
            player "What other curriculum options do I have?"
            jump stage5_choose_curriculum

        "Front End Development Libraries" :
            player pout "Front end development? That sounds so complicated."
            player "Maybe I should go for some beginner topics?"
            jump stage5_choose_curriculum

        "Data Visualization":
            player pout "I know there's a lot of hype about big data, but can I really do that without a Ph.D.?"
            player "This doesn't look like it's for me."
            jump stage5_choose_curriculum

        "Back End Development and APIs":
            player pout "Back end, front end. What are the differences? They definitely sound like they should go together."
            player "But I don't have the time or energy to learn both..."
            player "Let's look for something simpler."
            jump stage5_choose_curriculum

        "Quality Assurance":
            player pout "Quality assurance? That sounds like I'll be on a digital conveyor belt making sure all cookie packs weigh more or less the same."
            player happy "Nice, warm, and chewy cookies... I love cookies. Hope mom still keeps some in the kitchen cookie jar."
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
            player pout "But I don't know anything about Python. Plus, I didn't do a lot of math in college."
            player "That's probably too hard for me right now."
            player "Let's find something else."
            jump stage5_choose_curriculum

        # "Information Security":
        #     player pout "What can I do after learning about information security?"
        #     player "Hack into others' computers? Stop attackers from hacking into other people's computers?"
        #     player "That sounds pretty intense. I'm not sure if I can handle that."
        #     player "Is there something more neutral on the list?"
        #     jump stage5_choose_curriculum

        "Machine Learning with Python":
            player happy "Machine Learning. Wow. That sounds cool."
            player "I'm really interested in teaching machines to learn."
            player "Just think about it. Teaching machines to chat like humans. Wow."
            player "No wonder everyone is hyped about Artificial Intelligence these days."
            player "..."
            player pout "But it looks hard. I know nothing about machine learning, except that there are so many memes about how machine learning is nothing but math."
            player "Math... linear algebra... that kind of thing."
            player "That's probably out of my league."
            player "Maybe I should start with something more basic?"
            jump stage5_choose_curriculum

        "Let's just wait until tomorrow and ask Annika for advice":
            player pout "Hmmm... I don't know. They all look equally hard. Let's ask Annika for advice tomorrow."
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
    mom "Hey honey, taking a break from all the studying?"
    mom "Your dad and I are really glad that you're continuing to learn new things after college, but don't push yourself too hard, okay?"
    player happy "Haha thanks Mom. I'm doing just fine."
    player "I'm just deciding on what CS topic to learn so I can get a job in tech like Annika."
    mom "Alright, know that we are always here if you'd like to talk or anything."
    player "I will. Thanks Mom."

    scene bg bedroom night with blinds
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
    $ renpy.show_screen('player_stats_todo_screen', _layer='transient', show_todo=True)
    player happy "Right. Let's give Annika a call and ask about the CS curriculum."
    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    hide smartphone

    show annika neutral

    player happy "Morning Annika!"
    annika @ laugh "Morning! As energetic as ever, I see."
    player "Haha all thanks to you!"
    annika "What's up?"
    player "So I've been checking out [freeCodeCamp] as you suggested."
    player "I think its curriculum looks solid."
    player pout "The thing is, I have no idea what to learn. Web dev, data science, machine learning..."
    player "They all look super complicated. I bet you put in a lot of hard work to finish each certification."
    player "Which one did you do, by the way?"

    annika "Oh, I did the web design one. What was it? {a=https://www.freecodecamp.org/learn/responsive-web-design/}Responsive Web Design{/a}?"
    annika "If I remembered anything from my college CS minor, it's those web markup languages."
    player "Ahh I see."
    player pout "(So Annika managed to pull through the curriculum because she had some experience from college. Plus she has a real gift for design.)"
    player worry "(I'm not like that... There's no way I can do this...)"

    annika "Hey [player_name], don't get discouraged, okay?"
    annika "It's already a big step forward now that you've checked out their curriculum!"

    show annika serious
    annika "Trust me, I was just like you when I first started."
    annika "I was clueless, so I reached out to [freeCodeCamp]'s online community."
    annika "They recommended that I start with some general introduction to computer science quizzes on a site named [developerquiz]."
    annika "I found those bite-sized quizzes fun and easier to digest."
    annika "Plus these quizzes cover a lot of fundamental CS knowledge. You can think of it as an intro curriculum to CS for complete noobs."
    annika "How does that sound?"

    player worry "Ehh... Even that, I'm not sure if I can make it through all the quizzes and CS concepts on my own..."
    player pout "What if I run into something that I can't understand?"
    player worry "What if the quizzes get too hard like they always do at college, and I lose my motivation?"

    show annika neutral
    annika "That's totally okay! In fact, what I love about [freeCodeCamp] is that they have an entire community that can help you out and cheer you on."
    show annika laugh
    annika "And I can be your go-to accountability buddy as well! Ping me anytime if anything comes up."
    player happy "Thanks Annika. I know I can count on you."
    annika "Any time!"

    show annika neutral
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

    scene bg cafe with fadehold
    play sound 'audio/sfx/cafe_pour.wav'
    show coffee at truecenter
    pause 5
    hide coffee

    player neutral "I don't see too many people in the cafe today. Maybe because it's a work day?"

    scene bg cafe dusk with fadehold
    play sound 'audio/sfx/cafe_pour.wav'
    show coffee at truecenter
    pause 5
    hide coffee
    player "That's about it for my shift. Not much happened."
    player "Let's head home early to squeeze in some studying tonight, just to keep up the momentum."

label stage6:
    # Stage 6. Trials
    call screen text_over_black_bg_screen(_("{i}Chapter 3: Let's hit the books!{/i}"))

    scene bg bedroom dusk with fade
    player smile "I'm finally home! Let's head over to [developerquiz] and try out some quiz questions."
    scene bg laptop_screen with dissolve
    player surprised "Looks like they even divided the questions into subcategories like HTML, CSS, and JavaScript."

    $ stats_subcategory_unlocked = True
    $ renpy.show_screen('player_stats_todo_screen', _layer='transient')

    player smile "Well, guess I need to track my progress for each subcategory."
    "(Your {b}CS Knowledge{/b} is calculated as the average of all subcategories. So make sure to study for each of the categories!)"
    player "For each session, I'll need to complete four multiple choice questions from the chosen category."
    player happy "Let's give it a go!"

    call study_session_choose_topic from _call_study_session_choose_topic_2
    call study_session from _call_study_session

    $ add_achievement(milestone_start_curriculum)

    scene bg bedroom night with dissolve
    player neutral "Phew... I'm finally done with these questions. What a day..."
    player pout "I think I did okay, but I do feel tired after a long day at work."
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
    player happy "Morning, mom. Morning, dad."
    dad "Morning, pumpkin."
    mom "Morning, honey. Did you sleep well?"
    player laugh "Yep. I'm recharged for a new day."
    dad "That's great. Let's start the morning with a nice family breakfast."

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

    player happy "That's about it for the morning. I feel like I'm much more productive if I can focus on one thing for an entire day."
    player "Let's alternate between working whole-day shifts and spending whole days studying."
    player "I can call Annika this afternoon when she's done with her work. It'll be good to chat and ask her about things."

    scene bg bedroom dusk with fadehold

    show smartphone at truecenter
    play sound "<to 2.0>audio/sfx/phone_ring.wav"
    play sound "<to 2.0>audio/sfx/phone_dial_tone.wav"
    pause 2.0
    hide smartphone

    show annika
    pause 1.0
    player smile "Hey Annika! Is now a good time to talk?"

    show annika laugh
    annika "Heyya [player_name]! Now's perfect. I just got back from work."
    annika "How did your first day of studying go?"
    player "I felt pretty productive today. It's nice how the quiz questions give you instant feedback."
    player happy "What about your day? How was work?"
    annika "It went well! I'm learning to use the custom web dev framework that my company uses."
    annika "It's pretty different from what I've been using in my own projects, and a little confusing at times, but my colleagues say it gets better with practice."
    player "That sounds like fun!"

    show annika neutral
    annika "Yeah! And I've heard good things about this framework. Mostly from people I ran into at the local Hacker Space."
    annika "It looks like a popular tool for people who want to test out project ideas at hackathons."
    player neutral "({b}Hackathons{/b}! That reminds me, I should probably ask Annika about this topic.)"
    player "(And she also just mentioned something called a {b}Hacker Space{/b}. That's something worth asking about as well.)"

    show annika laugh
    annika "Hello? Earth to [player_name]?"
    player happy "Haha no worries I'm here. Just wondering about something."

    show annika neutral
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
    annika "Whelp, I guess you must be tired after a day's studying. Enjoy a relaxing evening!"
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

    scene bg bedroom night with blinds
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
    player happy "Hey Annika. You're up early."
    annika "Yeah! Told you we are going to check out the Hacker Space together."
    annika "You ready for the ride?"
    player laugh "Yes! Lead the way."

    scene bg hacker_space with slideright
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

    scene bg bedroom night with slideright
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
    call screen text_over_black_bg_screen(_('{i}Chapter 4: A mentor to lead the way!{/i}'))

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
            marco "If you are looking for a one-word answer, then it's “learning.” Everyone else I know will probably give you the same answer if you ask."
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

    scene bg bedroom night with slideright
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
    $ renpy.show_screen('player_stats_todo_screen', _layer='transient')
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

    show annika neutral
    annika "They could use some volunteers to help out."
    annika "Wanna come with me to check it out today?"
    player @ laugh "Sounds good! See you in a bit!"

    scene bg hacker_space with slideright
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
    player surprised "And energy!"
    annika "That too! Mentoring kids looks like fun. I hope one day I get to do that, too."
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

    show annika neutral
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

    scene bg bedroom night with slideright
    player relieved "I feel like I've learned so much about the coding interview process from Annika today."
    player laugh "So much that I can't wait to wrap up my curriculum and jump in to see what a real coding interview is like!"
    player smile "I heard that [developerquiz] will send an email notification to people who have made significant progress in their curriculum."
    player "Let's check to see my progress."
    if player_stats.player_stats_map['CS Knowledge'] < cs_knowledge_threshold:
        player "Hmmm... I think I still need to ramp up more on my CS knowledge. I'll get back to studying tomorrow."
        "(Try bumping your {b}CS Knowledge{/b} to above [cs_knowledge_threshold] by completing more quizzes.)"

    while player_stats.player_stats_map['CS Knowledge'] < cs_knowledge_threshold:
        call day_start from _call_day_start_6
        call day_activity_choices from _call_day_activity_choices_6

    call save_reminder from _call_save_reminder_12

    # once we are down here, we should have player_stats.player_stats_map['CS Knowledge'] >= cs_knowledge_threshold
    player laugh "Looks like I've made quite a bit of progress! I wonder when I can expect to receive that email."
    player "But let's first have a movie night to celebrate what I've gotten done!"

    scene bg bedroom with fadehold
    $ renpy.show_screen('player_stats_todo_screen', _layer='transient')

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
    call screen text_over_black_bg_screen(_("{i}Chapter 5: Let's crush those interviews!{/i}"))

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

    scene bg bedroom night with fadehold
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
            "(Does it feels like time is flying by without your doing much?)"
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
    call screen text_over_black_bg_screen(_("{i}Chapter 6: Let's meet my new colleagues!{/i}"))

    $ calendar.next_month() # player's start date is in a month
    # TODO: maybe in v2
    # $ player_stats.set_stats('Developer Skill', 0)

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

label ending:
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

    $ quick_menu = False
    $ calendar_enabled = False
    play sound 'audio/sfx/cartoon_suspense.wav'
    scene black with dissolve
    pause 1
    show text _("{bt}{size=48}{color=[white]}{i}Well, that's another chapter that we will bring to you in the future!{/i}{/color}{/size}{/bt}") with dissolve
    pause 3
    hide text with dissolve

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
