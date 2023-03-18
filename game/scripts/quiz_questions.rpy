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

            label _('Question')
            text quiz_question.question

            null height 20
            label _('Correct answer')
            text _('{b}[quiz_question.true!t]{/b}')

            null height 20
            if quiz_question.explanation:
                label _('Explanation')
                text quiz_question.explanation

            if quiz_question.learn_more_url:
                textbutton _("{icon=icon-help-circle} Learn More"):
                    hovered Notify(_('Learn more about this topic in an article!'))
                    action OpenURL(quiz_question.learn_more_url)

            null height 40
            textbutton _("Gotcha! Let's move on."):
                xalign 0.5
                action Return()

python early:

    class QuizQuestion():
        '''
        question: a string
        true: a string
        false: a list of strings
        explanation: an optional string
        code_label: an optional string, see game/quiz_code_snippets.txt
        '''
        def __init__(self, question, true, false, category=None, explanation=None, 
            code_label=None, learn_more_url=None, easter_egg_name=None, difficulty=None,
            spaced_repetition=None):

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
            self.category = category
            self.code_label = code_label
            self.learn_more_url = learn_more_url
            self.easter_egg_name = easter_egg_name
            self.difficulty = difficulty

            self.spaced_repetition = spaced_repetition

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.__dict__ == other.__dict__
            else:
                return False

