import csv
import random
import re
import csvPaths, factProcessor

words = {"habit": ["bad habit", "frequent habit", "unusual habit", "habit"],
"habitSuffix": [" when no-one is looking(( at !HER!))",
" when !SHE! is alone",
" when !SHE! is around others", ],
"suffix": ["The members said it was ((kind of ))serious",
"It was a habit !SHE! got from [closePerson]",
"[closePerson] tried to give !HER! an intervention"]}

factTemplates = ["A [habit] !SHE! has is [habiting]",
"!HER! [habit] is [habiting]",
"!SHE! has(( developed)) a [habit] of [habiting]",
"!SHE! can never drop !HER! [habit] of [habiting]",
"!SHE! used to have a [habit] of [habiting], but ((!SHE! says ))!SHE! doesn't do it anymore",
"!SHE! wants to fix !HER! [habit] of [habiting]",
"[habiting] is one of !HER! [habit]s",
"!SHE! doesn't have [habit]s", ]


def getHabits():
    habitPath = csvPaths.habitPath
    habitfile = open(habitPath, 'r', encoding="utf8")
    habits = []

    with habitfile:
        habitReader = csv.reader(habitfile)
        for line in habitReader:
            habits.append(line[0])
    return habits


words["habiting"] = getHabits()


def processFactTemplate(txt):
    txt = factProcessor.processFactEarly(txt)

    pickHabit = random.choice(words["habiting"])
    if random.random() < 0.1:
        pickHabit += random.choice(words["habitSuffix"])
    txt = txt.replace("[habiting]", pickHabit)

    if random.random() < 0.1:
        txt += ". " + random.choice(words["suffix"])

    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)
    return txt


def debug():
    for i in range(10):
        txt = random.choice(factTemplates)
        txt = processFactTemplate(txt)
        print(txt)


def getFacts(n):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
