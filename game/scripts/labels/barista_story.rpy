# events that happen when the player visit the cafe

label barista_fullstack:
    show woman red flipped at left
    show man blue at right
    female "So I heard that you've moved up to a new role? Congrats!"
    female "What do you do now?"
    male "Whelp, I'm now finally doing full-stack dev. Remember that I used to do front-end dev only? That got boring really fast..."
    player @ surprised "{b}Full-stack{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'Full-Stack')
    $ topics_to_ask.add('Full-Stack')
    return    

label barista_devops:
    show boy blue flipped at left
    show man red at right
    college_boy "Hey how's it going? Thanks so much for taking time out of your day to meet me!"
    male "No problem. I'm always happy to mentor college kids."
    college_boy "Haha thanks. Okay let's cut to the chase."
    college_boy "I'm really interested in getting a role in DevOps, is there any resource you'd recommend?"
    player @ surprised "{b}DevOps{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'DevOps')
    $ topics_to_ask.add('DevOps')
    return

label barista_machinelearning:
    show girl orange flipped at left
    show boy purple at right
    college_girl "Hey hey hey look at this cool thing we did for the course project!"
    college_girl "Give it a picture of a cat or a dog and it will be able to tell which is in the picture!"
    # TODO: this could actually be a minigame or the player's side project :D
    college_boy "That's cool! Did you use Machine Learning for that?"
    college_girl "Yeah! And there are a lot of new techniques that we can add onto this..."
    player @ surprised "{b}Machine Learning{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'Machine Learning')
    $ topics_to_ask.add('Machine Learning')
    return

label barista_conference:
    show woman blue flipped at left
    show girl blue at right
    college_girl "Ohh hey isn't that my favorite sister?"
    girl "... I'm your only sister."
    college_girl "Oh come on! I'm just trying to lighten up the mood a bit!"
    college_girl "Are you still nervous about going to the conference?"
    girl "... Well, yeah. I've never been to one before... I don't know what to do once I'm there..."
    college_girl "You'll be fine! Conferences are fun! There are talks, poster sessions, and even career fairs!"
    girl "Oh... That doesn't sound too bad. What exactly can I expect?"
    player @ surprised "A tech {b}conference{/b}... That sounds like a place for elite developers. I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'Conference')
    $ topics_to_ask.add('Conference')
    return

label barista_agile:
    show man red flipped at left
    show woman purple at right
    male "So your team is going fully agile?"
    female "Yeah! We had some agile coach coming in to boost our productivity."
    male "We had a coach as well. That was a smooth experience transitioning to a more modern way of developing software..."
    player @ surprised "{b}Agile{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'Agile')
    $ topics_to_ask.add('Agile')
    return

label barista_api:
    show girl purple flipped at left
    show boy red at right
    college_girl "Here's the requirements for this project."
    college_boy "Woah. We need to come up with our own APIs?"
    college_girl "Maybe. Or we can search online to see if there are public ones we can use."
    college_boy "That sounds like a good idea!"
    college_girl "Huh. Knowing you, anything that saves you efforts sounds like a good idea."
    college_boy "Ouch. Don't be so mean. I'm only doing this so we can avoid {bt}reinventing the wheel.{/bt}"
    college_girl "... Okay. Whatever you say. Let's get to work."
    player @ surprised "An {b}API{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'API')
    $ topics_to_ask.add('API')
    return

label barista_userexperience:
    show woman red flipped at left
    show boy orange at right
    female "Hey there. Nice to meet you!"
    female "You must be our new User Experience intern, right?"
    college_boy "Yes! It's my great pleasure to be on the team!"
    female "Good, good. Now tell me a bit about yourself. Why did you get into UX? What UX projects have you done?"
    college_boy "Sure! So it all started with this program at my school..."
    player @ surprised "{b}User Experience{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'User Experience')
    $ topics_to_ask.add('User Experience')
    return

label barista_versioncontrol:
    show girl red flipped at left
    show boy blue at right
    girl "Oh. {w}My. {w}God. {w}Did you just blow up our codebase?"
    boy "Oopsy."
    girl "'Oopsy' is all you can say? Our project deadline is tomorrow, you know!"
    boy "Relax, will you? We have version control, don't we?"
    girl "Uh. True."
    boy "Then problem solved. Let's just roll back."
    boy "And remember to thank the genius who first suggested that we set up version control."
    girl "... I'm not thanking you for breaking the code, you know."
    player @ surprised "{b}Version Control{/b}... What is that? I better take notes so I can learn more about it."
    $ todo_list.add_todo(todo_ask + 'Version Control')
    $ topics_to_ask.add('Version Control')
    return