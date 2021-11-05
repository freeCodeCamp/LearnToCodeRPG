init:
    screen quiz_question_answer_explanation_screen(quiz_question):
        # see code_snippet_example_screen.rpy

        default raw_code = example_code(quiz_question.code_label, raw=True)
        default code = example_code(quiz_question.code_label)

        on "show" action With(Dissolve(0.5))
        on "hide" action With(Dissolve(0.5))

        frame:
            xalign 0.5
            yalign 0.5
            xpadding 80
            ypadding 30
            background "#fffc"

            vbox:
                spacing 10

                textbutton '{icon=close}' xalign 1.0 action Return(True)

                viewport:
                    xsize 1000
                    ymaximum 600
                    child_size (None, 4000)
                    scrollbars 'vertical'
                    spacing 5
                    draggable True
                    mousewheel True
                    arrowkeys True
                    vscrollbar_xsize 5
                    vscrollbar_unscrollable "hide"

                    vbox spacing 5:
                        text 'Question Recap' bold True
                        text quiz_question.question

                        # TODO: maybe add copy code feature from screen example
                        if quiz_question.code_label:
                            null height 30
                            frame: # different background color from the primary screen for contrast
                                background "#d0d0d5cc" # gray15 at 80% opacity
                                text code:
                                    alt ""
                                    size gui.notify_text_size
                                    color "#000"
                                    font "fonts/roboto-mono/RobotoMono-Regular.ttf"

                        null height 30

                        text 'Correct answer' bold True
                        text quiz_question.true
                        if quiz_question.explanation:
                            null height 50
                            text 'Explanation' bold True
                            text quiz_question.explanation

