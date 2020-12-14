from factGenerators import basicUtils

words = {
"trainee": ["((!MYCOMPANYNAME! ))trainee", "trainee {at/under} !MYCOMPANYNAME!"],
"otherCompanyTrainee": ["{a /a former /an ex-}trainee {of/under/at} !OTHERCOMPANYNAME!", "a ((former ))!OTHERCOMPANYNAME! trainee"],
"onTraineeDate": ["in !TRAINEEDATEY!", "in !TRAINEEDATEYM!", "on !TRAINEEDATE!"],
"traineePeriod": ["!TRAINEEPERIODY!", "!TRAINEEPERIODY!", "around !TRAINEEPERIODY!"],
"traineeGroupNameDescription": ["trained the longest", "were part of !SURVIVALSHOWNAME!", "were introduced in !TRAINEEDATEY!", "were part of the trainee foreign line", "were part of the dance team", ]
}


factTemplates = [
#  Time spent training / startdate
"((In total, ))!HER! training period was [traineePeriod]",
"!SHE! {trained at !MYCOMPANYNAME!/was a [trainee]} for [traineePeriod](( [suffix]))",
"{Trainee/Training} period: [traineePeriod]",
"!SHE! debuted after [traineePeriod] of training(( [suffix]))",
"!SHE! {became a [trainee]/started training} ((after {being recruited/being scouted/passing an audition} )){[youngerTime]/[onTraineeDate]/around the same time as !MEMBERNAME!}(( [suffix]))",
"!SHE! ha{d/s} been a trainee since {!SCHOOLGRADE!/middle school/high school}(( [suffix]))",
"!SHE! had the {longest/shortest} trainee period out of all the members",
"!SHE! trained together with ({!MEMBERNAME!/!IDOLNAME!})*2( and ) at !MYCOMPANYNAME!(( [suffix]))",

# How she became a trainee
"!SHE! auditioned in a !MYCOMPANYNAME! audition in !HOMECOUNTRY! and joined the trainee program in South Korea [onTraineeDate]",
"!SHE! passed the audition on !TRAINEEDATE! and officially became a [trainee]",
"!SHE! became a [trainee] after {!HER! appearance/appearing} in the show !SURVIVALSHOWNAME!",

# Introduction / trainee group
"!SHE! is the !VERYHIGHRANK! trainee that was {officially introduced/announced as a part of !GROUPNAME!}",
"{One of the members/A member} of !TRAINEEGROUPNAME!, the !SMALLINT! members of !GROUPNAME! who [traineeGroupNameDescription]",

# Ex trainee history
"!SHE! and fellow member !MEMBERNAME! were also !OTHERCOMPANYNAME! trainees",
"!SHE! {is/was/used to be} [otherCompanyTrainee]((, !SHE! {was friends with/trained alongside} {!GROUPNAME!/!IDOLNAME!}))",
"!SHE! used to train {at/under} !COMPANYNAME!(( [suffix]))",
"!SHE! passed a !OTHERCOMPANYNAME! audition but didn't {train with them/become a trainee}",
"!SHE! used to train {with/alongside} ((several members of ))!GROUPNAME!",
]

words["suffix"] = [
", !SHE! joined [onTraineeDate]",
"and !SHE! used to train with !GROUPNAME!",
"and was a part of !TRAINEEGROUPNAME!",
", !SHE! trained there for !SMALLINT! years",
"{and was selected/before being selected} for !GROUPNAME!",
", and was rumored to debut in !OTHERGROUPNAME!",
"and has lived in Korea since",
"and the first person !SHE! met was !MEMBERNAME!",
"after winning !HIGHRANK! place at a !COMPANYNAME! Open Audition",
"after winning !HIGHRANK! place at a !COMPANYNAME! Open Audition (joint with !MEMBERNAME!)",
"and became a member of !TRAINEEGROUP! in !PREDEBUTDATEY!",
"after !SHE! won the !HIGHRANK! place in a contest on !SURVIVALSHOWNAME!",
"after auditioning in !PRETRAINEEDATEY!",
"after impressing judges with !HER! singing at the !PRETRAINEEDATEY! !FESTIVALNAME!",
"after winning an audition against !SMALLINTW! {thousand/hundred} other candidates",
"before {joining/going on} !SURVIVALSHOWNAME!",
"before debuting in !GROUPNAME!",
]


def processFactTemplate(txt):
    txt = basicUtils.processFactTemplateBasic(txt, words)
    return txt


def getFacts(n):
    return basicUtils.getFacts(n, factTemplates, processFactTemplate)
