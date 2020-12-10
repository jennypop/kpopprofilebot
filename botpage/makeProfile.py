import csv
import random
from botpage import idolData, csvPaths, factProcessor
from factGenerators import foodFactGenerator, mottoFactGenerator, movieFactGenerator, representativeFactGenerator


def getIdolNames():
    biofile = open(csvPaths.bioPath, 'r', encoding="utf8")
    idolNamesAll = {}

    with biofile:
        bioReader = csv.reader(biofile)
        for line in bioReader:
            if len(line) > 0 and line[0].isalpha and len(line[0]) > 2:
                idolNamesAll[line[0]] = line[4]
    return idolNamesAll


def getGroupNames():
    groupsfile = open(csvPaths.groupsPath, 'r', encoding="utf8")
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


def makeFactsList(
    gender,
    idolNames,
    groupNames
):
    factProcessor.initializeForIdol(gender, idolNames, groupNames)
    factsfile = open(csvPaths.factsPath, 'r', encoding="utf8")
    numRandomFacts = random.randint(5, 7)
    numFoodFacts = random.randint(0, 3)
    numMottoFacts = random.randint(0, 1)
    numMovieFacts = random.randint(0, 2)
    numRepresentativeFacts = random.randint(0, 2)
    factsList = []

    # General facts
    with factsfile:
        factsReader = csv.reader(factsfile)
        chances = numRandomFacts / 8000
        for line in factsReader:
            if random.random() < chances:
                unprocessedFact = line[0]
                factsList.append(unprocessedFact)
                if len(factsList) == numRandomFacts:
                    break

    # Fact generators
    factsList += foodFactGenerator.getFacts(numFoodFacts)
    factsList += mottoFactGenerator.getFacts(numMottoFacts)
    factsList += movieFactGenerator.getFacts(numMovieFacts)
    factsList += representativeFactGenerator.getFacts(numRepresentativeFacts)

    random.shuffle(factsList)

    processedFactsList = []
    for unprocessedFact in factsList:
        processedFact = factProcessor.processFact(unprocessedFact)
        processedFactsList.append(processedFact)
    return processedFactsList


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
