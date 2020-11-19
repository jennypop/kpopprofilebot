import csv
import random
from . import idolData


final = True


def getIdolNames():
    bioPath = '/home/kpopprofilebot/botsite/botpage/idolbio.csv' if final else "idolbio.csv"
    biofile = open(bioPath, 'r', encoding="utf8")
    idolNamesAll = {}

    with biofile:
        bioReader = csv.reader(biofile)
        for line in bioReader:
            if len(line) > 0 and line[0].isalpha and len(line[0]) > 2:
                idolNamesAll[line[0]] = line[4]
    return idolNamesAll


def getGroupNames():
    groupsPath = '/home/kpopprofilebot/botsite/botpage/idolgroups.csv' if final else "idolgroups.csv"
    groupsfile = open(groupsPath, 'r', encoding="utf8")
    groupNamesAll = []

    with groupsfile:
        groupsReader = csv.reader(groupsfile)
        for line in groupsReader:
            if len(line) > 0 and len(line[0]) > 0:
                groupNamesAll.append(line[0])
    return groupNamesAll


def makePositionsList():
    numPositions = 1
    weirdPositions = 0
    if (random.random() < 0.5):
        numPositions += 1
    if (random.random() < 0.5):
        numPositions += 1
    if (random.random() > 0.9):
        weirdPositions += 1
    if (random.random() > 0.9):
        weirdPositions += 1
    return random.sample(idolData.idolPositionsAll, numPositions) + random.sample(idolData.idolPositionsFun, weirdPositions)


def processFact(
    unprocessedFact,
    gender,
    idolNames,
    groupNames
):
    unprocessedFact = unprocessedFact.replace("!SHE!", "he" if gender else "she")
    unprocessedFact = unprocessedFact.replace("!HER!", "his" if gender else "her")
    unprocessedFact = unprocessedFact.replace("!HERSELF!", "himself" if gender else "herself")

    uniqueIdolNames = unprocessedFact.count("!IDOLNAME!")
    if uniqueIdolNames > 0:
        idolNamesUsing = random.sample(idolNames[1:], uniqueIdolNames)
        for i in range(uniqueIdolNames):
            unprocessedFact = unprocessedFact.replace("!IDOLNAME!", idolNamesUsing[i], 1)

    uniqueGroupNames = unprocessedFact.count("!GROUPNAME!")
    uniqueGroupNames += unprocessedFact.count("!SUBUNITNAME!")
    if uniqueGroupNames > 0:
        groupNamesUsing = random.sample(groupNames[1:], uniqueGroupNames)
        groupNamesUsing[0] = groupNames[0]
        for i in range(uniqueGroupNames):
            unprocessedFact = unprocessedFact.replace("!GROUPNAME!", groupNamesUsing[i], 1)
        for i in range(uniqueGroupNames):
            unprocessedFact = unprocessedFact.replace("!SUBUNITNAME!", groupNamesUsing[i], 1)

    unprocessedFact = unprocessedFact.replace("!COMPANYNAME!", random.choice(idolData.companyAll))
    unprocessedFact = unprocessedFact.replace("!SURVIVALSHOWNAME!", random.choice(idolData.survivalShowAll))
    unprocessedFact = unprocessedFact.replace("!TVSHOWNAME!", random.choice(idolData.tvShowAll))
    unprocessedFact = unprocessedFact.replace("\n", "")
    return unprocessedFact


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


def makeFactsList(
    gender,
    idolNames,
    groupNames
):
    factsPath = '/home/kpopprofilebot/botsite/botpage/idolfacts.csv' if final else "idolfacts.csv"
    factsfile = open(factsPath, 'r', encoding="utf8")
    numFacts = 8
    factsList = []

    with factsfile:
        factsReader = csv.reader(factsfile)
        chances = numFacts / 15000
        for line in factsReader:
            if random.random() < chances:
                unprocessedFact = line[0]
                processedFact = processFact(unprocessedFact, gender, idolNames, groupNames)
                fact = formatFact(processedFact)
                factsList.append(fact)
                if len(factsList) == numFacts:
                    break
        return factsList


def makeProfile(userIdolName, userGroupName):
    profile = {}

    idolNamesAll = getIdolNames()
    groupNamesAll = getGroupNames()
    idolNames = random.sample(list(idolNamesAll.keys()), 16)
    groupNames = random.sample(groupNamesAll, 10)
    gender = True if idolNamesAll[idolNames[0]] == "M" else False

    if userIdolName:
        idolNames[0] = userIdolName
    if userGroupName:
        groupNames[0] = userGroupName
    profile["name"] = idolNames[0]
    profile["group"] = groupNames[0]
    profile["positions"] = makePositionsList()
    profile["sign"] = random.choice(idolData.astrologyAll)
    profile["bloodType"] = random.choice(idolData.bloodTypesAll if random.random() < 0.9 else idolData.bloodTypesFun)
    profile["MBTI"] = random.choice(idolData.MBTIsAll if random.random() < 0.9 else idolData.MBTIsFun)
    profile["facts"] = makeFactsList(gender, idolNames, groupNames)
    return profile


def printProfile(profile):
    print(profile["name"] + " (" + profile["group"] + ")")
    print(*profile["positions"], sep = ", ")
    print(profile["sign"])
    print(profile["bloodType"])
    print(profile["MBTI"])
    print("\n")
    print(*profile["facts"], sep = "\n")


printProfile(makeProfile(False, False))
