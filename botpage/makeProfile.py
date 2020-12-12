import csv
import random
from botpage import factProcessor, myIdolUtility, csvPaths
from factGenerators import foodFactGenerator, mottoFactGenerator, movieFactGenerator, representativeFactGenerator, charmFactGenerator, simpleFactGenerator


def makeFactsList():
    factsfile = open(csvPaths.factsPath, 'r', encoding="utf8")
    numRandomFacts = random.randint(5, 7)
    numFoodFacts = random.randint(0, 2)
    numMottoFacts = random.randint(0, 1)
    numMovieFacts = random.randint(0, 2)
    numRepresentativeFacts = random.randint(0, 2)
    numCharmFacts = random.randint(0, 2)
    simpleFactsChance = 0.3
    factsList = []

    # General facts
    with factsfile:
        factsReader = csv.reader(factsfile)
        chances = numRandomFacts / 3000
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
    factsList += charmFactGenerator.getFacts(numCharmFacts)
    factsList += simpleFactGenerator.getFacts(simpleFactsChance)

    random.shuffle(factsList)

    processedFactsList = []
    for unprocessedFact in factsList:
        processedFact = factProcessor.processFact(unprocessedFact)
        processedFactsList.append(processedFact)
    return processedFactsList


def makeProfile(userIdolName, userGroupName):
    profile = myIdolUtility.initialize()

    # if userIdolName:
    #     idolNames[0] = userIdolName
    # if userGroupName:
    #     groupNames[0] = userGroupName
    profile.facts = makeFactsList()
    return profile


def printProfile(profile):
    print(profile.name + " (" + profile.group + ")")
    print(*profile.positions, sep = ", ")
    print("Age: " + str(myIdolUtility.getAge()) + " (born " + profile.birthDateString + ")")
    print("Debuted: " + profile.debutDateString)
    print(profile.sign)
    print(profile.bloodType)
    print(profile.MBTI)
    print("\n")
    print(*profile.facts, sep = "\n")


printProfile(makeProfile(False, False))
