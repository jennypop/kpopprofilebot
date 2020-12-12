import csv
import random
import inflect
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta
from botpage import idolData, csvPaths

dictSingle = {}
dictRandom = {
    "closePerson": ["!HER! mom", "!HER! dad", "!MEMBERNAME!", "!HER! sister", "!HER! brother", "!HER! grandmother", "!HER! grandpa", "!HER! manager"],
    "wasWere": ["was", "were"],
    "whenSituation": ["when !SHE! is alone", "when !SHE! is with others", "when !SHE! is at home", "when the night comes", "when !SHE! can't sleep", "before going to bed", "from her bed", "at the cinema", "when !SHE! feels good", "when !SHE! feels down", "on the first day of each month", "when watching a movie", ],
    "timeBasic": ["day", "week", "month"],
    "timePeriod": ["a [timeBasic]", "two [timeBasic]s", "three [timeBasics]", "half a year", "a year", "the rest of !HER! life"],
    "oftenTimePeriod": ["{once/twice/a few times/multiple times} a {[timeBasic]/year}", "once every few [timeBasic]s", "every {[timeBasic]/year}"],
    "shortTimePeriod": ["five seconds", "twenty seconds", "thirty seconds", "{one/a} minute", "!SMALLINTW! minutes", "the blink of an eye"],
    "positiveAdjective": ["relaxing", "comfortable", "refreshing"],
    "prefixCombiner": [" and ", ", ", ": "],
    "exceptBut": ["except", "but"],
    "youngerTime": ["at the age of !TRAINEEAGE!", "in {middle school/high school/!SCHOOLGRADE!}", "when !SHE! was in {middle school/high school/!SCHOOLGRADE!}", "when !SHE! was younger", ],
}


class Idol:
    def __init__(self):
        self.name = ""
        self.group = ""
        self.gender = True  # Male
        self.homeCountry = ""
        self.birthDate = None
        self.traineeDate = None
        self.debutDate = None
        self.birthDateString = ""
        self.debutDateString = ""
        self.positions = []
        self.sign = ""
        self.bloodType = ""
        self.MBTI = ""
        self.facts = []


myIdolData = Idol()

idolNamesAll = {}
groupNamesAll = []


def getIdolNames():
    biofile = open(csvPaths.bioPath, 'r', encoding="utf8")

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


def getRandomDate(yearY):
    return datetime(year=yearY, month=1, day=1) + relativedelta(days=random.randint(0, 364))


def makeDatesForIdol():
    idolAge = random.randint(18, 25)
    if random.random() < 0.2:
        idolAge += random.randint(0, 9)
    currentYear = datetime.now().year
    birthDate = getRandomDate(currentYear-idolAge)
    myIdolData.birthDate = min(birthDate, datetime.now() + relativedelta(years=-18, months=-6))  # For ease of everything they must be at least 18.5
    myIdolData.birthDateString = formatDate(myIdolData.birthDate, "")
    myIdolData.ageString = str(getAge())

    debutAge = random.randint(17, min(idolAge-1, 22))
    myIdolData.debutDate = birthDate + relativedelta(years=+debutAge, days=random.randint(0, 364))
    myIdolData.debutDateString = formatDate(myIdolData.debutDate, "")

    # Default trainee period 2-4 years
    traineePeriod = relativedelta(years=+2, days=+random.randint(0, 730))
    if random.random() < 0.1:
        traineePeriod += relativedelta(days=-random.randint(0, 600))
    elif random.random() < 0.1:
        traineePeriod += relativedelta(years=+random.randint(0, debutAge-16))
    myIdolData.traineeDate = myIdolData.debutDate - traineePeriod


def getAge():
    return relativedelta(datetime.today(), myIdolData.birthDate).years


def getTraineeAge():
    return relativedelta(myIdolData.traineeDate, myIdolData.birthDate).years


def getDebutAge():
    return relativedelta(myIdolData.debutDate, myIdolData.birthDate).years


def getPreTraineeDate(formatType):
    idolIsSixDate = myIdolData.birthDate + relativedelta(years=+6)
    return formatDate(getRandomDateBetween(idolIsSixDate, myIdolData.traineeDate), formatType)


def getPreDebutDate(formatType):
    return formatDate(getRandomDateBetween(myIdolData.traineeDate, myIdolData.debutDate), formatType)


