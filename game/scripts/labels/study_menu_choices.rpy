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