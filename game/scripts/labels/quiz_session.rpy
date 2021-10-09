label study_session:
    # correct choices increments CS knowledge
    # ask 4 questions each time
    $ num_questions = 4
    $ num_correct = 0
    while num_questions > 0:
        if num_questions == 4:
            player neutral "First question. Three more to go!"
        elif num_questions == 3:
            player neutral "Second question. Halfway through!"
        elif num_questions == 2:
            player neutral "Third question. Almost there!"
        elif num_questions == 1:
            player neutral "Last question. Hang in there!"

        $ num_questions -= 1

        window hide
        # see cs_questions.rpy
        $ quiz_question = renpy.random.choice(general_questions)
        if quiz_question.code_label is not None:
            show screen example(quiz_question.code_label)

        # result is True or False
        $ result = renpy.display_menu(quiz_question.choices)
        hide screen example

        if result == True:
            $ num_correct += 1
            $ player_stats.change_stats('CS Knowledge', 5)
            player happy "Correct!"
        else:
            with vpunch
            player confused "Wrong..."

    with hpunch
    player neutral "All done!"

    return