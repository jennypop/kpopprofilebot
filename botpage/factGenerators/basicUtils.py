import csv
import random
import re
from botpage import factProcessor


def getFromCSV(path):
    file = open(path, 'r', encoding="utf8")
    x = []

    with file:
        reader = csv.reader(file)
        for line in reader:
            x.append(line[0])
    return x


def processFactTemplateBasic(txt, words):
    txt = factProcessor.processFactEarly(txt)

    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)
    return txt


def addSuffix(txt, chance, suffixTable, joiner):
    if random.random() < chance:
        txt += joiner + random.choice(suffixTable)
    return txt


def debug(factTemplates, processFactTemplateF):
    for i in range(10):
        txt = random.choice(factTemplates)
        txt = processFactTemplateF(txt)
        print(txt)


def getFacts(n, factTemplates, processFactTemplateF):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplateF(txt) for txt in factList]
    return processedList