init python:
    class QuizQuestion():
        # TODO: explanation
        '''
        question: a string
        true: a string
        false: a list of strings
        code_label: an optional string, see game/quiz_code_snippets.txt
        '''
        def __init__(self, question, true, false, explanation=None, code_label=None):
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

    # we have general_questions, javascript_questions, web_questions, algorithm_questions, and system_questions

    general_questions = [
    
    QuizQuestion(
        question="What is the binary representation of 10?",
        true="1010",
        false=["0101", "1011", "0010"]
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
        code_label='c_code1'
        ),

    QuizQuestion(
        question="Which will display `hello world` in JavaScript?",
        true="console.log('hello world')",
        false=["console.print('hello world')", "document.write('hello world')"]
        ),

    QuizQuestion(
        question="What will this Python code print?",
        true="3",
        false=["0", "1", "2", "π"],
        code_label='py_code1'
        ),

    QuizQuestion(
        question="What is the value of 'puzzle' in this line of JavaScript?",
        true="joke answer",
        false=["free", "code", "camp", "courses"],
        code_label='js_code11'
        ),

    QuizQuestion(
        question="What will this Python code print?",
        true="None of the above.",
        false=["012345", "15", "01234", "10"],
        code_label='py_code2'
        ),

    QuizQuestion(
        question="What should be at the top of most HTML files?",
        true="<!DOCTYPE html>",
        false=["<DOCTYPE html>", "<!BEWARE html>"]
        ),

    QuizQuestion(
        question="Which is an HTML comment?",
        true="<!-- comment -->",
        false=["// comment", "# comment", "-- comment"]
        ),

    QuizQuestion(
        question="In Regex, which will match all digits in a string?",
        true="[[1-9]",
        false=["/#", "/digits", "/D", "/d"]
        ),

    QuizQuestion(
        question="What will the following Python code print?",
        true="Any line that starts with 'From:'",
        false=[
        "Any line containing 'From'",
        "Any line taht starts with 'From'",
        "Any line containing 'From:'",
        "The lyrics of 'Never Gonna Give You Up'"
        ],
        code_label='py_code3'
        ),

    QuizQuestion(
        question="What will print out after running this Python code:",
        true="4.0",
        false=["4", "height/3", "5", "opossum"],
        code_label='py_code4'
        ),

    QuizQuestion(
        question="What will be the output of the following JavaScript code?",
        true="11",
        false=["11121314", "1112", "12345"],
        code_label='js_code12'
        ),

    QuizQuestion(
        question="How do you access the value for key `Price` in the following Python dictionary?",
        true='mystock[["Price"]',
        false=[
        'mystock[[Price]',
        'mystock("Price")',
        'mystock{{"Price"}',
        'mystock(price)'
        ],
        code_label='py_code5'
        ),

    QuizQuestion(
        question="Which will create a variable in JavaScript?",
        true='let me = "in"',
        false=[
        'string freeCodeCamp = "amazing";',
        'language <- "JavaScript"',
        'variable correct = "answer";',
        'let there be variable'
        ]
        ),

    QuizQuestion(
        question="What will be the output of the following Java code?",
        true="Runtime Exception",
        false=[
        "Compile time exception",
        "UnsupportedOperationException",
        ],
        code_label='java_code1'
        ),

    QuizQuestion(
        question="How do you convert uppercase letters in a string to lowercase letters in Python?",
        true="lower()",
        false=["lowercase()", "toLower()", "sudo make lower case"]
        ),

    QuizQuestion(
        question="What will be the output of the following Java code?",
        true="UnsupportedOperationException",
        false=[
        "{{11=a}",
        "{{11=a, 12=b}",
        "Compile time exception",
        ],
        code_label='java_code2'
        ),

    QuizQuestion(
        question="Which of the following properly expresses the precedence of operators (using parentheses) in the following expression: 5*3 > 10 and 4+6==11",
        true="((5*3) > 10) and ((4+6) == 11)",
        false=[
        "(5*(3 > 10)) and (4 + (6 == 11))",
        "((((5*3) > 10) and 4)+6) == 11",
        "((5*3) > (10 and (4+6))) == 11"
        ]
        ),

    QuizQuestion(
        question="What is the command to list all Node modules that are installed globally?",
        true="npm ls -g",
        false=[
        "npm ls",
        "node ls -g",
        "node ls"
        ]
        ),

    QuizQuestion(
        question="Which line of code produces a list of numbers between 1 and 1000 that are divisible by 3?",
        true="[[x for x in range(1000) if x%3==0]",
        false=[
        "[[x in range(1, 1000) if x%3==0]",
        "[[x%3 for x in range(1, 1000)]",
        "[[x%3=0 for x in range(1, 1000)]"
        ]
        ),

    QuizQuestion(
        question="What is the output of the following Python program?",
        true="33",
        false=["34", "12", "31", "42"],
        code_label='py_code6'
        ),

    QuizQuestion(
        question="What is the result of the following Java code?",
        true="A will be printed, and then an exception is thrown.",
        false=[
        "It only prints B and exits.",
        "It only prints A and exits.",
        "It prints A and B with a 1000 seconds delay between them."
        ]
        ),

    QuizQuestion(
        question="Which of the following is not part of Data Analysis?",
        true="Picking a desired conclusion for the analysis.",
        false=[
        "Building statistical models and data visualizations.",
        "Fixing incorrect values and removing invalid data.",
        "Transforming data into an appropriate data structure."
        ]
        ),

    QuizQuestion(
        question="What does the shape of our dataframe tell us?",
        true="How many rows and columns our dataframe has.",
        false=[
        "The size in gigabytes the dataframe we loaded into memory is.",
        "How many rows the source data had before loading.",
        "How many columns the source data had before loading."
        ]
        ),

    QuizQuestion(
        question="Which statement below is false?",
        true="Neural networks are modeled after the way the human brain works.",
        false=[
        "Computer programs that play tic-tac-toe or chess against human players are examples of simple artificial intelligence.",
        "Machine learning is a subset of artificial intelligence."
        ]
        ),

    QuizQuestion(
        question="Where are your programs stored when they are running?",
        true="Memory.",
        false=["Hard Drive.", "Central Processing Unit."]
        ),

    QuizQuestion(
        question="Which data structure ensures the uniqueness of its elements?",
        true="Set",
        false=["List", "Array", "Collection", "Heap"]
        ),

    ]

    # https://github.com/freeCodeCamp/multiple-choice-questions
    
    javascript_questions = [

    QuizQuestion(
        question="Which of the following statements is true of JavaScript?",
        true="All of these choices are correct",
        false=[
        "JavaScript supports object-oriented programming",
        "JavaScript supports functional programming",
        "JavaScript supports imperative programming",
        ]
        ),

    QuizQuestion(
        question="Is JavaScript single-threaded or multi-threaded?",
        true="JavaScript is single-threaded.",
        false=[
        "Threading only applies to compiled languages.",
        "JavaScript is multi-threaded.",
        "Threading only applies in staticly typed languages.",
        ]
        ),

    QuizQuestion(
        question="What will the following code print to the console?",
        true="dlroW olleH",
        false=[
        "[[ 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd' ]",
        "[[ 'd', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H' ]",
        "Hello World",
        ],
        code_label='js_code1',
        explanation="You may have expected this code to print Hello World to the console. However, when we define baz, we are not creating a new array. Rather, we are simply creating a reference to the array that was created during the assignment of bar (in fact, both variables are just references to the same object, which is stored in memory behind the scenes). Since baz is just a reference to bar, and not its own array, any operation that is performed on it, is also performed on the original array. So, when we join bar back into a string, the result is a mirror image of what you might have expected! And, of course, the same result that we would have gotten from console.log(baz.join(' '));"
        ),

    QuizQuestion(
        question="When executed in a browser's console, what will the following code output?",
        true="Window {{...}\nundefined",
        false=[
        "{{ baz: 'Hello', bar: [[Function: bar] }\nHello",
        "Window {{...}\nHello",
        "{{ baz: 'Hello', bar: [[Function: bar] }\nundefined"
        ],
        code_label='js_code2',
        explanation="""
        You might have expected this code to log the foo object along with Hello to the console, however, arrow function expressions are not ideally suited for method functions. Here's why: arrow functions do not create their own this context, nor do they care how the function is called; rather, they inherit their this value from the enclosing scope. So in this case, this still refers to the global context, in which baz is not defined. Had bar been written with the function keyword, this code would have worked as expected, since typically, when a function is invoked with method invokation, this will always refer to the context, or object, that the function was written in.

        Note that in different environments, the global this value can reference different things. Running this code in a browser's console, as in this example, this will always refer to the global Window object. If we ran this same code in a Node environment, however, the this value would simply be an empty global object: {{}.

        In general, there's no other reason why arrow functions are not an appropriate choice for object methods. So if you use them in this way, just be careful with this!
        """
        ),

    QuizQuestion(
        question="Which of the following is a feature provided by ES6 arrow functions?",
        true='They "inherit" this from the enclosing lexical context, regardless of how the function is called.',
        false=[
        "They allow for functional composition.",
        "The only advantage is shorter syntax.",
        "They are prone to fewer memory leaks."
        ],
        explanation="""
        ES6 arrow functions take this from the context where they are written and implicitly bind it to the function. Now, regardless of where that function is called it will retain the original this value. The same result could be accomplished by explicitly binding this (e.g. .bind(this)) to the function in the context you want to bind this. Otherwise, for non-arrow functions, this will be defined by the context in which a function is called.
        """
        ),

    QuizQuestion(
        question="In JS, The use of const prevents the modification of arrays and objects.",
        true="True, these are now constant values.",
        false=["False, they are only references. The actual values in the array or object can still be mutated."],
        explanation="""
        The use of const prevents a value from being reassigned. Arrays and objects, however, can be modified without being reassigned. If you have a const object dictionary and you write dictionary[[freecodecamp] = true this code will run without error. However, if you were to try to reassign this constant value by writing dictionary = 5, this would throw an error: Uncaught TypeError: Assignment to constant variable. This is an important aspect to keep in mind when working with constant values in JavaScript.
        """
        ),

    QuizQuestion(
        question="Which of the following choices will empty the array foo as well as all references to foo (such as bar)?",
        true="foo.splice(0, foo.length);",
        false=[
        "foo = [[];",
        "foo.empty();",
        "foo.slice(0, foo.length);",
        ],
        explanation="""
        JavaScript's native splice method modifies a referenced array in place by removing and (optionally) adding elements. splice's first parameter indicates the index at which to begin removing elements, the second indicates how many elements to remove, while the third can be any number of elements to add to the array in their place. So by invoking splice with 0 and Array.length, and by omitting the 3rd, parameter we can reliably empty an array of any length. Another method of emptying an array that works just as well, is to explicitly set the length of the array to 0, i.e. foo.length = 0;.

        The foo = [[]; method would not truly empty the array. Instead, it would have only reassigned the variable foo to a new array object. The original array that foo used to point to would still exist in memory, and any other references to that array, such as bar in this case, would be unaffected.

        slice is better suited to copying arrays, and is not appropriate for this use case. Array.empty() is not a native JavaScript method, so this solution would fail.
        """
        ),

    QuizQuestion(
        question="What will the following code output to the console?",
        true="super",
        false=[
        "null",
        "cool",
        "undefined",
        ],
        code_label='js_code3',
        explanation=_p("""
        This code logs super to the console even though a is never defined in the inner function bar, because bar has closure over the outer function foo.

        When a function is defined inside of another function, it is said to have "closure" over that function, meaning that it has access to the variables defined in the outer function's scope. When execution reaches the console.log() statement, JavaScript searches bar's scope for a variable called a. When it does not find one, it then searches the scope "bubble" that is the next level up, in this case, the scope created by foo. If a was not defined in foo, the search would continue, moving up to the next scope. If the outer-most, or global scope is reached and a variable is still not found, JavaScript will throw a ReferenceError.

        If the way that these functions are called tripped you up, here's the explanation: foo is an immediately invoked function expression (or IIFE), invoked by the parentheses that contain 'super'. This expression resolves before anything else occurs, and since it resolves to the function bar, the second set of parentheses are simply invoking that function, and thus the console.log() statement is executed.
        """)
        ),

    QuizQuestion(
        question="What will the following code log to the console?",
        true="true\nfalse",
        false=[
        "false\ntrue",
        "false\nfalse",
        "true\ntrue"
        ],
        code_label='js_code4',
        explanation="""
        The first expression will evaluate to true since the == operator performs a non-strict comparison, meaning that if the 2 values are not of the same type, JavaScript will attempt to coerce the values into comparable types. In this case, JavaScript will coerce 0 into to a boolean, and since 0 is falsy in JavaScript, it will coerce to false.

        The === operator, on the other hand, represents strict equality, meaning that no type coercion will take place. To evaluate to true, the values on either side of this symbol must be of the same type and value. This means that the second expression evaluates to false — since false and 0 are not of the same type, no further comparison is necessary.

        Note that these principles hold true for JavaScript's inequality operators as well, non-strict: !=, strict: !==.
        """
        ),

    QuizQuestion(
        question="This code does not work correctly, it simply prints five 5s to the console. How can we use ES6 to fix this problem so that the code works as expected?",
        true="By replacing the var keyword with let",
        false=[
        "By replacing the function keyword with => syntax",
        "By replacing the var keyword with const",
        "None of these answers are correct"
        ],
        code_label='js_code5',
        explanation="""
        The major advantages of the let keyword introduced in the ECMAScript 2015 specification is the ability to "block scope" a variable to a specific block, statement, or expression. This is unlike the var keyword which creates a variable that is scoped globally to the context it is defined in — either a function or the global scope. In the case of this code, replacing var with let block scopes let to the for loop, so that each iteration refers to a new instance of the variable i, and 0-4 is printed to the console as expected.

        Prior to ES6, the best solution for this problem was to create a local scope around or within the setTimeout function and passing in the value of i during each iteration of the loop. For example, by wrapping setTimeout in an IIFE and invoking it with i.
        """
        ),

    QuizQuestion(
        question="What will the following code output to the console?",
        true='"022"\n"221-1"',
        false=[
        '4\n4',
        '"04"\n"220"',
        '"022"\n"220"'
        ],
        code_label='js_code6',
        explanation="""
        What makes this code a bit tricky is the fact that JavaScript is a "weakly" or "loosely" typed language. This means that, in part, JavaScript will allow operations to be performed on values that are not of the same data types, and as a result, it will "coerce" values that are not of the same type in order to accomodate the operation. This has a significant impact on the above code snippets. Let's look at each example in turn.

        Ex: console.log(1 + -"1" + "2" - "2");
        In JavaScript, the negation symbol, e.g. -x, is treated as a unary operator, and, according to order of operations precedence, is evaluated before the four standard mathematical operators (+, -, /, *). Thus in this snippet, the first operation performed is the negation of "1". Since this value is a string, to accomodate this operation, "1" is converted to a number. From here, the expression is evaluated from left to right, since all other operators are treated equally in precedence. First 1 is added to -1, resulting in 0, followed by 0 + "2" . However, since one of these two values is a string, the remaining value is coerced into a string, and concatenation is performed rather than addition. Now we are left with "02" + "2" , a simple string concatenation with no coersion necessary, giving us the final result of "022"

        Ex: console.log("2" + "2" + 1 + -"1");
        This example is nearly identical. However, even though "1" is coerced into a number before any other operations are performed, -1 is then coerced back into a string since it is a part of the final evaluation: "2" + "2" results in "22", "22" + 1 results in "221", and "221" + -1 gives us "221-1".
        """
        ),

    QuizQuestion(
        question="What will the following code log to the console?",
        true="undefined",
        false=[
        "ReferenceError: x is not defined",
        "TypeError: x is not defined",
        "ReferenceError: x is undefined"
        ],
        code_label='js_code7',
        explanation="""
        undefined refers to a variable that has been declared but not yet assigned a value. not defined is a ReferenceError, thrown when a variable is encountered that has not yet been declared.

        If you were to comment out the first line var x; and run the code again, ReferenceError: x is not defined would be thrown.
        """
        ),

    QuizQuestion(
        question="What is the difference between == and === in JavaScript?",
        true="== represent abstract equality and allows type coercion, whereas === uses strict equality and will not coerce its arguments.",
        false=[
        "=== can be used to test deep equality of arrays and objects, whereas == cannot.",
        "None of these are correct.",
        "These operators are interchangeable and both test for equality."
        ],
        explanation="""
        The difference between these two equality operators is that the first allows type coercion and the second does not. Because JavaScript is a loosely typed language, the abstract equality operator can establish equality between dissimilar types. For instance, "2" == 2 evaluates to true, however, this would fail under a check of strict equality. Generally, strict equality is safer and preferred, but it's good to understand the difference between these two equality operators.
        """
        ),

    ]

    web_questions = [

    QuizQuestion(
        question="What service do CDNs provide?",
        true="A CDN (content delivery or distribution network) is designed to provide web content with high availability and high performance.",
        false=[
        "A CDN makes real-time communication between web clients very efficient.",
        "CDNs are responsible for routing web requests to destination servers.",
        "None of these are correct."
        ],
        explanation="""
        A CDN is a content delivery network primarily responsible for serving static web assets in a very performant manner. CDNs can reduce server traffic by handling specific requests and are often geographically distributed in a way to handle requests more efficiently. A large percentage of web traffic is served via CDNs today.
        """
        ),

    QuizQuestion(
        question="Which HTTP status code is reserved for successful responses?",
        true="200",
        false=[
        "500",
        "404",
        "303",
        "505"
        ],
        explanation="The 200 status codes are reserved for client requests that are received and successfully processed by a server."
        ),

    QuizQuestion(
        question="___ is the HTTP status code for client errors, and ___ is the status code for server errors.",
        true="400, 500",
        false=[
        "200, 400",
        "200, 500",
        "200, 300",
        "300, 500"
        ],
        explanation="Any 400 status is used for client errors (unauthorized, bad request, not found, etc), and 500 status is used for servers errors (internal server error, bad gateway, etc.)."
        ),

    QuizQuestion(
        question="What role does the Domain Name System play in resolving web traffic?",
        true="The DNS is responsible for resolving web domain names to the actual IP addresses where the associated service is located.",
        false=[
        "The DNS system plays an important role re-routing server traffic when a single server becomes over-loaded.",
        "The DNS is responsible for breaking internet traffic into small packets to be sent to web clients.",
        "The DNS system is responsible for verifying SSL security certificates."
        ],
        explanation="""
        The Domain Name System maps domain names to the underlying IP addresses which are responsible for actually serving web traffic. This allows web addresses to be represented by a single, human-readable domain (e.g. freecodecamp.com), while behind the scenes freeCodeCamp servers may exist at one or more IP addresses which are mapped to the domain name by the DNS system when a user visits freecodecamp.com.
        """
        ),

    QuizQuestion(
        question="How many classes of HTTP status codes are there?",
        true="Five",
        false=["Two", "Three", "Four", "One"],
        explanation="""
        There are five different classes of HTTP status codes, represented by 100, 200, 300, 400, and 500. Each is used to specify a different server response to a client during use of the Hypertext Transfer Protocol (HTTP). 
        """
        ),

    ]

    algorithm_questions = [

    QuizQuestion(
        question="What is the distinguishing characteristic of a `pure function`?",
        true="A pure function has no side effects and given the same arguments always returns the same result.",
        false=[
        "A pure function directly returns a result without calling any other functions.",
        "A pure function is a function that modifies a global variable, and does nothing else.",
        "A function is `pure` if it only accepts a single argument.",
        "None of these answers are correct."
        ],
        explanation="""
        Pure functions are crucial elements of functional programming. In this paradigm, a pure function is conceptually similar to a mathematical function. It will determine a result solely based on its input values, and given those same input parameters again, it will return the same result. This property allows a pure function to exist independently of the state of system surrounding it. It doesn't rely on the state of outside variables and it also does not directly modify any variables in its outer scope. This property also means the function can be memoized, which is a common method of improving performance. 
        """
        ),

    QuizQuestion(
        question="What principle does the following function illustrate?",
        true="Recursion",
        false=[
        "Dynamic Programming",
        "Memoization",
        "Object-Oriented Programming",
        "Imperative Programming"
        ],
        code_label='js_code8',
        explanation="""
        This demonstrates recursion, a programming technique where a function calls itself. Here, we are searching through a binary tree structure looking for a node. At each node, if we can't find the target value and that node has child nodes, we call the parent function again with the appropriate child node as input. This continues until the function finds the target node or reaches a leaf node and terminates.
        """
        ),

    QuizQuestion(
        question="What is the time complexity of the following function?",
        true="O(n)",
        false=["O(log(n))", "O(1)", "O(n*log(n))", "O(n^2)"],
        code_label='js_code9',
        explanation="""
        This function takes an array and a target element and searches for the element in the array. It iterates through the array with a for-loop, and in the worst case must visit every item in the array. This gives this function linear time complexity. That is, the time complexity will increase in a linear manner in relation to the size of the input. If the input increases by 1000, this solution may loop 1000 times more — there is a linear relationship between the algorithm's performance and the size of the input.
        """
        ),

    QuizQuestion(
        question="What principle does the following function illustrate?",
        true="Memoization",
        false=[
        "Recursion",
        "Prototypal Inheritance",
        "Object Composition"
        ],
        code_label='js_code10',
        explanation="""
        This code demonstrates memoization. createSearchFunction returns a new function that has closure over a cache, which is simply a fast, constant-time lookup table. The function sees if a parameter exists in the cache as a key, if it does it returns the associated value. If not, it computes the value, saves the parameter and result in the cache, and then returns the result. In this way, if it subsequently encounters the same parameter again, it can quickly return the cached result and forego the expensive computation. This pattern is a very useful way to improve the performance of computationally expensive functions.         """
        ),

    QuizQuestion(
        question="A complex problem which can be broken down into repeating sub-problems can be solved by a method known as:",
        true="Dynamic Programming",
        false=["Recursion", "Functional Composition", "Multithreaded Programming"],
        explanation="""
        Some complex problems can be divded into smaller, repeating sub-problems. These are ideal candidates for the method of dynamic programming, in which the sub-problems are solved and used to dynamically build up a solution to the more complex problem. This is a more advanced programming method but can be very useful in solving problems which otherwise would not be possible by brute force approaches.
        """
        ),

    ]

    system_questions = [

    QuizQuestion(
        question="What problem does a load balancer solve?",
        true="Load balancers can distribute incoming traffic to one of many servers, allowing one to scale a server architecture to support a high volume of traffic.",
        false=[
        "A load balancer determines how to route requests between clients and servers.",
        "None of these are correct.",
        "If traffic reaches a certain level load balancers will start throttling traffic to prevent servers from crashing."
        ],
        explanation="Load balancers optimize resource use by distributing requests or traffic evenly among many computers. This is commonly used in serving web traffic to a number of servers after the point where a single server is unable to handle the amount of incoming traffic. The load balancer acts as an intermediary which distributes incoming requests to one of many servers, and in this way is an important scaleability tool."
        ),

    QuizQuestion(
        question="Caching is an important method to improve web application performance. Which of the following are popular caching technologies that exist at the server/database interface?",
        true="Redis and Memcached",
        false=["CDNs", "Docker", "Kubernetes", "Elasticsearch"],
        explanation="""
        Redis and Memcached are two of the most common caching solutions for database queries. They are key-value pair in-memory datastores that allow you to cache the results of database queries to prevent subsequent requests from performing the same database query again. The use of these technologies can often offer sizable performance improvements to database heavy web applications.
        """
        ),

    QuizQuestion(
        question="When scaling a server architecture, it is important to use redundancy to protect against: ",
        true="Single points of failture",
        false=[
        "System fragility",
        "Network vulnerabilities",
        "Security exploits"
        ],
        explanation="""
        Introducing a load balancer, for instance, creates a single point that, if compromised, could compromise the entire system. Because of this, it is important to use redundancy to guard against these single points of failure. Now, if one of these components fails the backup system could be transitioned in through a process known as "failover".
        """
        ),

    QuizQuestion(
        question="What is continuous integration?",
        true="Continuous integration is a software development practice that involves frequent incorporation of code changes to a shared repository, and usually involves an automated build and testing process.",
        false=[
        "None of these are correct.",
        "Continuous integration is a process where tests are written for a project and all subsequent code is written in order to pass the tests.",
        "Continuous integration is the agile methodology practice of deploying production code frequently, usually at least once per sprint."
        ],
        explanation="""
        Continuous integration (CI) is the practice of frequently integrating local code changes with a shared code repository. The main idea is to speed up the development/release lifecycle and improve the ability of developers to identify and address bugs. CI is often associated with an automated build and testing process, which additionally helps to catch bugs quickly and earlier.
        """
        ),

    QuizQuestion(
        question="A system designed with several different services that are all isolated and managed independently is referred to as",
        true="A microservices architecture.",
        false=[
        "A dynamic architecture.",
        "A monolithic architecture.",
        "A component architecture."
        ],
        explanation="""
        Microservices are commonly contrasted with the so-called monolithic architecture. In the former, different tasks or services are broken up into independent, isolated services, all of which interact with each other. In the other approach, everything involved in an application is consolidated into one architecture. Both approaches have their own advantages and disadvantages.
        """
        ),

    ]

    # TODO: more fine-grained category
    interview_questions = javascript_questions + web_questions + algorithm_questions + system_questions

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
        question="Which of the following programming languages is created by a Japanese?",
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