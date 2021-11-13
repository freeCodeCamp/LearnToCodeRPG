# need to set npc and npc_sprite before calling these labels

label npc_conversation_start:
    show npc_sprite
    # TODO: play sound of typing
    player "Hello!"
    npc "Hey [persistent.player_name]! What's up?"
    player "Well, I heard some tech buzzwords and would like to learn more about them."
    npc "Sure, what would you like to know?"
    $ choices = [(topic, ask_npc[topic]) for topic in topics_to_ask]
    $ label = renpy.display_menu(items=choices)
    $ renpy.call(label=label)
    # remove the asked topic
    $ topics_to_ask.remove(ask_npc_label_to_topic[label])

    player "That's all I need to know. Thanks!"
    npc "No problem. Have a good night!"
    return

label ask_hackathon:
    player "What is a hackathon?"
    npc "It's a event where people come together to design and implement cool tech projects."
    npc "Hackathons aren't usually too long. Most lasts for one or two days. {w}Now imagine people hacking away at their laptops overnight! You get the idea."
    npc "People usually form small teams to collaborate. It's especially cool when the team consists of people with different expertise, not just software engineers, but graphic designers and product managers as well."
    npc "It's a great way to brainstorm, prototype, and test out ideas that might one day evolve into full-fledged products."
    player "That sounds cool!"
    npc "Yeah! I've only been to one or two of them, but my company has those seasonal innovation events that I'll be checking out soon."
    npc "You should go to some hackathons as well! You will learn to collaborate with other developers and even designers."
    npc "Plus, hackathon projects look great on your resume."
    player "Cool! But how do I find hackathon events?"
    npc "Just search online! You might be surprised by the number of hackathons happening locally near you."
    player "That's awesome! I'll check that out when I get a bit better at coding."

    # TODO: todo_list.add_todo('Try out hackathons'), needs more writing
    # TODO: refactor and add to topics_to_ask
    $ todo_list.complete_todo(todo_ask_hackathon)
    return

label ask_fullstack:
    player "What is a full-stack developer?"
    npc "A full-stack developer usually refers to a full-stack web developer. It's a role for people who can develop both client and server software."
    npc "You might have heard about front-end and back-end already. Full-stack is front-end and back-end put together."
    npc "Front-end is synonymous with client software, or, User Interface (UI), the appearance of the application we are using."
    npc "Like the layout of a website."
    npc "Back-end is synonymous with server software, or, the logic. Like how the database remembers your information on a e-shopping website."
    npc "Again, put front-end and back-end together and you have full-stack!"
    player "Wow. Then a full-stack developer must be a real jack-of-all-trades."
    npc "Exactly! If that's something you'd like to learn more about, check out the classes on [freeCodeCamp]!"
    player "I'll, thanks!"

    # TODO: add glossary
    return

label ask_devops:

label ask_conference:

label ask_versioncontrol:

label ask_machinelearning:

label ask_agile:

label ask_api:

label ask_userexperience: