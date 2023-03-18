init python:
    from supermemo2 import SMTwo

label bonus_quiz_entry_label:
    scene bg laptop_screen with dissolve
    "Welcome to the quiz practice mode. Here you can practice questions with spaced repetition."
    $  timeout_label = None # no time limit

    python:
        questions_to_review = []
        for question in persistent.all_quiz_questions:
            if question.spaced_repetition is None:
                questions_to_review.append(question)
            else:
                if question.spaced_repetition.review_date <= date.today():
                    questions_to_review.append(question)

    $ num_questions = len(questions_to_review)
    "Today you have [num_questions] questions to review."

    while questions_to_review:
        $ quiz_question = questions_to_review.pop()

        # display question
        $ renpy.say(None, quiz_question.question, interact=False)
        # result is True or False
        $result = renpy.display_menu(quiz_question.choices)

        if result == True:
            "Correct!"
            $ value = 5 # perfect response
        else:
            "Wrong..."
            $ value = 0 # complete blackout

        python:
            if question.spaced_repetition is None:
                question.spaced_repetition = SMTwo.first_review(value)
            else:
                question.spaced_repetition = question.spaced_repetition.review(value)
            print(question.spaced_repetition.review_date)

        # show the correct answer and explanation using a viewport
        call screen quiz_question_answer_explanation_screen(quiz_question)
