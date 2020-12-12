import random
import re
from botpage import factProcessor

words = {
"trainee": ["((!MYCOMPANYNAME! ))trainee"/"trainee {at/under }!MYCOMPANYNAME!"],
"otherCompanyTrainee": ["{a /a former /an ex-}trainee {of/under/at} !OTHERCOMPANYNAME!", "a ((former ))!OTHERCOMPANYNAME! trainee"],
"onTraineeDate": ["in !TRAINEEDATEY!", "in !TRAINEEDATEYM!", "on !TRAINEEDATEYMD!"],
"traineePeriod": ["!TRAINEEPERIODYM!", "!TRAINEEPERIODY!", "around !TRAINEEPERIODY!"],
"traineeGroupNameDescription": ["trained the longest", "were part of !SURVIVALSHOWNAME!", "were introduced in !TRAINEEDATEY!", "were part of the trainee foreign line", "were part of the dance team", ]
}


factTemplates = [
#  Time spent training / startdate
"((In total, ))!HER! training period was [traineePeriod]",
"!SHE! {trained at !MYCOMPANYNAME!/was a [trainee]} for [traineePeriod]",
"{Trainee/Training} period: [traineePeriod]",
"!SHE! debuted after [traineePeriod] of training",
"!SHE! {became a [trainee]/started training} ((after {being recruited/being scouted/passing an audition} )){[youngerTime]/[onTraineeDate]/around the same time as !MEMBERNAME!}",
"!SHE! ha{d/s} been a trainee since {!SCHOOLGRADE!/middle school/high school}",
"!SHE! had the {longest/shortest} trainee period out of all the members.",
"!SHE! trained together with ({!MEMBERNAME!/!IDOLNAME!})*2( and ) at !MYCOMPANYNAME!",

# How she became a trainee
"SHE! auditioned in a !MYCOMPANYNAME! audition in !HOMECOUNTRY! and joined the trainee program in South Korea [onTraineeDate]",
"!SHE! passed the audition on !TRAINEEDATE! and officially became a [trainee]",
"!SHE! became a [trainee] after {!HER! appearance/appearing} in the show !SURVIVALSHOWNAME!",

# Introduction / trainee group
"!SHE! is the !VERYHIGHRANK! trainee that was {officially introduced/announced as a part of !GROUPNAME!}",
"{One of the members/A member} of !TRAINEEGROUPNAME!, the SMALLINT members of !GROUPNAME! who [traineeGroupNameDescription]",

# Ex trainee history
"!SHE! and fellow member !MEMBERNAME! were also !OTHERCOMPANYNAME! trainees",
"!SHE! {is/was/used to be} [otherCompanyTrainee]((, she {was friends with/trained alongside} {!GROUPNAME!/!IDOLNAME!}))",
"!SHE! used to train {at/under }!COMPANYNAME!",
"!SHE! passed a !OTHERCOMPANYNAME! audition but didn't {train with them/become a trainee}",
"!SHE! used to train {with/alongside} ((several members of ))!GROUPNAME!",
]

suffix = [
", !SHE! joined [onTraineeDate]",
"and !SHE! used to train with !GROUPNAME!",
"and was a part of !TRAINEEGROUPNAME!",
", !SHE! trained there for !SMALLINT! years",

"after winning !HIGHPLACE! place at a !COMPANYNAME! Open Audition (((joint with !MEMBERNAME!)))",
"and became a member of !TRAINEEGROUP! in TO(!TRAINEEDATE!, !DEBUTDATE!)",
"after !SHE! won the !HIGHPLACE! place in a contest on !SURVIVALSHOWNAME!",
"after auditioning in BEFORE(!TRAINEEDATE!)Y",
"after impressing judges with !HER! singing at the BEFORE(!TRAINEEDATE!) !FESTIVALNAME!",
"after winning an audition against !SMALLINT!*1000 other candidates",
"and has lived in Korea since",
"and the first person she met was !MEMBERNAME!",
"before {joining/going on} !SURVIVALSHOWNAME!",
"before debuting(( in !GROUPNAME!))",
"{and was selected/before being selected} for !GROUPNAME!",
"and was rumored to debut in !OTHERGROUPNAME!"
] # Can add ", "


def addSuffix(txt):
    if "favorite" not in txt and "loved" not in txt:
        txt += "((,)) but it is not !HER! favorite"


def processFactTemplate(txt):
    factProcessor.processFactEarly(txt)
    txt = txt.replace("!LUCKYNUMBER!", str(getRealisticLuckyNumber()))
    # Use a traineeExpression
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), str(txt))
    if random.random() < 0.1:
        addSuffix(txt)
    return txt


def getFacts(n):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
