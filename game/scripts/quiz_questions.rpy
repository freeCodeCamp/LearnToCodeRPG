init python:
    class QuizQuestion():
        '''
        question: a string
        true: a string
        false: a list of strings
        code_label: an optional string, see game/quiz_code_snippets.txt
        '''
        def __init__(self, question, true, false, code_label=None):
            choices = {
            question: None,
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
            # put the question at the front
            self.choices = [(question, None)] + choices

            self.code_label = code_label

    general_questions = [
    
    QuizQuestion(
        question="What is the binary representation of 10?",
        true="1010",
        false=["0101"]
        ),

    QuizQuestion(
        question="What is the size of wchar_t in bits?",
        true="16", 
        false=["8", "4"]
        ),

    QuizQuestion(
        question="How many times is the value of i checked in the following C code?",
        true="3",
        false=["2", "4", "1"],
        code_label="code1"
        ),

    QuizQuestion(
        question="Which will display `hello world` in JavaScript?",
        true="console.log('hello world')",
        false=["console.print('hello world')", "document.write('hello world')"]
        ),

    QuizQuestion(
        question="What will this Python code print?\n`print([0,[1,2,3,4,5][2],2][1])`",
        true="3",
        false=["0", "1", "2", "π"]
        ),

    ]

    # https://github.com/freeCodeCamp/multiple-choice-questions
    
    javascript_questions = [

    QuizQuestion(
        question="Which of the following statements is true of JavaScript?",
        true="All of these choices are correct",
        false=[
        "JavaScript supports object-oriented programming"
        ]
        ),

    ]

    web_questions = [

    ]

    algorithm_questions = [

    ]

    system_questions = [

    ]