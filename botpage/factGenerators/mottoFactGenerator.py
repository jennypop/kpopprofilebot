import csv
import random
import re
from botpage import csvPaths, factProcessor

words = {"lifeStage": ["in elementary school", "in secondary school", "in high school", "as a trainee"]}

factTemplates = ["!HER! ((life ))motto {[lifeStage] was/is}((:)) ",
"Motto: ", ]


def getMottos():
    mottoPath = csvPaths.mottoPath
    mottofile = open(mottoPath, 'r', encoding="utf8")
    mottos = []

    with mottofile:
        mottoReader = csv.reader(mottofile)
        for line in mottoReader:
            mottos.append(line[0])
    return mottos


mottos = getMottos()


def processFactTemplate(txt):
    txt = factProcessor.processABCChoice(txt)
    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)
    txt = txt + '"' + random.choice(mottos) + '"'
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