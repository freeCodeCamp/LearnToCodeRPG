# need to set npc and npc_sprite before calling these labels

label npc_conversation_start:
    $ renpy.show(npc_sprite) # Annika or Marco
    player smile "Hello!"
    npc "Hey [player_name]! What's up?"
    player "Well, I learned some tech buzzwords and would like to learn more about them."
    npc "Sure, what would you like to know?"

    $ label = None
    while label != 'done':
        $ choices = [(topic, ask_npc[topic]) for topic in topics_to_ask]
        $ choices.append(("That's all", 'done'))
        $ label = renpy.display_menu(choices)
        if label != 'done':
            $ renpy.call(label=label)
            # no need to discard the asked topic here since it's discarded inside each label
            npc "Anything else?"

    player "That's all I need to know. Thanks!"
    npc "No problem. Have a good night!"
    player "You as well!"
    play sound 'audio/sfx/phone_hangup.wav'
    $ renpy.hide(npc_sprite)

    if not plot_buzzword_ask in persistent.achievements:
        $ add_achievement(plot_buzzword_ask)

    return

label npc_choose_question:
    

label ask_hackathon:
    # use `discard` instead of `remove` to prevent the exception in case the player rolls back
    $ topics_to_ask.discard('Hackathon')
    player "What is a hackathon?"
    npc "It's an event where people come together to design and implement cool tech projects."
    npc "Hackathons aren't usually too long. Most last for one or two days. Now imagine people hacking away at their laptops overnight! You get the idea."
    npc "People usually form small teams to collaborate. It's especially cool when the team consists of people with different expertise, not just software engineers, but graphic designers and product managers as well."
    npc "It's a great way to brainstorm, prototype, and test out ideas that might one day evolve into full-fledged products."
    player "That sounds cool!"
    npc "Yeah! I've only been to one or two of them, but my company has those seasonal innovation events that I'll be checking out soon."
    npc "You should go to some hackathons as well! You'll learn to collaborate with other developers and even designers."
    npc "Plus, hackathon projects look great on your résumé."
    player "Cool! But how do I find hackathon events?"
    npc "Just search online! You might be surprised by the number of hackathons happening locally near you."
    player "That's awesome! I'll check that out when I get a bit better at coding."

    # TODO: todo_list.add_todo('Try out hackathons'), needs more writing
    player "(Hmmm, so that's what a {b}hackathon{/b} is about.)"
    $ todo_list.complete_todo(todo_ask_hackathon)
    player "Checked it off my To-Do."
    return

label ask_fullstack:
    $ topics_to_ask.discard('Full-Stack')
    player "What is a full-stack developer?"
    npc "A full-stack developer usually refers to a full-stack web developer. It's a role for people who can develop both client and server software."
    npc "You might have heard about front-end and back-end already. Full-stack is front-end and back-end put together."
    npc "Front-end is synonymous with client software, or User Interface (UI). It refers to the appearance of the application we are using."
    npc "Like the layout of a website."
    npc "Back-end is synonymous with server software, or the logic. Like how the database remembers your information on a e-shopping website."
    npc "Again, put front-end and back-end together and you have full-stack!"
    player "Wow. Then a full-stack developer must be a real jack-of-all-trades."
    npc "Exactly! If that's something you'd like to learn more about, check out the courses on [freeCodeCamp]!"
    player "I'll do that, thanks!"

    # TODO: add glossary
    player "(Hmmm, so that's what {b}full-stack{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'Full-Stack')
    player "Checked it off my To-Do."
    return

label ask_machinelearning:
    $ topics_to_ask.discard('Machine Learning')
    player "What is Machine Learning?"
    npc "By definition, Machine Learning is a method of data analysis that automates analytical model building."
    npc "Basically, our goal is to build a model based on the data we observe."
    npc "The model can be a regression model, meaning that it can give estimates. For example, we can build a regression model that estimates the price of a house based on the house's location, layout, etc."
    npc "The model can also be a classification, like classifying cats versus dogs."
    player "Wow..."
    npc "I know. Amazing, isn't it?"
    npc "Machine Learning requires a lot of mathematical knowledge. You need to be familiar with linear algebra, calculus, and so on."
    player "That sounds intense, but really cool!"
    npc "Remember that [freeCodeCamp] has resources if you'd like to get started with Machine Learning."
    npc "You can build a lot of cool projects with Machine Learning. How about {a=https://www.freecodecamp.org/news/discord-ai-chatbot/}a chatbot that speaks like your favorite character{/a}?"
    player "Sounds awesome! Thanks for sharing!"

    player "(Hmmm, so that's what {b}machine learning{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'Machine Learning')
    player "Checked it off my To-Do."
    return

label ask_conference:
    $ topics_to_ask.discard('Conference')
    player "What is a tech conference?"
    npc "Tech conferences are places for developers to gather and learn about the cutting-edge advances in the field of software."
    npc "There are usually talks given by speakers who are subject experts in their respective fields."
    npc "There may also be booths and demo sessions for people to show off their ideas and prototypes."
    npc "Sometimes there are career fairs where companies try to recruit conference attendees. Make sure to bring your résumé if you're interested."
    player "What are those conferences about? Tech sounds like a huge field."
    npc "Conferences usually have more specific topics. For example, there could be conferences for game developers, for web developers, or for developers who work with a particular programming language like Python or Java."
    player "Sounds like a lot of fun!"
    npc "Yep. Some companies even sponsor their employees to attend annual conferences so they can keep their skills up-to-date."
    npc "Search for local conferences around you if you are interested!"
    player "I sure will!"

    player "(Hmmm, so that's what a tech {b}conference{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'Conference')
    player "Checked it off my To-Do."
    return