def getActiveDate(formatType):
    return formatDate(getRandomDateBetween(myIdolData.debutDate, datetime.now() + relativedelta(months=-1)), formatType)


def getRandomRank(start, fin):
    p = inflect.engine()
    return p.ordinal(random.randint(start, fin))


def getRandomSchoolGrade():
    if random.random() < 0.25:
        return str(getRandomRank(1, 6)) + " grade of elementary school"
    elif random.random() < 0.5:
        return str(getRandomRank(1, 3)) + " grade of middle school"
    else:
        return str(getRandomRank(1, 3)) + " grade of high school"


def formatDate(dateArg, formatType):
    assert formatType == "YM" or formatType == "Y" or formatType == ""
    if formatType == "Y":
        return dateArg.strftime("%Y")
    elif formatType == "YM":
        return dateArg.strftime("%B ((of ))%Y")
    else:
        return dateArg.strftime("%B %#d, %Y")


def getRandomDateBetween(date1, date2):
    timeBetweenDates = (date2 - date1).days
    assert timeBetweenDates > 0
    return date1 + relativedelta(days=+random.randrange(timeBetweenDates))


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


def initialize():
    idolNamesAll = getIdolNames()
    global groupNamesAll
    groupNamesAll = getGroupNames()

    makeDatesForIdol()

    myIdolData.name = random.choice(list(idolNamesAll.keys()))
    myIdolData.group = random.choice(groupNamesAll)
    myIdolData.gender = True if idolNamesAll[myIdolData.name] == "M" else False
    myIdolData.positions = makePositionsList()
    myIdolData.sign = random.choice(idolData.astrologyAll)
    myIdolData.bloodType = random.choice(idolData.bloodTypesAll if random.random() < 0.9 else idolData.bloodTypesFun)
    myIdolData.MBTI = random.choice(idolData.MBTIsAll if random.random() < 0.9 else idolData.MBTIsFun)

    initializeDicts()
    return myIdolData


def initializeDicts():
    p = inflect.engine()
    # Replace gendered pronouns
    gender = myIdolData.gender
    dictSingle["!SHE!"] = "he" if gender else "she"
    dictSingle["!HER!"] = "his" if gender else "her"
    dictSingle["!HERHIM!"] = "him" if gender else "her"
    dictSingle["!HERSELF!"] = "himself" if gender else "herself"

    dictRandom["!COMPANYNAME!"] = idolData.companyAll
    dictRandom["!OTHERCOMPANYNAME!"] = idolData.companyAll
    dictRandom["!SURVIVALSHOWNAME!"] = idolData.survivalShowAll
    dictRandom["!TVSHOWNAME!"] = idolData.tvShowAll
    dictRandom["!FESTIVALNAME!"] = idolData.festivalAll
    dictRandom["!IDOLNAME!"] = list(idolNamesAll.keys())
    dictRandom["!GROUPNAME!"] = groupNamesAll
    dictRandom["!SUBUNITNAME!"] = groupNamesAll

    dictSingle["!MYGROUPNAME!"] = myIdolData.group
    dictSingle["!HOMECOUNTRY!"] = "South Korea"  # TODO

    # Key dates
    dates = {"BIRTHDATE": myIdolData.birthDate,
    "TRAINEEDATE": myIdolData.traineeDate,
    "DEBUTDATE": myIdolData.debutDate}

    for key, value in dates.items():
        dictSingle["!" + key + "!"] = formatDate(value, "")
        dictSingle["!" + key + "Y!"] = formatDate(value, "Y")
        dictSingle["!" + key + "YM!"] = formatDate(value, "YM")

    traineePeriodLength = relativedelta(myIdolData.debutDate, myIdolData.traineeDate)
    if traineePeriodLength.years > 0:
        dictSingle["!TRAINEEPERIODY!"] = p.number_to_words(traineePeriodLength.years) + " years"
        dictSingle["!TRAINEEPERIOD!"] = dictSingle["!TRAINEEPERIODY!"] + " and " + p.number_to_words(traineePeriodLength.months) + " months"
    else:
        dictSingle["!TRAINEEPERIODY!"] = p.number_to_words(traineePeriodLength.months) + " months"
        dictSingle["!TRAINEEPERIOD!"] = dictSingle["!TRAINEEPERIODY!"]

    dictSingle["!TRAINEEAGE!"] = str(getTraineeAge())
    dictSingle["!DEBUTAGE!"] = str(getDebutAge())