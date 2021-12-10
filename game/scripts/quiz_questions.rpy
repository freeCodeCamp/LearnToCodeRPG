screen quiz_question_answer_explanation_screen(quiz_question):
    on "show" action With(dissolve)
    on "hide" action With(dissolve)

    frame:
        style_prefix "confirm"

        xfill True
        xsize 1200
        xmargin 50
        ypadding 30
        yalign .25
        background '#fffe'

        vbox:
            xfill True
            spacing 10

            label 'Question'
            text quiz_question.question

            null height 20
            label 'Correct answer'
            text '{b}[quiz_question.true]{/b}'

            null height 20
            if quiz_question.explanation:
                label 'Explanation'
                text quiz_question.explanation

            if quiz_question.learn_more_url:
                textbutton "{icon=icon-help-circle} " + _("Learn More"):
                    hovered Notify('Learn more about this topic in an article!')
                    action OpenURL(quiz_question.learn_more_url)

            null height 40
            textbutton "Gotcha! Let's move on.":
                xalign 0.5
                action Return()

init python:

    class QuizQuestion():
        '''
        question: a string
        true: a string
        false: a list of strings
        explanation: an optional string
        code_label: an optional string, see game/quiz_code_snippets.txt
        '''
        def __init__(self, question, true, false, explanation=None, 
            code_label=None, learn_more_url=None, easter_egg_name=None, difficulty=None):

            """
            tech trivia questions only have question, true, and false, so all other fields are optional
            """

            choices = {
            true: True
            }
            for f in false:
                choices[f] = False

            # a list of tuples
            # ex.
            '''
            [
            ("What is the binary representation of 10?", None),
            ("1010", True),
            ("0101", False),
            ],
            '''
            choices = []
            for f in false:
                choices.append((f, False))
            # shuffle insert the true answer
            # max is total num of choices, true plus false
            idx = renpy.random.randint(0, len(false) + 1)
            choices.insert(idx, (true, True))

            self.choices = choices

            self.true = true
            self.question = question
            self.explanation = explanation
            self.code_label = code_label
            self.learn_more_url = learn_more_url
            self.easter_egg_name = easter_egg_name
            self.difficulty = difficulty

    ## Hacker Space Tech Trivia
    trivia_questions = [
    QuizQuestion(
        question="Which is faster for training Neural Networks, a GPU or a CPU?",
        true="GPU.",
        false=[
        "CPU.",
        "They are the same."
        ]
        ),
    QuizQuestion(
        question="Which of the following is a legal identifier in assembly language?",
        true="july_2021",
        false=[
        "10percent",
        "a1a2a3...a247a248",
        "eflags"
        ]
        ),
    QuizQuestion(
        question="Who was the child of a famous poet and English mathematician whom many historians consider the first programmer?",
        true="Ada Lovelace",
        false=[
        "Grace Hopper",
        "Alan Turing",
        "Charles Babbage"
        ]
        ),
    QuizQuestion(
        question="Which has more precision, a double or a float?",
        true="A double.",
        false=[
        "A float.",
        "They have the same precision."
        ]
        ),
    QuizQuestion(
        question="Which of the following programming languages is created by a Japanese developer?",
        true="Ruby",
        false=[
        "C",
        "C++",
        "Java",
        "Kotlin",
        "Python"
        ]
        ),
    QuizQuestion(
        question="Which of the following operators has the highest precedence in C++?",
        true="!",
        false=[
        "*",
        "&&",
        "!=",
        ]
        ),
    QuizQuestion(
        question="What's the meaning behind the name of the Python programming language?",
        true="Monty Python",
        false=[
        "The snake",
        ]
        ),
    QuizQuestion(
        question="What was the original name for Java?",
        true="Oak",
        false=[
        "Coffee",
        "JavaScript",
        "Guava",
        "Homebrew"
        ]
        ),

    ]

    easter_egg_quiz_questions = [
    QuizQuestion(
        question="freeCodeCamp.org first launched in:",
        true="2014",
        false=["2001", "1910", "2030"],
        explanation="The first version of the freeCode",
        learn_more_url="https://www.freecodecamp.org/news/about/",
        easter_egg_name="The Launch of freeCodeCamp",
        difficulty=1
        )
    ]