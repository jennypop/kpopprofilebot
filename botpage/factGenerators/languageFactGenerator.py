import random
import re
from factGenerators import basicUtils

words = {
"languageA": ["English", "Japanese", "Mandarin", "Thai", "Korean", "Taiwanese", "in satoori", "Cantonese", ],
"languageRare": ["!IDOLNAME!ese", "German", "Portuguese", "Tagalog", "sign language", "French", "Spanish", ],
"languagePre": ["basic", "a bit of", "a little", "fluent", "intermediate"],
"languagePost": ["fluently", "very well"],
"languageSuffix": ["!IDOLNAME! said !SHE!'s not very good tho((ugh))", "!SHE! learned it from TV programs", "!SHE! learned it while studying abroad", "because !SHE! lived there"],
}
languageFactTemplates = [
"!SHE! can speak [language]",
"!SHE! is the best at speaking [language] in !GROUPNAME!",
"!SHE! can speak both [language] and [language]",
"!SHE! is multi-lingual and can speak ([language])*2(, ) and [language]",
"!SHE! {is studying/studied} [language]",
"Languages: ([language])*4(, )",
"When !IDOLNAME! {gets/is} drunk !SHE! speaks fluent [language].",
]


def getLanguageString():
    txt = random.choice(words["languageA"] if random.random() < 0.8 else words["languageRare"])
    if random.random() < 0.6:
        txt = random.choice(words["languagePre"]) + " " + txt
    elif random.random() < 0.3:
        txt = txt + " " + random.choice(words["languagePost"])
    return txt


def processFactTemplate(txt):
    txt = basicUtils.addSuffix(txt, 0.3, words["languageSuffix"], ", ")
    txt = basicUtils.processFactTemplateBasic(txt, words)
    while "[language]" in txt:
        txt = txt.replace("[language]", getLanguageString(), 1)
    return txt


def getFacts(n):
    return basicUtils.getFacts(n, languageFactTemplates, processFactTemplate)

