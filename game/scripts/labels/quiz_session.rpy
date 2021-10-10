label study_session:
    # correct choices increments CS knowledge
    $ timeout_label = None # no time limit
    $ num_questions = 4 # ask 4 questions each time
    $ num_correct = 0
    while num_questions > 0:
        if num_questions == 4:
            player neutral "First question."
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

label interview_session:
    # ask 3 - 6 questions each time
    # to pass, must have more than 80 percent correct
    # and then 0.6 chance of hearing back with an offer in 1 - 3 days
    $ num_questions = 4
    $ num_correct = 0

    $ timeout_label = 'interview_one_question'
    $ timeout = 180.0 # three minutes for each question

    while num_questions > 0:
        call interview_one_question

label interview_one_question:
    $ num_questions -= 1
    $ quiz_question = renpy.random.choice(interview_questions)
    if quiz_question.code_label is not None:
        show screen example(quiz_question.code_label)

    # result is True or False
    $ result = renpy.display_menu(quiz_question.choices)
    hide screen example

    if result == True:
        $ num_correct += 1

    with dissolve
    return