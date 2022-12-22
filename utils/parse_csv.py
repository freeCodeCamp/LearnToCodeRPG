import csv
import json

# Learn to Code RPG Quiz Questions - CSS.csv
# Learn to Code RPG Quiz Questions - General CS Concepts.csv
# Learn to Code RPG Quiz Questions - Git.csv
# Learn to Code RPG Quiz Questions - HTML.csv
# Learn to Code RPG Quiz Questions - IT.csv
# Learn to Code RPG Quiz Questions - JavaScript.csv
# Learn to Code RPG Quiz Questions - Linux.csv
# Learn to Code RPG Quiz Questions - Python.csv
# Learn to Code RPG Quiz Questions - SQL.csv
# Learn to Code RPG Quiz Questions - freeCodeCamp.csv
for name in ['CSS', 'General CS Concepts', 'Git', 'HTML', 'IT', 'JavaScript', 'Linux', 'Python', 'SQL', ]:
    file = 'Learn to Code RPG Quiz Questions - {}.csv'.format(name)

    ret = []
    # i = 0
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # XXX: difficulty={Difficulty (1 - 5)} can't parse
            # .replace('[', '[[').replace('{', '{{')
            # replace('%', '%%')
            obj = {}
            obj['question'] = row['Question'].replace('"', r'\"').replace('[', '[[').replace('{', '{{')
            obj['true'] = row['Correct answer'].replace('"', r'\"').replace('[', '[[').replace('{', '{{')
            obj['explanation'] = row['Explanation'].replace('"', r'\"').replace('[', '[[').replace('{', '{{')
            obj['false1'] = row['Distractor 1'].replace('"', r'\"').replace('[', '[[').replace('{', '{{')
            obj['false2'] = row['Distractor 2'].replace('"', r'\"').replace('[', '[[').replace('{', '{{')
            obj['false3'] = row['Distractor 3'].replace('"', r'\"').replace('[', '[[').replace('{', '{{')
            obj['link'] = row['Learn more link']
            obj['difficulty'] = row['Difficulty (1 - 5)']

            # if i == 3:
            #     break
            s = """
            QuizQuestion(
            question="{question}",
            true="{true}",
            false=["{false1}", "{false2}", "{false3}"],
            explanation="{explanation}",
            learn_more_url="{link}",
            difficulty={difficulty},
            )""".format(**obj)
            # print(s)
            # print(row)
            # i += 1
            ret.append(s)

    with open('out_{}.txt'.format(name), 'wt') as f:
        f.write(','.join(ret))