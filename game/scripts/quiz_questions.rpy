init python:
    class QuizQuestion():
        '''
        question: a string
        true: a string
        false: a list of strings
        code: an optional string
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
            self.choices = [
            (question, None),
            (true, True),
            ]
            for f in false:
                self.choices.append((f, False))
            self.code_label = code_label

    general_questions = [
    
    # QuizQuestion(
    #     question="What is the binary representation of 10?",
    #     true="1010",
    #     false=["0101"]
    #     ),

    # QuizQuestion(
    #     question="What is the size of wchar_t in bits?",
    #     true="16", 
    #     false=["8", "4"]
    #     ),

    QuizQuestion(
        question="How many times is the value of i checked in the following C code?",
        true="3",
        false=["2", "4", "1"],
        code_label="code1"
        )
    ]

    # https://github.com/freeCodeCamp/multiple-choice-questions