label ask_versioncontrol:
    $ topics_to_ask.discard('Version Control')
    player "What is version control?"
    player "(And why should I care?)"
    npc "That's a great question to ask. Let me tell you what version control is, and, yes, why you should care."
    player "!"
    player "(Ehhh... I guess I had why-bother written all over my face...)"
    npc "By definition, version control is the practice of tracking and managing changes to software code."
    npc "Version control systems are software tools that help software teams manage changes to source code over time."
    npc "Examples include Git, which is the most popular modern one."
    npc "Some companies that have been in the industry for a while might also use older version control software like Subversion (SVN), Perforce, and so on."
    player "And why should I care?"
    npc "Well, version control can be your life saver when you find a bug in your code."
    npc "For example, what do you do when a new change you've made broke the existing tests?"
    npc "As a starter, you can try reverting to the previous working version where the tests were still passing and debug from there."
    player "That sounds pretty useful."
    npc "Version control is pretty useful. You should definitely understand it to increase your developer output."
    player "Thanks for the tip!"

    player "(Hmmm, so that's what {b}version control{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'Version Control')
    player "Checked it off my To-Do."
    return

label ask_devops:
    $ topics_to_ask.discard('DevOps')
    player "What is DevOps?"
    npc "By definition, DevOps is the combination of cultural philosophies, practices, and tools for better software delivery."
    npc "Some of its core principles include Continuous Improvement and Automate Everything You Can."
    player "Wow. The automation one sounds pretty extreme."
    npc "Well, if you can, automation saves a lot of time and effort!"
    npc "DevOps is a big subject, and I highly recommend reading about it online if you're interested."
    npc "Just remember it's not just a job title, but more of a mindset."
    player "Alright, I'll do my own research. Thanks."

    player "(Hmmm, so that's what {b}DevOps{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'DevOps')
    player "Checked it off my To-Do."
    return

label ask_agile:
    $ topics_to_ask.discard('Agile')
    player "What is agile development?"
    npc "The definition might be boring but here it goes: Agile is an iterative approach to project management and software development."
    npc "Teams work in fast iterations, deliver frequent builds, and receive frequent feedback in order to build better software."
    npc "The software requirements, plans, and results are evaluated continuously so teams have a tight feedback loop."
    npc "Some people call agile a methodology, but to me, it's more like a mindset."
    player "Fail fast, fail often?"
    npc "Exactly. And that's how you improve."
    player "Haha I can see how this mindset is helpful in lifelong learning. That's awesome."

    player "(Hmmm, so that's what {b}agile{/b} development is about.)"
    $ todo_list.complete_todo(todo_ask + 'Agile')
    player "Checked it off my To-Do."
    return

label ask_api:
    $ topics_to_ask.discard('API')
    player "What is an API?"
    player "(And why is everyone going around using those three-letter acronyms?)"
    npc "API stands for application programing interface."
    npc "It is a software intermediary that allows two applications to talk to, or interface, with each other."
    npc "For example, say a weather organization provides an API for the weather report."
    npc "You may build a website to display weather reports by contacting their API."
    npc "The weather app built into your phone might also use the exact same API as its data source."
    npc "So this one weather API can be used by anyone and any application to communicate the state of the weather."
    npc "For a three-letter acronym, API is quite a mouthful to explain, huh?"
    player "Yeah... but I think I get the idea now."

    player "(Hmmm, so that's what an {b}API{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'API')
    player "Checked it off my To-Do."
    return

label ask_userexperience:
    $ topics_to_ask.discard('User Experience')
    player "What is User Experience?"
    npc "Thinking ahead of just writing code, aren't you? You might have it in you to become a product manager!"
    player "(Uh, thanks, I guess?)"
    npc "User Experience, commonly abbreviated UX, is how a user interacts with and experiences a product, system or service."
    npc "It includes a person's perceptions of utility, ease of use, and efficiency."
    npc "We might say a website has poor user experience when it has poor usability or presentation."
    npc "For example, a news website has poor user experience if new articles are scattered all over the site. You as a user won't be able to find anything you are looking for there."
    npc "But fear not, we have User Experience Design that'll come to the rescue."
    npc "There are time-tested UX flows and templates designed to make an application clean and crisp."
    player "(Hmmm... have I encountered any sites that have either really great or really bad user experience?)"
    npc "My turn to ask a question. What do you think about the user experience of [freeCodeCamp]?"

    menu:
        "What do you think about the user experience of [freeCodeCamp]?"
    
        "So far so good!":
            npc "That's what I think as well. You can maybe learn something by navigating through their site and taking notes."

        "Needs work!":
            npc "Whelp, they always welcome feedback from the community. So do let them know!"

    player "Will do!"

    player "(Hmmm, so that's what {b}User Experience{/b} is about.)"
    $ todo_list.complete_todo(todo_ask + 'User Experience')
    player "Checked it off my To-Do."
    return
