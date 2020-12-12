import random
import re
from botpage import factProcessor

words = {"religiousPerson": ["Buddhist", "Christian", "Protestant", "Catholic"],
"religion": ["Buddhism", "Christianity", "Protestantism", "Catholicism"],
"instrument": ["piano", "guitar", "bass", "drums", "janggu", "kwaenggwari", "daegeum", "jing", "guzheng", "ehru", "pipa", "harmonica", "ukelele", "violin"],
"danceStyle": ["ballet", "jazz", "hip hop", "popping and locking", "house", "waacking", "street dance", "Chinese classical dance", "Korean classical dance", "martial arts", "freestyle dance", "contemporary dance", "girl group dance", "tango", "modern dance", "tumbling", "b-boying", "traditional dance", ],
"superpower": ["happy virus", "power booster", "shield", "magnifying", "healing", "rocket punch", "X-ray vision", "teleportation", "time control", "light", "earth", "water", "invisibility", "stopping time", "creating anything", "telekinesis", "not needing sleep", "controlling metal (((like Magneto)))", "mind control", ],
"rankSuffix": ["and got to debut in the group !GROUPNAME!", "and was eliminated", "and was unfortunately eliminated", "and became a fan favorite", "but had to leave due to conflicting schedules"],
"switchBodiesReason": [
"they have a really healthy body", "they have good body proportions", "they are charming", "!SHE! wants to see things from a higher view", "!SHE! would want to cook well", "they have strong legs", "they have chocolate abs", "of their fortune", "they're a good dancer", "!SHE! could do things without feeling as much embarrassment", "!SHE! wants to breathe the air from up there", "!SHE! would not have problems trying on clothes", "of their height", "they are young", "of their face", "they never sleep", "!SHE! just wants to(( try it))", "they have a nice ass", "!SHE! wants to be tall", "they have great muscles", "!SHE! wants to know !HER! enemy", "they can do anything", "they want to know what it's like to be a great singer", "they are cute", ],
"instrumentDanceSuffix": [
", !SHE! {practiced/learned} it for !SMALLINT! years [youngerTime]",
", !SHE! began learning [youngerTime]"
],
}

religiousFactTemplates = [
"!SHE! is ((a ))((devout ))[religiousPerson]",
"Religion: [religion]",
"!SHE! practices [religion]",
"!HER! religion is [religion]",
"!SHE! doesn't have a religion that !SHE! follows",
"!SHE! doesn't practice any religion",
]
instrumentFactTemplates = [
"!SHE! {can/knows how to} play several instruments including the [instrument](( and the [instrument]))(([instrumentDanceSuffix]))",
"!SHE! {can/knows how to} play the [instrument](([instrumentDanceSuffix]))",
"!SHE! won {a special prize/!VERYHIGHRANK! place} at a [instrument] {competition/festival}"
]
danceFactTemplates = [
"!HER! {dance specialty/main dance style/primary dance style} is [danceStyle](([instrumentDanceSuffix]))",
"!SHE! {specializes in/is especially good at} [danceStyle](([instrumentDanceSuffix]))",
]
superpowerFactTemplates = [
"!HER! concept specialty is [superpower]",
"If !SHE! could have a superpower it would be [superpower]",
]
rankFactTemplates = [
"!SHE! ((is ))ranked !RANK100! on TC Candler \"The 100 Most {Beautiful/Handsome/!IDOLNAME!dsome} Faces of !ACTIVEDATEY!\"",
"!SHE! ((was ))ranked !RANK! on !SURVIVALSHOWNAME!{ ep !SMALLINT! / receiving !HUGENUMBER! votes / with !HUGENUMBER! votes}(( [rankSuffix]))",
"!SHE! {appeared on/participated in} !SURVIVALSHOWNAME! and ranked !RANK!(( {receiving/with} !HUGENUMBER! votes))(( [rankSuffix]))",
]
switchBodiesFactTemplates = [
"If !SHE! could {switch/exchange} bodies with any member it would be !MEMBERNAME! {because/since} [switchBodiesReason]",
"!SHE! picked !MEMBERNAME! as the one who !SHE! would want to {switch/exchange} bodies with {because/since} [switchBodiesReason]",
"!SHE! would want to {switch/exchange} bodies with !MEMBERNAME! {because/since} [switchBodiesReason]",
"!SHE! doesn't want to {switch/exchange} bodies with anyone ((, !SHE! likes !HER! body the best))",
]

factTemplatesList = [religiousFactTemplates, instrumentFactTemplates, danceFactTemplates, superpowerFactTemplates, rankFactTemplates, switchBodiesFactTemplates]


def processFactTemplate(txt):
    txt = factProcessor.processFactEarly(txt)
    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)
    return txt


def getFacts(chanceOfSelection):
    factList = []
    for factTemplateList in factTemplatesList:
        if random.random() < chanceOfSelection:
            fact = processFactTemplate(random.choice(factTemplateList))
            factList.append(fact)
    return factList


def debug():
    for i in range(10):
        facts = getFacts(1.0)
        for fact in facts:
            print(fact)

