from botpage import csvPaths
from factGenerators import basicUtils

words = {}
suffixes = ["because of a nightmare !SHE! had [youngerTime]",
"because of an incident that happened [youngerTime]"]

factTemplates = [
"!SHE! has a fear of [fear]",
"!SHE! is afraid of [fear]",
"!SHE! is scared of [fear]",
"!HER! biggest fear is [fear]",
"!SHE! used to have a fear of [fear]",
"!SHE! has a phobia of [fear]",
"!SHE! isn't afraid of anything except [fear]",
"!SHE! fears [fear] more than [fear]",
"!SHE! has {trypophobia/acrophobia/aquaphobia/mysophobia}",
"!SHE! is not afraid of anything"
]


words["fear"] = basicUtils.getFromCSV(csvPaths.fearsPath)


def processFactTemplate(txt):
    txt = basicUtils.addSuffix(txt, 0.2, suffixes, " ")
    txt = basicUtils.processFactTemplateBasic(txt, words)

    return txt


def getFacts(n):
    return basicUtils.getFacts(n, factTemplates, processFactTemplate)
