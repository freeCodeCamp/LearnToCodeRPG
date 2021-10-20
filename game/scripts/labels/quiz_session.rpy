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

        # display question
        $ renpy.say(None, quiz_question.question, interact=False)
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

    $ timeout_label = 'interview_session_questions'
    $ timeout = 180.0 # three minutes for each question

    # fall through to the next label

label interview_session_questions:
    while num_questions > 0:
        if num_questions == 4:
            interviewer "Here's the first question."
        elif num_questions == 1:
            interviewer "Last question."
        else:
            interviewer "Next question."
        call interview_one_question from _call_interview_one_question

    interviewer "Thanks for taking your time. We will be in touch about next steps."
    player "Hmmm... I heard that you might be allowed to ask about your performance on the interview. Shall I do that?"

    $ timeout_label = None
    menu:
        "Shall I ask about how I did on the interview and get feedback?"
    
        "There's no harm in asking, right?":
            player "Emm... Excuse me. How did I do? May I ask for some feedback so I can improve next time?"
            if renpy.random.random() > 0.5:
                interviewer "Sorry. We don't provide feedback after interviews."
            else:
                interviewer "From my opinion you did okay. Just keep doing what you are doing."
    
        "Let's not do that and ruin my chance of getting an offer":
            pass

    # check results
    if num_correct > num_questions * 0.8:
        # coin flip
        if renpy.random.random() > 0.2:
            $ renpy.notify("This is a debug message to let you know that you've gotten an offer")
            $ days_before_offer = renpy.random.randint(2, 4)
            # TODO: this must be buggy lol
            $ offer_company_name = interview_company_name

    return

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