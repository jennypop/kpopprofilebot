import csv
import random
from botpage import factProcessor, myIdolUtility, csvPaths
from factGenerators import foodFactGenerator, mottoFactGenerator, movieFactGenerator, representativeFactGenerator, charmFactGenerator, simpleFactGenerator, habitFactGenerator, roleModelFactGenerator, englishNameFactGenerator, roommateFactGenerator, fearFactGenerator, traineeFactGenerator, languageFactGenerator, familyFactGenerator


def makeFactsList(gender):
    factsfile = open(csvPaths.factsPath, 'r', encoding="utf8")
    numRandomFacts = random.randint(5, 7)
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
    factsList += foodFactGenerator.getFacts(random.randint(0, 2))
    factsList += mottoFactGenerator.getFacts(random.randint(0, 1))
    factsList += movieFactGenerator.getFacts(random.randint(0, 2))
    factsList += representativeFactGenerator.getFacts(random.randint(0, 2))
    factsList += charmFactGenerator.getFacts(random.randint(0, 2))
    factsList += simpleFactGenerator.getFacts(simpleFactsChance)
    factsList += habitFactGenerator.getFacts(random.randint(0, 1))
    factsList += roleModelFactGenerator.getFacts(random.randint(0, 1))
    factsList += englishNameFactGenerator.getFacts(random.randint(0, 1), gender)
    factsList += roommateFactGenerator.getFacts(random.randint(0, 1))
    factsList += fearFactGenerator.getFacts(random.randint(0, 1))
    factsList += traineeFactGenerator.getFacts(random.randint(0, 1))
    factsList += languageFactGenerator.getFacts(random.randint(0, 1))
    factsList += familyFactGenerator.getFacts(random.randint(0, 1))

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
    profile.facts = makeFactsList(profile.gender)
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
