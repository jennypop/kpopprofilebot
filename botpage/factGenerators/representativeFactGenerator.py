import csv
import random
import re
from botpage import csvPaths, factProcessor

words = {"flower": [],
        "weapon": [],
        "day": [],
        "planet": [],
        "representative": ["representative", "designated", "favorite", "lucky", "official", "most loved"],
        "colorfulObject": ["a [positiveAdjective] vitamin", "!HER! eyes", "!HER! room", "the sky", "!HER! hometown", "!HER! voice"],
        }

factTemplates = ["((!HER! ))(([representative] ))animal{ is/:} the [animal]",
"((!HER! ))(([representative] ))flower{ is/:} the [flower]",
"((!HER! ))[representative] drink{ is/:} [drink]",
"((!HER! ))[representative] fruit{ is/:} the [fruit]",
"((!HER! ))[representative] weapon{ is/:} the [weapon]",
"((!HER! ))[representative] day{ is/:} [day]",
"((!HER! ))[representative] planet{ is/:} [planet]",
"((!HER! ))[representative] number{ is/:} !LUCKYNUMBER!",
"((!HER! ))[representative] color{ is/:} ([color])*2( and )(( because it's the color of [colorfulObject]))",
]
factReasons = ["because !SHE! finds it ([positiveAdjective])*2( and )"]

def getWords():
    representativePath = csvPaths.representativePath
    representativefile = open(representativePath, 'r', encoding="utf8")

    with representativefile:
        representativeReader = csv.reader(representativefile)
        next(representativeReader)
        for line in representativeReader:
            if (line[1]):
                words["flower"].append(str(line[1]))
            if (line[4]):
                words["weapon"].append(str(line[4]))
            if (line[5]):
                words["day"].append(str(line[5]))
            if (line[6]):
                words["planet"].append(str(line[6]))


getWords()


def getRealisticLuckyNumber():
    randFloat = abs(random.random() - random.random()) * 20
    if (random.random() < 0.1):
        randFloat += abs(random.random() - random.random()) * 50
    if (random.random() < 0.1):
        randFloat += abs(random.random() - random.random()) * 100
    if (random.random() < 0.05):
        randFloat += abs(random.random() - random.random()) * 1000
    return int(randFloat)


def addSuffix(txt):
    if "favorite" not in txt and "loved" not in txt:
        txt += "((,)) but it is not !HER! favorite"


def processFactTemplate(txt):
    factProcessor.processFactEarly(txt)
    txt = txt.replace("!LUCKYNUMBER!", str(getRealisticLuckyNumber()))
    # Use a representativeExpression
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), str(txt))
    if random.random() < 0.1:
        addSuffix(txt)
    return txt


def getFacts(n):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
