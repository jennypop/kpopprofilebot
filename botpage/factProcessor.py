import random
import re
from botpage import idolData


replaceWords = {}
replaceWordsMultipleChoice = {
    "closePerson": ["!HER! mom", "!HER! dad", "!MEMBERNAME!", "!HER! sister", "!HER! brother", "!HER! grandmother", "!HER! grandpa", "!HER! manager"],
    "wasWere": ["was", "were"],
    "whenSituation": ["when !SHE! is alone", "when !SHE! is with others", "when !SHE! is at home", "when the night comes", "when !SHE! can't sleep", "before going to bed", "from her bed", "at the cinema", "when she feels good", "when she feels down", "on the first day of each month", "when watching a movie", ],
    "timePeriod": ["a month", "two months", "three months", "a week", "two weeks", "half a year", "a year", "the rest of !HER! life"],
    "oftenTimePeriod": ["once a month", "every day", "every week", "twice a week", "every two weeks", "once every few days", "every year", "twice a year", "a few times a year", "once every few months", "multiple times a day"],
    "shortTimePeriod": ["five seconds", "a minute", "three minutes", "the blink of an eye", "ten minutes", "twenty seconds"],
    "positiveAdjective": ["relaxing", "comfortable", "refreshing"],
    "prefixCombiner": [" and ", ", ", ": "],
    "exceptBut": ["except", "but"],
}
idolName = ""
idolGroup = ""


def initializeForIdol(gender, idolNames, groupNames):
    initializeReplaceWordsTable(gender, idolNames, groupNames)
    global idolName
    global idolGroup
    idolName = idolNames[0]
    idolGroup = groupNames[0]


def initializeReplaceWordsTable(
    gender,
    idolNames,
    groupNames
):
    # Replace gendered pronouns
    replaceWords["!SHE!"] = "he" if gender else "she"
    replaceWords["!HER!"] = "his" if gender else "her"
    replaceWords["!HERHIM!"] = "him" if gender else "her"
    replaceWords["!HERSELF!"] = "himself" if gender else "herself"

    replaceWordsMultipleChoice["!COMPANYNAME!"] = idolData.companyAll
    replaceWordsMultipleChoice["!SURVIVALSHOWNAME!"] = idolData.survivalShowAll
    replaceWordsMultipleChoice["!TVSHOWNAME!"] = idolData.tvShowAll
    replaceWordsMultipleChoice["!IDOLNAME!"] = idolNames[1:]
    replaceWordsMultipleChoice["!GROUPNAME!"] = groupNames[1:]
    replaceWordsMultipleChoice["!SUBUNITNAME!"] = groupNames[1:]


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
    # Process "(x)*d(w)" pattern
    txt = processAsterisk(txt)

    # Process "{A/B/C}"" pattern
    txt = processABCChoice(txt)

    # Replace numbers and dates
    txt = txt.replace("!SMALLINT!", str(random.randint(1, 20)))

    # Replace ((x)) with nothing half of the time
    matchParen = re.compile(r"\(\(([^)]*)\)\)")
    txt = matchParen.sub(lambda match: random.choice([match.group(1), ""]), txt)

    # Replace names - TODO look at this again
    uniqueIdolNames = txt.count("!IDOLNAME!")
    uniqueIdolNames2 = txt.count("!MEMBERNAME!")
    if uniqueIdolNames > 0:
        idolNamesUsing = random.sample(replaceWordsMultipleChoice["!IDOLNAME!"], uniqueIdolNames + uniqueIdolNames2)
        for i in range(uniqueIdolNames):
            txt = txt.replace("!IDOLNAME!", idolNamesUsing[i], 1)
        for i in range(uniqueIdolNames2):
            txt = txt.replace("!MEMBERNAME!", idolNamesUsing[i], 1)

    uniqueGroupNames = txt.count("!GROUPNAME!")
    uniqueGroupNames += txt.count("!SUBUNITNAME!")
    if uniqueGroupNames > 0:
        groupNamesUsing = random.sample(replaceWordsMultipleChoice["!GROUPNAME!"], uniqueGroupNames)
        groupNamesUsing[0] = idolGroup
        for i in range(uniqueGroupNames):
            txt = txt.replace("!GROUPNAME!", groupNamesUsing[i], 1)
        for i in range(uniqueGroupNames):
            txt = txt.replace("!SUBUNITNAME!", groupNamesUsing[i], 1)

    # Replace replaceWordsMultipleChoice table
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(replaceWordsMultipleChoice)))
    txt = matchKeys.sub(lambda match: random.choice(replaceWordsMultipleChoice[match.group(1)]), txt)
    matchKeys = re.compile(r'({})'.format('|'.join(replaceWordsMultipleChoice)))
    txt = matchKeys.sub(lambda match: random.choice(replaceWordsMultipleChoice[match.group(1)]), txt)

    # Replace replaceWords table
    matchKeys = re.compile(r'({})'.format('|'.join(replaceWords)))
    txt = matchKeys.sub(lambda match: replaceWords[match.group(1)], txt)

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
