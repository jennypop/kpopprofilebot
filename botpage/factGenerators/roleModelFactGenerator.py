import random
from botpage import csvPaths, factProcessor
from factGenerators import basicUtils

words = {"fan": ["big fan", "huge fan", "fan", "long-time fan", "really big fan"],
"roleModel": ["role model", "favorite artist", "idol", "((biggest ))inspiration"],
"otherIdol": ["!GROUPNAME!",
"!GROUPNAME!'s !IDOLNAME!",
"!IDOLNAME! OF !GROUPNAME!",
"!IDOLNAME!", ]}

factTemplates = [
"!SHE! is a [fan] of [idol]",
"!HER! [roleModel]s are ([idol])*2(, ) and [idol]",
"!HER! [roleModel] is [idol]",
"!SHE! admires [idol]",
"!SHE! looks up to [idol]",
"The artist who made !HER! want to become {a singer/an idol} is [idol]"
]
words["suffix"] = [" ever since [youngerTime]",
" and !SHE! wants to buy their merch",
" ever since !SHE! went to their concert",
" and !SHE! once gave them a fan letter",
" and !SHE! learned to {sing / dance / play the guitar }because of them",
", !SHE! cried when !SHE! met them",
" and !SHE! knows most of the choreographies to their songs",
" and !SHE! joined their fanclub in !YEAR!",
" and !SHE! impersonated them on !TVSHOWNAME!",
" and !SHE! has a lot of their merch",
", !SHE! has a poster of them in her room",
" !SHE! wants to take a picture with them",
" and !SHE! took a picture with them",
", !SHE!'d like to collaborate with them",
", they're the reason why !SHE! became an idol",
", because they are ((really ))cool on the stage",
", !SHE! has their picture set as !HER! phone wallpaper"]

words["idol"] = basicUtils.getFromCSV(csvPaths.roleModelPath)


def processFactTemplate(txt):
    txt = factProcessor.processFactEarly(txt)

    if random.random() < 0.4:
        txt = txt.replace("[idol]", random.choice(words["otherIdol"]))
    if random.random() < 0.7:
        txt += random.choice(words["suffix"])

    txt = basicUtils.processFactTemplateBasic(txt, words)
    return txt


def getFacts(n):
    factList = random.sample(factTemplates, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
