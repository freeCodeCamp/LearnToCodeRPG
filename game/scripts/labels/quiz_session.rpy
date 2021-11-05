## study session in daily activity choices
label study_session:
    scene bg laptop_screen with dissolve

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
        $ quiz_question = renpy.random.choice(study_session_questions)
        if quiz_question.code_label is not None:
            show screen example(quiz_question.code_label)

        # display question
        $ renpy.say(None, quiz_question.question, interact=False)
        # result is True or False
        $ result = renpy.display_menu(quiz_question.choices)
        hide screen example

        if result == True:
            $ num_correct += 1
            $ player_stats.change_stats('CS Knowledge', 3)
            player happy "Correct!"
        else:
            with vpunch
            player pout "Wrong..."
            # show the correct answer and explanation using a viewport
            call screen quiz_question_answer_explanation_screen(quiz_question)

        # hide player stats screen if it was showing so it doesn't obstruct the questions
        hide screen player_stats_screen

    play sound 'audio/sfx/quiz_complete.wav'
    pause 0.5
    player neutral "All done!"

    return

## hacker space trivia session
label trivia_session:
    $ num_questions = len(trivia_questions)
    $ num_correct = 0

    $ timeout_label = 'trivia_session_questions'
    $ timeout = 30.0 # 30 seconds for each question

    # fall through to the next label

label trivia_session_questions:
    while num_questions > 0:
        if num_questions == len(trivia_questions):
            trivia_guy "Here's the first question."
        elif num_questions == 1:
            trivia_guy "Last question."
        else:
            trivia_guy "Next question."
        call trivia_one_question

    # check results
    trivia_guy "Now let's check the results."
    play sound 'audio/sfx/hacker_space_trivia_evaluate.wav'
    trivia_guy "...{w=0.5}...{w=0.5}...{w=0.5}"
    if num_correct == len(trivia_questions):
        trivia_guy "Could this be...?"
        play sound 'audio/sfx/hacker_space_trivia_win.wav'
        trivia_guy "You are the first person to get everything correct! Congratulations!"
        $ player_stats.change_stats('Dev Trivia', 20)
        trivia_guy "Now about the award..."
        show business_card at truecenter with zoomin
        trivia_guy "I'm actually a talent recruiter at {b}CupcakeCPU™{/b}. Feel free to apply to our roles. We welcome talent like you."
        hide business_card
        trivia_guy "Until next time!"
        hide trivia_guy with dissolve
        player "Uhhh... cool? I guess?"
        player "Let's add it to my To-Do list to apply to their company once I'm comfortable with my skill level."
        $ todo_list.add_todo(todo_apply_cupcakecpu)
        $ has_won_hacker_space_trivia = True

    else:
        trivia_guy "You missed some of the questions there, but it was close."
        trivia_guy "Better luck next time. I'll be here waiting."

    return

label trivia_one_question:
    $ num_questions -= 1
    $ quiz_question = trivia_questions[num_questions]
    if quiz_question.code_label is not None:
        show screen example(quiz_question.code_label)

    # display question
    $ renpy.say(None, quiz_question.question, interact=False)
    # result is True or False
    $ result = renpy.display_menu(quiz_question.choices)
    hide screen example

    if result == True:
        $ num_correct += 1

    with dissolve
    return

## coding interview session
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

    # display question
    $ renpy.say(None, quiz_question.question, interact=False)
    # result is True or False
    $ result = renpy.display_menu(quiz_question.choices)
    hide screen example

    if result == True:
        $ num_correct += 1

    with dissolve
    return