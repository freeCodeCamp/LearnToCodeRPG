'''
Input structure:
  {
    Question: "What is DevOps?",
    Answer:
      "a combination of software development and IT operations with the goal of shortening the systems development life cycle ",
    Distractor1: "a popular JavaScript library",
    Distractor2: "a popular SQL database",
    Distractor3: "a popular Python library",
    Explanation:
      "DevOps combines software development and IT operations with the goal of shortening the systems development life cycle and providing continuous delivery of software. ",
    Link: "https://www.freecodecamp.org/news/devops-engineering-course-for-beginners/"
  },

Output structure:
    QuizQuestion(
    question=_("What is RGB?"),
    true=_("A color model"),
    false=[_("An Internet Protocol"), _("HTML syntax"), _("A secret password")],
    explanation=_("RGB is an acronym that stands for red green blue. It expresses colors in terms of the amount of red, green, and blue they are made up of and uses a human counting system with integers ranging from 0-255 or a percentage ranging from (0% - 100%)."),
    learn_more_url="https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/",
    difficulty=1,
    ),
'''

import re

in_file = 'input_devops.txt'
out_file = 'output_devops.txt'

with open(in_file, 'rt') as f:
    text = f.read()

pat = re.compile(
    r"Question:[\n}\s]\s*\"(?P<question>.+)\",\n\s+Answer:[\n}\s]\s*\"(?P<true>.+)\",\n\s+Distractor1:[\n}\s]\s*\"(?P<false1>.+)\",\n\s+Distractor2:[\n}\s]\s*\"(?P<false2>.+)\",\n\s+Distractor3:[\n}\s]\s*\"(?P<false3>.+)\",\n\s+Explanation:[\n}\s]\s*\s*\"(?P<explanation>.+)\",\n\s+Link:[\n}\s]\s*\"(?P<link>.+)\""
    )

ret = []
for m in pat.finditer(text):
    data = m.groupdict()
    s = """
    QuizQuestion(
    question="{question}",
    true="{true}",
    false=["{false1}", "{false2}", "{false3}"],
    explanation="{explanation}",
    learn_more_url="{link}",
    difficulty=1,
    )""".format(**data)
    ret.append(s)

with open(out_file, 'wt') as f:
    f.write(','.join(ret))

