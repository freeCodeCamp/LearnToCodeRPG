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
    hide screen player_stats_screen
    return