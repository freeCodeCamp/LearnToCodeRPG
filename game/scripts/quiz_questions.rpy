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
        def __init__(self, question, true, false, category=None, explanation=None, 
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
            self.category = category
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

    # TODO: read csv
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

    css_questions = [
    
        QuizQuestion(
        question="What is RGB?",
        true="A color model",
        false=["An Internet Protocol", "HTML syntax", "A secret password"],
        explanation="RGB is an acronym that stands for {b}red{/b} {b}green{/b} {b}blue{/b}. It expresses colors in terms of the amount of red, green, and blue they are made up of and uses a human counting system with integers ranging from 0-255 or a percentage ranging from (0% - 100%).",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What color would rgb(255,0,0) give?",
        true="Red",
        false=["Green", "Blue", "Yellow"],
        explanation="Each parameter defines the intensity of each color, rgb(red, green, and blue), with an integer number ranging from 0-255. The minimum value of 0 represents that none of the color is being shown, so it is at its darkest. On the other hand, the maximum value of 255 represents that the full amount of color and the full intensity is on display",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What do R, G, and B in RGB stand for?",
        true="Red, green, and blue",
        false=["Red, gray, and black ", "Red, green, and black", "Red, gray, and blue"],
        explanation="RGB is an acronym that stands for {b}red{/b} {b}green{/b} {b}blue{/b}",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What color would rgb(255,255,255) give?",
        true="White",
        false=["Red", "Black", "Blue"],
        explanation="The maximum value of 255 represents that the full amount of all colors and their full intensity is on display.",
        learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the role of media queries in CSS?",
        true="They help create responsive websites",
        false=["They create links to other webpages", "They add interactivity to a static webpage", "They change the font of text"],
        explanation="{b}CSS media queries{/b} allow you to create responsive websites across all screen sizes, ranging from desktop to mobile",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/",
        difficulty=1
        ),
        QuizQuestion(
        question="What are the conditions that decide if a media rule is applied?",
        true="Breakpoints",
        false=["Breaks", "Points", "Keys"],
        explanation="A breakpoint is a key to determine when to change the layout and adapt the new rules inside the media queries",
        learn_more_url="https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the background-image of an element in CSS?",
        true="background-image: url(\"path_to_image\");",
        false=["background-img: url(\"path_to_image\");", "background_image: url(\"path_to_image\");", "background-image: (\"path_to_image\")"],
        explanation="The background-image CSS property allows you to place an image behind any HTML element you wish. Immediately after the property you add a colon. Then, url() is used to tell CSS where the image is located. Inside the parentheses the path to the image is listed in opening and closing double quotes. This lets the browser know what URL to pull. Lastly, don't forget the semicolon to end the statement!",
        learn_more_url="https://www.freecodecamp.org/news/css-background-image-with-html-example-code/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you create a flexbox container in CSS?",
        true="display:flex;",
        false=["display:flexbox;", "display:flexcontainer;", "display:flexB;"],
        explanation="You can apply flexbox to an HTML container by using display:flex;",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to arrange the items in a column?",
        true="flex-direction: column;",
        false=["flex-direction: row;", "flex-column: column;", "flex-direction: set-column;"],
        explanation="In CSS, you can apply flex-direction: column; to the container whose items you want arrange in a column",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to reverse the items in a row?",
        true="flex-direction: row-reverse;",
        false=["flex-direction: reverse-row;", "flex-row: row-reverse;", "flex-direction: set-row-reverse;"],
        explanation="In CSS, you can apply flex-direction: row-reverse; to the container whose items you want to display in a row, with their order reversed.",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you set the flex container to reverse the items in a column?",
        true="flex-direction: column-reverse;",
        false=["flex-direction: reverse-c;", "flex-direction: column-r;", "flex-direction: column-rev;"],
        explanation="In CSS, you can apply flex-direction: column-reverse; to the container whose items you want to display in a column, with their order reversed.",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does justify-content do in flexbox?",
        true="aligns the items along the main axis",
        false=["aligns the items to right of the y axis", "aligns the items to the left of  the x and y axis", "aligns the items to the right of the x axis"],
        explanation="In flexbox, justify-content is used to align the items in the container along the main axis",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with justify-content?",
        true="flex-middle",
        false=["flex-start", "flex-end", "space-around"],
        explanation="In flexbox, some of the options for justify-content include space-around, flex-end, flex-start and space-between",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does align-items do in flexbox?",
        true="aligns the items along the cross axis",
        false=["aligns the items to the right of the y axis", "aligns the items to the right of the x axis", "aligns the items to the right of the z axis"],
        explanation="In flexbox, align-items aligns the items along the cross axis",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with align-items?",
        true="align-middle",
        false=["flex-end", "flex-start", "baseline"],
        explanation="In flexbox, some of the options for align-items include flex-start, flex-end, baseline and stretch",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does align-self do in flexbox?",
        true="adjusts the alignment for an element",
        false=["adjust the alignment for all elements", "adjusts the alignment for hr elements", "adjusts the alignment for an img element"],
        explanation="In flexbox, align-self adjusts the alignment for an element",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you allow items to move to a new line in flexbox?",
        true="flex-wrap: wrap;",
        false=["flex: wrap;", "flex-wrap: wrap-items;", "flex-wrap: item-wrap;"],
        explanation="In flexbox, flex-wrap: wrap; will tell the computer to move items to a new line if there is not enough space",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT used with align-content?",
        true="align-bottom",
        false=["center", "space-around", "stretch"],
        explanation="In flexbox, some of the options for align-content include center, stretch, space-around and space-between",
        learn_more_url="https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the default position property in CSS?",
        true="position: static;",
        false=["position: relative;", "position: top;", "position: absolute;"],
        explanation="The default property in CSS is position: static; which means it follows the order of the HTML",
        learn_more_url="https://www.freecodecamp.org/news/css-positioning-position-absolute-and-relative/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you change the background color in CSS?",
        true="background-color: pink;",
        false=["bg-color: pink;", "backgroundColor: pink;", "b-color: pink;"],
        explanation="You can use the background property in CSS to change the background color of an element",
        learn_more_url="https://www.freecodecamp.org/news/css-background-color-how-to-change-the-background-color-in-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the rule that will override CSS style for an element?",
        true="!important",
        false=["!override", "!change", "!specific"],
        explanation="The !important rule will override the other CSS style rules for that element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make all of the text for an element uppercase?",
        true="text-transform: uppercase;",
        false=["text-transform: toUpper;", "text-transform: upper;", "text-transform: set-upper;"],
        explanation="You can use the text-transform: uppercase; to make all of the text for that element uppercase",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make the text for an element all lowercase?",
        true="text-transform: lowercase;",
        false=["text-transform: lower;", "text-transform: to-lower;", "text-transform: set-lower;"],
        explanation="You can use the text-transform: lowercase; to make all of the text for that element lowercase",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add content before an element?",
        true="::before",
        false=["::add-content", "::before-content", "::after"],
        explanation="You can use the ::before selector to add content before an element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add content after an element?",
        true="::after",
        false=["::after-content", "::add", "::before"],
        explanation="You can use the ::after selector to add content after an element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you add a smooth scroll to the html element?",
        true="scroll-behavior: smooth;",
        false=["scroll-behavior: smooth-scroll;", "scroll: smooth;", "behavior: smooth;"],
        explanation="You can use scroll-behavior: smooth; to add a smooth scroll to the html element",
        learn_more_url="https://www.freecodecamp.org/news/10-css-tricks-for-your-next-coding-project/",
        difficulty=1
        ),
        QuizQuestion(
        question="The amount of space between an element's content and its border is known as...",
        true="Padding",
        false=["Margin", "White Space", "Indentation"],
        explanation="The padding is the amount of space between the element's content and its border.",
        learn_more_url="https://www.freecodecamp.org/news/css-margins/",
        difficulty=1
        ),
        QuizQuestion(
        question="The amount of space between an element's border and its surrounding elements is known as...",
        true="Margin",
        false=["Padding", "White Space", "Indentation"],
        explanation="The margin is the amount of space between an element's border and its surrounding elements.",
        learn_more_url="https://www.freecodecamp.org/news/css-margins/",
        difficulty=1
        ),
        QuizQuestion(
        question="How do you make an image circular or oval?",
        true="border-radius: 50%;",
        false=["border-radius: 10%;", "border-radius: 0;", "border-radius: 3px;"],
        explanation="You can use the CSS property border-radius with a value of 50% to make an image circular or oval.",
        learn_more_url="https://forum.freecodecamp.org/t/freecodecamp-challenge-guide-make-circular-images-with-a-border-radius/18229",
        difficulty=1
        ),
        QuizQuestion(
        question="What CSS selector would you use to select all elements with the class blue-text?",
        true=".blue-text",
        false=["#blue-text", "a[blue-text]", "blue-text"],
        explanation="In CSS, you can select all the elements with a given class with a dot before its name.",
        learn_more_url="https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does CSS stand for?",
        true="Cascading Style Sheets",
        false=["Complex Style Sheets", "Complete Synchronizes Sheets", "Community Stylish System"],
        explanation="CSS stands for Cascading Style Sheets",
        learn_more_url="https://www.freecodecamp.org/news/best-css-and-css3-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the A in RGBA stand for?",
        true="Alpha",
        false=["Alphabetical", "Ambiguous", "Ancient"],
        explanation="The A in RGBA stands for Alpha. This value represents the transparency of the color.",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgba()",
        difficulty=1
        ),
        QuizQuestion(
        question="Type of CSS unit that is relative to another length value.",
        true="Relative",
        false=["Absolute", "Fixed", "Dynamic"],
        explanation="In CSS, relative units are relative to other length values. Several of the relative units depend on the viweport size.",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/#why-learn-css-relative-units",
        difficulty=1
        ),
        QuizQuestion(
        question="Type of CSS unit that is tied to physical units of length. ",
        true="Absolute",
        false=["Relative", "Fixed", "Dynamic"],
        explanation="In CSS, absolute units are tied to physical units of length. ",
        learn_more_url="https://www.freecodecamp.org/news/css-unit-guide/",
        difficulty=1
        ),
        QuizQuestion(
        question="How can you abbreviate the following Hex code? #FF0000",
        true="#F00",
        false=["#0F0", "#00F", "#0FF0"],
        explanation="To abbreviate a Hex code in CSS, include one digit of each pair of digits in the code. ",
        learn_more_url="https://www.freecodecamp.org/news/how-hex-code-colors-work-how-to-choose-colors-without-a-color-picker/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the main purpose of CSS in a website?",
        true="Style",
        false=["Structure", "Functionality", "Sound"],
        explanation="CSS is used to define the style of the elements in a website.",
        learn_more_url="https://www.freecodecamp.org/news/best-css-and-css3-tutorial/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does list-style-type: circle; do in CSS?",
        true="applies circles to all of the list items in an unordered list",
        false=["applies discs to all of the list items in an unordered list", "applies decimals to all of the list items in an unordered list", "applies squares to all of the list items in an unordered list"],
        explanation="list-style-type: circle; will apply circles to all of the list items for the unordered list",
        learn_more_url="https://www.freecodecamp.org/news/html-bullet-points-how-to-create-an-unordered-list-with-the-ul-tag-example/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values does NOT apply to the CSS all shorthand property?",
        true="position",
        false=["unset", "initial", "revert"],
        explanation="The all CSS shorthand property can accept the following values: initial, inherit, unset, revert",
        learn_more_url="https://developer.mozilla.org/en-US/docs/Web/CSS/all",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-name property do in CSS?",
        true="a name used to describe the animation applied to the element",
        false=["sets the duration for the animation", "sets a delay for the animation to start", "sets how many times an animation should run"],
        explanation="The animation-name is used to describe the animation applied to the element",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-duration property do in CSS?",
        true="determines how long an animation should last in seconds",
        false=["is used to style the element after the animation ends", "sets the direction for the element", "pauses the animation if the animation is running"],
        explanation="The animation-duration is used to determine how long an animation should last in seconds",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-timing-function do in CSS?",
        true="determines when the animation should speed up or slow down",
        false=["sets the direction for the element", "is used to style the element after the animation ends", "a name used to describe the animation applied to the element"],
        explanation="The animation-timing-function  is used to determine when the animation should speed up or slow down",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-delay  do in CSS?",
        true="sets a delay for the animation to start",
        false=["determines how long an animation should last in seconds", "pauses the animation if the animation is running", "determines when the animation should speed up or slow down"],
        explanation="The animation-delay is used to set a delay for the animation to start",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-iteration-count do in CSS?",
        true="sets how many times an animation should run",
        false=["a name used to describe the animation applied to the element", "determines how long an animation should last in seconds", "sets a delay for the animation to start"],
        explanation="The animation-iteration-count sets how many times the animation should run",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-direction  do in CSS?",
        true="sets the direction for the animation",
        false=["sets how many times an animation should run", "is used to style the element after the animation ends", "pauses the animation if the animation is running"],
        explanation="The animation-direction sets the direction for the animation",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-fill-mode do in the CSS?",
        true="is used to style the element after the animation ends",
        false=["sets a delay for the animation to start", "sets how many times an animation should run", "determines how long an animation should last in seconds"],
        explanation="The animation-fill-mode is used to style the element after the animation ends",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the animation-play-state do in CSS?",
        true="is used to pause the animation if set to paused",
        false=["determines how long an animation should last in seconds", "is used to style the element after the animation ends", "sets the direction for the animation"],
        explanation="The animation-play-state is used to pause the animation if set to paused",
        learn_more_url="https://www.freecodecamp.org/news/a-quick-introduction-to-css-animations-a1655375ec90/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is an at-rule in CSS?",
        true="rules that dictate what the CSS will look like based on certain conditions",
        false=["rules to dictate how to format the HTML", "rules to dictate javascript functions", "rules to that only apply to how p elements are styled"],
        explanation="An at-rule in CSS will dictate what the CSS will look like based on certain conditions",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a media type in CSS?",
        true="the category of media for the device",
        false=["set of rules only applied to mobile devices", "category only for print media", "category only for speech"],
        explanation="A media type refers to the category of media for the device",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the all media type in CSS?",
        true="works for all devices",
        false=["only works for mobile devices", "only works for print media", "only works for tablets"],
        explanation="The all media type will work for all media devices",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the print media type in CSS?",
        true="works for devices where the media is in print preview mode",
        false=["a type of media only for 4k monitors", "a type of media that only works for desktop computers", "set of rules only applied to mobile devices"],
        explanation="The print media type works for devices where the media is in print preview mode",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the screen media type in CSS?",
        true="works for devices with screens",
        false=["works for media in print preview mode", "works for devices without screens", "only works for tablets"],
        explanation="The screen media type works for devices with screens",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the speech media type in CSS?",
        true="works for devices like screen readers where the content is read out loud to the user",
        false=["works for devices with screens", "works for devices where the media is in print preview mode", "only works for mobile devices"],
        explanation="The speech media type works for devices like screen readers where the content is read out loud to the user",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the and operator used in a media query?",
        true="join multiple media features",
        false=["reverses a true query into a false", "separate multiple media features by commas", "splits media queries into separate ones"],
        explanation="The and operator is used to join multiple media features in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the not operator used in a media query?",
        true="reverses a true query into a false and a false query into a true",
        false=["join multiple media features", "splits media queries into separate ones", "separate multiple media features by commas"],
        explanation="The not operator is used to reverse a true query into a false and a false query into a true",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="How is the comma operator used in a media query?",
        true="separates multiple media features by commas and apply the styles inside the curly brace if one of the conditions is true",
        false=["reverses a true query into a false and a false query into a true", "join multiple media features", "splits media queries into separate ones"],
        explanation="The comma operator is used to separate multiple media features by commas and apply the styles inside the curly brace if one of the conditions is true",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for mobile devices in a media query?",
        true="320px - 480px",
        false=["1000px - 5000px", "100px - 150px", "200px - 4000px"],
        explanation="The range of 320px — 480px can be used to target mobile devices in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for tablet devices in a media query?",
        true="481px - 768px",
        false=["300px - 7000px", "2px - 68px", "81px - 700px"],
        explanation="The range of 481px - 768px can be used to target table devices in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for laptop devices in a media query?",
        true="769px -1024px",
        false=["7px -10px", "69px -124px", "769px -10,024px"],
        explanation="The range of 769px -1024px can be used to target laptop devices ina media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is a common breakpoint range used for desktop and larger screens in a media query?",
        true="1025px - 1200px",
        false=["25px - 120px", "125px - 12,000px", "5px - 12px"],
        explanation="The range of 1025px - 1200px can be used to target desktop and larger screen  in a media query",
        learn_more_url="https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the CSS property that sets the opacity for an HTML element",
        true="opacity",
        false=["margin", "padding", "border"],
        explanation="The opacity property is used to set the opacity for an HTML element",
        learn_more_url="https://www.freecodecamp.org/news/transparent-background-image-opacity-in-css-and-html/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the code used to create a CSS grid container?",
        true="display: grid;",
        false=["display: flex;", "display: grid-box;", "display: grid-container;"],
        explanation="You can use display: grid; to create a new CSS grid container",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of grid property used to set the number and width of columns?",
        true="grid-template-columns",
        false=["grid-columns", "flex-template-columns", "template-columns-grid"],
        explanation="The grid-template-columns property is used to set the number and width for the columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the function to set the width for all columns in CSS grid?",
        true="repeat",
        false=["set-width", "width-all", "width-container"],
        explanation="The repeat() function is used to set the width for all of the columns in in the grid container",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What does fr stand for in CSS grid?",
        true="fraction unit",
        false=["font units", "flex unit", "fit unit"],
        explanation="fr stands for fraction unit in CSS grid",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to set the number and height for the rows?",
        true="grid-template-rows",
        false=["grid-template-columns", "grid-rows", "grid-unit-rows"],
        explanation="The grid-template-rows property is used to set the number and height for the rows",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to set the space for grid cells in rows and columns?",
        true="grid-template-areas",
        false=["grid-template-rows", "fraction unit", "repeat"],
        explanation="The grid-template-areas property is used to set the space for grid cells in rows and columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to create gaps between columns?",
        true="column-gap",
        false=["set-width", "fit unit", "grid-template-columns"],
        explanation="The column-gap property is used to create gaps between columns",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to create gaps between rows?",
        true="row-gap",
        false=["grid-template-rows", "grid-columns", "repeat"],
        explanation="The row-gap property is used to create gaps between rows",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the grid property used to position items inside the container along the main axis?",
        true="justify-items",
        false=["justify-content", "justify-rows", "justify-columns"],
        explanation="The justify-items property is used to position items within a grid container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the justify-items property?",
        true="gap",
        false=["start", "end", "stretch"],
        explanation="The four values that can be used for the justify-items property are start, end, center, and stretch",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position items inside the container along the y-axis?",
        true="align-items",
        false=["grid-columns", "grid-template-columns", "fraction unit"],
        explanation="The align-items property is used to position items in the container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position the grid inside the container along the x-axis?",
        true="justify-content",
        false=["grid-template-areas", "grid-template-rows", "row-gap"],
        explanation="The justify-content property is used to position the grid in the container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the justify-content property?",
        true="repeat",
        false=["space-around", "space-between", "space-evenly"],
        explanation="The justify-content property can accept seven values including space-around, space-between, start and end",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position the grid inside the container along the y-axis?",
        true="align-content",
        false=["justify-content", "end", "grid-unit-rows"],
        explanation="The align-content property is used to position the grid in the container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these options is NOT a value used for the align-content property?",
        true="row-gap",
        false=["space-between", "center", "start"],
        explanation="The align-content property can accept seven values including space-around, space-between, start and end",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position one grid item in a container along the x-axis?",
        true="justify-self",
        false=["align-content", "grid-template-areas", "justify-rows"],
        explanation="The justify-self property is used to position one grid item in a container along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to position one grid item in a container along the y-axis?",
        true="align-self",
        false=["grid-columns", "space-around", "grid-template-columns"],
        explanation="The align-self property is used to position one grid item in a container along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/#css-grid-architecture",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to adjust the size for a background image in CSS?",
        true="background-size",
        false=["background-repeat", "background-origin", "background-position"],
        explanation="The background-size property is used to adjust the size for a background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to repeat a background image?",
        true="background-repeat",
        false=["background-position-x", "background-position-y", "background-origin"],
        explanation="The background-repeat property is used to repeat the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-repeat property?",
        true="repeat-z-axis",
        false=["no-repeat", "repeat", "repeat-x"],
        explanation="The background-repeat property can take in seven values include no-repeat, repeat, repeat-x and repeat-y",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the repeat-x value do in the background-repeat property?",
        true="repeats the image along the x-axis",
        false=["repeats the image along the y-axis", "repeats the image along the z-axis", "repeats the image along both of the x-axis and y-axis"],
        explanation="The repeat-x value repeats the image along the x-axis",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the repeat-y value do in the background-repeat property?",
        true="repeats the image along the y-axis",
        false=["repeats the image along the x-axis", "repeats the image along both of the x-axis and y-axis", "repeats the image along the z-axis"],
        explanation="The repeat-y value repeats the image along the y-axis",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the no-repeat value do in the background-repeat property?",
        true="sets no repetition for the background image",
        false=["repeats the image along the z-axis", "repeats the image along the y-axis", "repeats the image along the x-axis"],
        explanation="The no-repeat value sets no repetition for the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the value that evenly distributes space in the background-repeat property?",
        true="space",
        false=["repeat", "no-repeat", "repeat-x"],
        explanation="The space value is used to evenly distributes the space in the background-repeat property",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the value that stretches the repeated images in the background-repeat property?",
        true="round",
        false=["space", "around", "rounding"],
        explanation="The round value is used to stretch the repeated images in the background-repeat property",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to change the position of the background image?",
        true="background-position",
        false=["background-clip", "background-color", "background-origin"],
        explanation="The background-position is used to change the position of the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-position property?",
        true="side-left",
        false=["top", "bottom", "right"],
        explanation="The background-position property can take in many values including of top, right, left and bottom",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property used to change the origin of the background image?",
        true="background-origin",
        false=["background-position", "background-clip", "background-color"],
        explanation="The background-origin property is used to set the origin for the background image",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-origin property?",
        true="box-sizing",
        false=["border-box", "padding-box", "content-box"],
        explanation="The background-origin property can use following value border-box, padding-box, inherit, content-box",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property that clips the background image to inside the container?",
        true="background-clip",
        false=["background-color", "background-position", "background-size"],
        explanation="The background-clip property is used to clip the background image to inside the container",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the property that determines if the background image is in a scroll or fixed position?",
        true="background-attachment",
        false=["background-origin", "background-clip", "background-position"],
        explanation="The background-attachment property is used to determine if the background image is in a scroll or fixed position",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values is NOT used for the background-attachment property?",
        true="inherit",
        false=["local", "scroll", "fixed"],
        explanation="The background-attachment property can take in the fixed, scroll and local values",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-background-properties/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one is NOT an example of a relative unit in CSS?",
        true="px",
        false=["rem", "em", "vh"],
        explanation="Relative units in CSS include rem, em, vh, and vw",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="How many pixels are equivalent to 1 rem unit?",
        true="16",
        false=["32", "12", "6"],
        explanation="One rem unit is equivalent to 16 pixels",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the relative unit that based on the root element's font size?",
        true="rem",
        false=["em", "px", "vw"],
        explanation="The rem unit is based off of the root element's font size",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What is the name of the relative unit that is based its parent's font size",
        true="em",
        false=["rem", "vh", "vw"],
        explanation="The em unit is based off of the parent's font size",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the vw unit stand for?",
        true="viewport width",
        false=["view width height", "viewport weight", "viewport height"],
        explanation="The vw unit stands for viewport width",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values represents 10% of the viewport width?",
        true="10vw",
        false=["10vh", "100vw", "1000vw"],
        explanation="10vw is equivalent to 10% of the viewport width",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What does the vh unit stand for?",
        true="viewport height",
        false=["viewport width", "view heights", "viewing height"],
        explanation="The vh unit stands for viewport height",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="Which one of these values represents 20% of the viewport height?",
        true="20vh",
        false=["200vh", "2vh", "2000vh"],
        explanation="20vh is equivalent to 20% of the viewport height",
        learn_more_url="https://www.freecodecamp.org/news/learn-css-units-em-rem-vh-vw-with-code-examples/",
        difficulty=1
        ),
        QuizQuestion(
        question="What CSS property is used to customize the marker of a list item?",
        true="list-style-type",
        false=["list-style", "list-marker-type", "list-markers"],
        explanation="The list-style-type property is used to set the marker of a list item. ",
        learn_more_url="https://www.freecodecamp.org/news/how-to-style-lists-with-css/",
        difficulty=2
        ),
        QuizQuestion(
        question="What is the universal selector in CSS?",
        true="*",
        false=["#", "$", "@"],
        explanation="The asterisk * is the universal selector in CSS. It selects all elements of any type.",
        learn_more_url="https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/",
        difficulty=2
        ),
        QuizQuestion(
        question="Fonts that are generally available across most browsers and operating systems are known as...",
        true="Web safe fonts",
        false=["General fonts", "Universal fonts", "Web Fonts"],
        explanation="Web safe fonts are the fonts that are generally available across most browsers and operating systems.",
        learn_more_url="https://www.freecodecamp.org/news/web-safe-fonts/",
        difficulty=2
        )
    ]