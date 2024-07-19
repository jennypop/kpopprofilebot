import csv
import random
import csvPaths, factProcessor

factTemplates = [
"((On !INTERVIEWSHOWNAME! ))!SHE! {revealed/told fans} !HER! English name which is [EnglishName]",
"!HER! English name is [EnglishName]",
"When !SHE! lived in {the US/the UK/Australia} !SHE! used to be called by the name [EnglishName]",
]

englishNamesM = []
englishNamesF = []


def getenglishNames():
    englishNamePath = csvPaths.englishNamePath
    englishNamefile = open(englishNamePath, 'r', encoding="utf8")
    englishNamesM = []
    englishNamesF = []

    with englishNamefile:
        englishNameReader = csv.reader(englishNamefile)
        for line in englishNameReader:
            englishNamesM.append(line[0])
            englishNamesF.append(line[1])
    return englishNamesM, englishNamesF


englishNamesM, englishNamesF = getenglishNames()


def processFactTemplate(txt, gender):
    txt = factProcessor.processFactEarly(txt)

    txt = txt.replace("[EnglishName]", random.choice(englishNamesM if gender else englishNamesF))
    return txt


def debug():
    for i in range(10):
        txt = random.choice(factTemplates)
        txt = processFactTemplate(txt, False)
        print(txt)
        txt1 = random.choice(factTemplates)
        txt1 = processFactTemplate(txt1, True)
        print(txt1)


def getFacts(n, gender):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt, gender) for txt in factList]
    return processedList

