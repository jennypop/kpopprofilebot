import random
import re
import inflect
from botpage import myIdolUtility


def processFactEarly(txt):
    txt = processAsterisk(txt)
    txt = processABCChoice(txt)
    return txt


def processAsterisk(txt):
    # Match "(x)*d(w)". Group 1 = X , Group 2 = d, Group 3 = W
    # Example: "([food])*3(, )" -> "food" or "food, food" or "food, food, food"
    matchParenAsterisk = re.compile(r"\(([^)]*)\)\*([0-9])\(([^)]*)\)")
    matches = re.finditer(matchParenAsterisk, txt)
    for match in matches:
        phraseToRepeat = match.group(1)
        timesToRepeat = int(match.group(2))
        joiningWord = match.group(3)

        listPhrase = [phraseToRepeat] * random.randint(1, timesToRepeat)
        newPhrase = joiningWord.join(listPhrase)
        txt = txt[:match.start()] + newPhrase + txt[match.end():]
    return txt


def processABCChoice(txt):
    # Match "{a/b/c}" -> a or b or c
    matchABCChoice = re.compile(r"\{([^\/\}]*)\/([^\/\}]*)\/?([^\/\}]*)?\/?([^\}]*)?\}")
    matches = re.finditer(matchABCChoice, txt)
    for match in matches:
        phraseChoices = [match.group(1), match.group(2)]
        if match.group(3) is not None and match.group(3):
            phraseChoices.append(match.group(3))
        if match.group(4) is not None and match.group(4):
            phraseChoices.append(match.group(4))
        txt = txt.replace(match.group(0), random.choice(phraseChoices))
    return txt


def processFact(
    txt
):
    p = inflect.engine()
    # Process "(x)*d(w)" pattern
    txt = processAsterisk(txt)

    # def lookupMatch(match, dicti):
    #     # print(match.group(1))
    #     return random.choice(dicti[match.group(1)])

    matchKeys = re.compile(r'\[({})\]'.format('|'.join(myIdolUtility.dictRandom)))
    txt = matchKeys.sub(lambda match: random.choice(myIdolUtility.dictRandom[match.group(1)]), txt)
    matchKeys = re.compile(r'({})'.format('|'.join(myIdolUtility.dictRandomNoBrackets)))
    txt = matchKeys.sub(lambda match: random.choice(myIdolUtility.dictRandomNoBrackets[match.group(1)]), txt)

    # Do substition twice to make up for embedded []
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(myIdolUtility.dictRandom)))
    txt = matchKeys.sub(lambda match: random.choice(myIdolUtility.dictRandom[match.group(1)]), txt)
    matchKeys = re.compile(r'({})'.format('|'.join(myIdolUtility.dictRandomNoBrackets)))
    txt = matchKeys.sub(lambda match: random.choice(myIdolUtility.dictRandomNoBrackets[match.group(1)]), txt)

    # Replace dictSingle table
    matchKeys = re.compile(r'({})'.format('|'.join(myIdolUtility.dictSingle)))
    txt = matchKeys.sub(lambda match: myIdolUtility.dictSingle[match.group(1)], txt)

    # Replace numbers and dates
    txt = txt.replace("!SMALLINT!", str(random.randint(2, 7)))
    txt = txt.replace("!SMALLINTW!", p.number_to_words(random.randint(2, 7)))
    txt = txt.replace("!HUGENUMBER!", str(random.randint(1000000, 150000000)))
    txt = txt.replace("!HIGHRANK!", myIdolUtility.getRandomRank(1, 12))
    txt = txt.replace("!VERYHIGHRANK!", myIdolUtility.getRandomRank(1, 5))
    txt = txt.replace("!RANK100!", myIdolUtility.getRandomRank(1, 100))
    txt = txt.replace("!RANK!", myIdolUtility.getRandomRank(1, 150))
    txt = txt.replace("!SCHOOLGRADE!", myIdolUtility.getRandomSchoolGrade())
    txt = txt.replace("!YEAR!", str(random.randint(2003, 2019)))
    dateFormats = ["", "Y", "YM"]
    for dateFormat in dateFormats:
        txt = txt.replace("!PRETRAINEEDATE" + dateFormat + "!", myIdolUtility.getPreTraineeDate(dateFormat))
        txt = txt.replace("!PREDEBUTDATE" + dateFormat + "!", myIdolUtility.getPreDebutDate(dateFormat))
        txt = txt.replace("!ACTIVEDATE" + dateFormat + "!", myIdolUtility.getActiveDate(dateFormat))

    # Replace names - TODO look at this again
    uniqueIdolNames = txt.count("!IDOLNAME!")
    uniqueIdolNames2 = txt.count("!MEMBERNAME!")
    if uniqueIdolNames + uniqueIdolNames2 > 0:
        idolNamesUsing = random.sample(myIdolUtility.dictRandomNoBrackets["!IDOLNAME!"], uniqueIdolNames + uniqueIdolNames2)
        for i in range(uniqueIdolNames):
            txt = txt.replace("!IDOLNAME!", idolNamesUsing[i], 1)
        for i in range(uniqueIdolNames2):
            txt = txt.replace("!MEMBERNAME!", idolNamesUsing[i], 1)

    uniqueGroupNames = txt.count("!GROUPNAME!")
    uniqueGroupNames += txt.count("!SUBUNITNAME!")
    if uniqueGroupNames > 0:
        groupNamesUsing = random.sample(myIdolUtility.dictRandomNoBrackets["!OTHERGROUPNAME!"], uniqueGroupNames)
        groupNamesUsing[0] = myIdolUtility.myIdolData.group
        for i in range(uniqueGroupNames):
            txt = txt.replace("!GROUPNAME!", groupNamesUsing[i], 1)
            txt = txt.replace("!IDOLGROUP!", groupNamesUsing[i], 1)
            txt = txt.replace("!MYGROUPNAME!", groupNamesUsing[i], 1)
        for i in range(uniqueGroupNames):
            txt = txt.replace("!SUBUNITNAME!", groupNamesUsing[i], 1)

    # Process "{A/B/C}"" pattern
    txt = processABCChoice(txt)

    # Replace ((x)) with nothing half of the time
    # Note: Cannot have embedded ((x ((and y)))) bc of greediness
    matchParen = re.compile(r"\(\(([^)]*)\)\)")
    txt = matchParen.sub(lambda match: random.choice([match.group(1), ""]), txt)

    # Formatting
    txt = formatFact(txt)

    return txt


def formatFact(fact):
    if (random.random() < 0.9):
        fact = fact[:1].upper() + fact[1:]
    if (random.random() < 0.95):
        fact = "- " + fact
    elif (random.random() < 0.5):
        fact = "-" + fact
    else:
        fact = "-  " + fact
    return fact