init 101 python:

    ## Hacker Space Tech Trivia
    trivia_questions = [
    QuizQuestion(
        question=_("Which is faster for training Neural Networks, a GPU or a CPU?"),
        true=_("GPU."),
        false=[_("CPU."), _("They are the same.")]
        ),
    QuizQuestion(
        question=_("Which of the following is a legal identifier in assembly language?"),
        true=_("july_2021"),
        false=[_("10percent"), _("a1a2a3...a247a248"), _("eflags")]
        ),
    QuizQuestion(
        question=_("Who was the child of a famous poet and English mathematician whom many historians consider the first programmer?"),
        true=_("Ada Lovelace"),
        false=[_("Grace Hopper"), _("Alan Turing"), _("Charles Babbage")]
        ),
    QuizQuestion(
        question=_("Which has more precision, a double or a float?"),
        true=_("A double."),
        false=[_("A float."), _("They have the same precision.")]
        ),
    QuizQuestion(
        question=_("Which of the following programming languages is created by a Japanese developer?"),
        true=_("Ruby"),
        false=[_("C"), _("C++"), _("Java"), _("Kotlin"), _("Python")]
        ),
    QuizQuestion(
        question=_("Which of the following operators has the highest precedence in C++?"),
        true=_("!"),
        false=[_("*"), _("&&"), _("!=")]
        ),
    QuizQuestion(
        question=_("What's the meaning behind the name of the Python programming language?"),
        true=_("Monty Python"),
        false=[_("The snake")]
        ),
    QuizQuestion(
        question=_("What was the original name for Java?"),
        true=_("Oak"),
        false=[_("Coffee"), _("JavaScript"), _("Guava"), _("Homebrew")]
        ),

    ]

    easter_egg_quiz_questions = [

    QuizQuestion(
    question=_("freeCodeCamp.org first launched in:"),
    true=_("2014"),
    false=[_("2001"), _("1910"), _("2030")],
    explanation=_("The first version of the freeCodeCamp curriculum went live in 2014, from Quincy Larson's closet office in San Francisco. Other developers quickly stepped in to help expand the curriculum and save him from madness."),
    learn_more_url="https://www.freecodecamp.org/news/about/",
    difficulty=1,
    easter_egg_name=quiz_fcc_launch
    ),
    QuizQuestion(
    question=_("freeCodeCamp is a 501(c)(3) public charity (nonprofit) with a mission to:"),
    true=_("To help people learn to code for free."),
    false=[_("Help companies recruit developers"), _("Advocate for open source software"), _("Make cat photo apps")],
    explanation=_("Even though freeCodeCamp does create open source projects, and does help developers get jobs, its mission is \"to help people learn to code for free. We accomplish this by creating thousands of videos, articles, and interactive coding lessons - all freely available to the public.\""),
    learn_more_url="https://www.freecodecamp.org/news/about/",
    difficulty=1,
    easter_egg_name=quiz_fcc_mission
    ),
    QuizQuestion(
    question=_("Code Radio is:"),
    true=_("An internet radio that plays music you can code to"),
    false=[_("A form of communication America used during World War II created by the Navajo people"), _("A radio station for old acoustic modems"), _("A way to talk with beings from other solar systems")],
    explanation=_("Code Radio is avilable 24/7, with more than 1,500 instrumental songs on rotation. Lots of developers enjoy listening to it as background music while they work."),
    learn_more_url="https://www.freecodecamp.org/news/code-radio-24-7/",
    difficulty=1,
    easter_egg_name=quiz_code_radio
    ),
    QuizQuestion(
    question=_("What is DevDocs.io? "),
    true=_("A powerful documentation website run by the freeCodeCamp community"),
    false=[_("A community of doctors who know how to code"), _("Developers who work at the shipyard"), _("A fancy docking station you can put your laptop on while you code")],
    explanation=_("DevDocs.io is a popular search engine for programming language documentation. You can download the full documentation for different tools and browse it offline. Perfect for when you need to code on the go and won't have an internet connection."),
    learn_more_url="https://www.freecodecamp.org/news/devdocs-is-joining-the-freecodecamp-community-ae185a1c14a6/",
    difficulty=1,
    easter_egg_name=quiz_devdocs
    ),
    QuizQuestion(
    question=_("What is the name of freeCodeCamp's popular GitHub repository that teaches you how to contribute to open source?"),
    true=_("How to Contribute to Open Source"),
    false=[_("GitGoing"), _("Project Octocat"), _("Open Sauce")],
    explanation=_("One of the best ways to get real-world experience working with large legacy codebases is to contribute to open source. But this is an ambiguous process. So the freeCodeCamp community created this repository to help new developers get started."),
    learn_more_url="https://www.freecodecamp.org/news/how-to-contribute-to-open-source-projects-beginners-guide/",
    difficulty=1,
    easter_egg_name=quiz_fcc_opensource
    ),
    QuizQuestion(
    question=_("The freeCodeCamp learning platform is written in which programming language?"),
    true=_("JavaScript and Node.js"),
    false=[_("Python and Django"), _("PHP and Laravel"), _("Java and Spring")],
    explanation=_("freeCodeCamp teaches many different programming languages and frameworks, and could be written in any of these. This said, in 2014 when Quincy Larson sat down to start building the first version of freeCodeCamp, he chose JavaScript and Node.js. He did this because it had a huge package ecosystem and was relatively easy to program in. Node.js is also very fast, and works well at scale. Large websites like Netflix and LinkedIn use it as a primary language."),
    learn_more_url="https://www.freecodecamp.org/news/the-definitive-node-js-handbook-6912378afc6e/",
    difficulty=1,
    easter_egg_name=quiz_fcc_language
    ),
    QuizQuestion(
    question=_("Which open source community has been the biggest inspiration to freeCodeCamp?"),
    true=_("Wikipedia"),
    false=[_("Linux"), _("Mozilla Firefox"), _("Open Office")],
    explanation=_("All of these projects have been a source of inspiration, but Wikipedia is the closest analog to what the freeCodeCamp community would ultimately like to become: hundreds of languages represented, with thousands of contributors from a wide variety of backgrounds and interests."),
    learn_more_url="https://www.freecodecamp.org/news/welcome-to-the-abundance-economy-there-are-free-lunches-all-over-the-place-b9d0a417fd1a/",
    difficulty=1,
    easter_egg_name=quiz_fcc_inspiration
    ),
    QuizQuestion(
    question=_("What forum tool does freeCodeCamp use for its forum?"),
    true=_("Discourse"),
    false=[_("NodeBB"), _("phpBB"), _("vBulletin")],
    explanation=_("The freeCodeCamp community was an early adopter of Discourse, a powerful forum tool designed by Stack Overflow founder Jeff Atwood. Quincy Larson first met Jeff at an event in San Francisco in 2014, and the two talked about online communities. Jeff convinced Quincy to create a forum so that learners could easily help one another. One benefit of a forum is that other people can then discover past conversations, and use them to help get unstuck. If you ask a question on the freeCodeCamp forum, you will generally get an answer in just a few hours."),
    learn_more_url="https://www.freecodecamp.org/news/the-future-of-the-freecodecamp-forum/",
    difficulty=1,
    easter_egg_name=quiz_fcc_forum
    ),
    QuizQuestion(
    question=_("What chat tool does freeCodecamp use for its main self-hosted chat server?"),
    true=_("Discord"),
    false=[_("Slack"), _("RocketChat"), _("Gitter")],
    explanation=_("The freeCodeCamp contributor community communicates mostly through our active Discord server at discord.gg/PRyKn3Vbay, and in the past have used RocketChat, Slack and Gitter."),
    learn_more_url="https://www.freecodecamp.org/news/freecodecamp-discord-chat-room-server/",
    difficulty=1,
    easter_egg_name=quiz_fcc_chat
    ),
    QuizQuestion(
    question=_("freeCodeCamp's Mascot is:"),
    true=_("CamperBot"),
    false=[_("freeCodeCampasaurus Rex"), _("Bill Murray"), _("Campy the Raccoon")],
    explanation=_("The freeCodeCamp community created CamperBot early on to help out with automated tasks in our chat rooms. Since then, he has been helpful in many different places, including the freeCodeCamp forum. He is a helpful robot who runs on kindness."),
    learn_more_url="https://www.freecodecamp.org/news/about/",
    difficulty=1,
    easter_egg_name=quiz_fcc_mascot
    )    
    ] 