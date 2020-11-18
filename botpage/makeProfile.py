import csv
import random

def makeProfile(userIdolName, userGroupName):
    bioPath = '/home/kpopprofilebot/botsite/botpage/idolbio.csv'
    groupsPath = '/home/kpopprofilebot/botsite/botpage/idolgroups.csv'
    factsPath = '/home/kpopprofilebot/botsite/botpage/idolfacts.csv'

    biofile = open(bioPath, 'r', encoding="utf8")
    groupsfile = open(groupsPath, 'r', encoding="utf8")
    factsfile = open(factsPath, 'r', encoding="utf8")

    profile = {}
    idolNamesAll = {}
    groupNamesAll = []

    idolPositionsAll = ["Main Vocal", "Lead Vocal", "Sub-Vocal", "Main Dancer", "Lead Dancer", "Maknae", "Leader", "Visual", "MILF", "Catboy", "Hag", "The one who wears the cowboy hat", "Mullet", "manbun"]
    bloodTypesAll = ["A", "B", "AB", "O", "Unknown", "!!"]
    MBTIsAll = [
    "ISTJ",
    "ISTP",
    "ISFJ",
    "ISFP",
    "INFJ",
    "INFP",
    "INTJ",
    "INTP",
    "ESTP",
    "ESTJ",
    "ESFP",
    "ESFJ",
    "ENFP",
    "ENFJ",
    "ENTP",
    "ENTJ",
    "????",
    "8Hx4",
    "Don't know"
    ]
    astrologyAll = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    companyAll = ["SM", "YG", "JYP", "BigHit", "Toast Ent", "Socks Ent"]
    survivalShowAll = ["IDOL HELL", "Idol Broiler 92", "The Monastery"]

    with biofile:
        bioReader = csv.reader(biofile)
        for line in bioReader:
            if len(line) > 0 and line[0].isalpha and len(line[0]) > 2:
                idolNamesAll[line[0]] = line[4]

    with groupsfile:
        groupsReader = csv.reader(groupsfile)
        for line in groupsReader:
            if len(line) > 0 and len(line[0]) > 0:
                groupNamesAll.append(line[0])

    with factsfile:
        idolNameCount = 0
        idolNames = random.sample(list(idolNamesAll.keys()), 16)
        groupNames = random.sample(groupNamesAll, 10)
        gender = True if idolNamesAll[idolNames[0]] == "M" else False
        numFacts = 5

        myIdolName = userIdolName if userIdolName else idolNames[0]
        myGroupName = userGroupName if userGroupName else groupNames[0]
        profile["name"] = myIdolName
        profile["group"] = myGroupName
        profile["position"] = random.choice(idolPositionsAll)
        profile["sign"] = random.choice(astrologyAll)
        profile["bloodType"] = random.choice(bloodTypesAll)
        profile["MBTI"] = random.choice(MBTIsAll)
        profile["facts"] = []

        factsReader = csv.reader(factsfile)
        chances = numFacts / 1000
        for line in factsReader:
            if random.random() < chances:
                unprocessedFact = line[0]

                unprocessedFact = unprocessedFact.replace("!SHE!", "he" if gender else "she")
                unprocessedFact = unprocessedFact.replace("!HER!", "his" if gender else "her")
                unprocessedFact = unprocessedFact.replace("!HERSELF!", "himself" if gender else "herself")

                unprocessedFact = unprocessedFact.replace("!IDOLNAME!", idolNames[1 + idolNameCount], 1)
                unprocessedFact = unprocessedFact.replace("!IDOLNAME!", idolNames[2 + idolNameCount], 1)
                unprocessedFact = unprocessedFact.replace("!IDOLNAME!", idolNames[3 + idolNameCount])

                unprocessedFact = unprocessedFact.replace("!GROUPNAME!", myGroupName, 1)
                unprocessedFact = unprocessedFact.replace("!GROUPNAME!", groupNames[1 + idolNameCount], 1)
                unprocessedFact = unprocessedFact.replace("!GROUPNAME!", groupNames[2 + idolNameCount], 1)
                unprocessedFact = unprocessedFact.replace("!GROUPNAME!", groupNames[3 + idolNameCount])
                idolNameCount = idolNameCount + 1
                unprocessedFact = unprocessedFact.replace("!COMPANYNAME!", random.choice(companyAll))
                unprocessedFact = unprocessedFact.replace("!SURVIVALSHOWNAME!", random.choice(survivalShowAll))
                unprocessedFact = unprocessedFact.replace("\n", "")

                #capitalize fact
                if (random.random() < 0.8):
                    unprocessedFact = unprocessedFact[:1].upper() + unprocessedFact[1:]
                if (random.random() < 0.9):
                    unprocessedFact = "- " + unprocessedFact
                elif (random.random() < 0.5):
                    unprocessedFact = "-" + unprocessedFact
                else:
                    unprocessedFact = "-  " + unprocessedFact
                profile["facts"].append(unprocessedFact)

                if len(profile["facts"]) == numFacts:
                    break
        return profile