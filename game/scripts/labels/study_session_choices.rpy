label study_session_choices:
    # correct choices increments CS knowledge
    # ask 4 questions each time
    $ num_questions = 4
    $ num_correct = 0
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
        $ quiz_question = renpy.random.choice(general_questions)
        if quiz_question.code_label is not None:
            show screen example(quiz_question.code_label)

        # result is True or False
        $ result = renpy.display_menu(quiz_question.choices)

        if result == True:
            $ num_correct += 1
            $ player_stats.change_stats('CS Knowledge', 5)
            player happy "Correct!"
        else:
            player confused "Wrong..."

        hide screen example

    player "All done!"

    return