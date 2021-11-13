# ask Annika

label ask_annika_hackathon:
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
    # TODO: refactor and add to topics_to_ask
    $ todo_list.complete_todo(todo_ask_hackathon)
    return

label ask_annika_fullstack:
    player "What is a full-stack developer?"
    annika "A full-stack developer usually refers to a full-stack web developer. It's a role for people who can develop both client and server software."
    annika "You might have heard about front-end and back-end already. Full-stack is front-end and back-end put together."
    annika "Front-end is synonymous with client software, or, User Interface (UI), the appearance of the application we are using."
    annika "Like the layout of a website."
    annika "Back-end is synonymous with server software, or, the logic. Like how the database remembers your information on a e-shopping website."
    annika "Again, put front-end and back-end together and you have full-stack!"
    player "Wow. Then a full-stack developer must be a real jack-of-all-trades."
    annika "Exactly! If that's something you'd like to learn more about, check out the classes on [freeCodeCamp]!"
    player "I'll, thanks!"

    # TODO: add glossary
    return

label ask_annika_devops:

label ask_annika_conference:

label ask_annika_versioncontrol:

# ask Marco

label ask_marco_machinelearning:

label ask_marco_agile:

label ask_marco_api:

label ask_marco_userexperience: