import csv
import random
import re
from botpage import csvPaths, factProcessor

words = { "herCharm": [], "body": [], "noHerCharm": [], }
factTemplates = ["!HER! (({main/most notable} )){((most ))charm((ing))/attraction/unique} point is((:)) {[noHerCharm]/!HER! [herCharm]}",
"!HER! {((biggest ))strength/charm/most attractive quality} is((:)) {[noHerCharm]/!HER! [herCharm]}",
"!HER! {charming/charm/attraction/unique} points are((:)) ({[noHerCharm]/!HER! [herCharm]})*3( and )",
"!HER! {((biggest ))strengths/charms} are((:)) ({[noHerCharm]/!HER! [herCharm]})*3( and )",
"{Attractive point((s))/ Charm/ Charm((ing)) point((s))/ Strength((s))}: ({[noHerCharm]/!HER! [herCharm]})*4(, )",
"!HER! favorite body feature is !HER! [body]",
"!HER! [body] is the most attractive part of !HER! body",
"!SHE! has an attractive [body]",
"Body secret: [body]",
"!HER! personality {can be described as/is} ({very/quite/} [personalityTrait])*2( and )",
"!HER! most attractive personality trait is that !SHE! is (({very/quite} ))[personalityTrait]",
"!HER! strengths{ are/ include/:} being ([personalityTrait])*2( and )",
"!SHE!'s the group's [personalityTrait] member",
"!SHE! has a [personalityTrait] personality",
"!SHE! is actually [personalityTrait] but does not know how to show it",
"Personality: ([personalityTrait])*5(, )", ]
prefixes = ["!SHE! {believes/said/feels} that ", "According to [closePerson], ", "According to !HER!, ", "!SHE! {says/thinks} "]

def getWords():
    charmPath = csvPaths.charmPath
    charmfile = open(charmPath, 'r', encoding="utf8")

    with charmfile:
        charmReader = csv.reader(charmfile)
        next(charmReader)
        for line in charmReader:
            if (line[0]):
                words["herCharm"].append(str(line[0]))
            if (line[1]):
                words["body"].append(str(line[1]))
                words["herCharm"].append(str(line[1]))
            if (line[2]):
                words["noHerCharm"].append(str(line[2]))


getWords()


def addPrefix(txt):
    txt = random.choice(prefixes) + txt[:1].lower() + txt[1:]


def processFactTemplate(txt):
    txt = factProcessor.processFactEarly(txt)
    # Use a charmExpression
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), str(txt))
    if random.random() < 0.1:
        addPrefix(txt)
    return txt


def getFacts(n):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
