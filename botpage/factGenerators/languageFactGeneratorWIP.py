import csv
import random
import re
from botpage import csvPaths, factProcessor

words = {
"language": ["English", "Japanese", "Mandarin", "Thai", "Korean", "Taiwanese", "in satoori", "Cantonese", ],
"languageRare": ["!IDOLNAME!ese", "German", "Portuguese", "Tagalog", "sign language", "French", "Spanish", ],
"languagePre": ["basic", "a bit of", "a little", "fluent", "intermediate"],
"languagePost": ["fluently", "very well"],
"languageSuffix": ["!IDOLNAME! said !SHE!'s not very good tho((ugh))", "!SHE! learned it from TV programs", "!SHE! learned it while studying abroad", "because !SHE! lived there"],
}
languageFactTemplates = [
"!SHE! can speak [language](( [languageSuffix]))",
"!SHE! is the best at speaking [language] in !GROUPNAME!(( [languageSuffix]))",
"!SHE! can speak both [language] and [language]",
"!SHE! is multi-lingual and can speak [language](*3)(, )",
"!SHE! {is studying/studied} [language]",
"Languages: [language](*4)(, )",
"When !IDOLNAME! {gets/is} drunk !SHE! speaks fluent [language].",
]

def getLanguageString():
    txt = random.choice(words["language"] if random.random() < 0.8 else words["languageRare"])
    if random.random() < 0.6:
        txt = random.choice(words["languagePre"] + " " + txt)
    elif random.random() < 0.3:
        txt = txt + " " + random.choice(words["languagePost"])
    return txt


def processFactTemplate(txt):
    txt = factProcessor.processABCChoice(txt)
    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)
    txt = txt + '"' + random.choice(mottos) + '"'
    return txt


def debug():
    for i in range(10):
        txt = random.choice(factTemplates)
        txt = processFactTemplate(txt)
        print(txt)


def getFacts(n):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList