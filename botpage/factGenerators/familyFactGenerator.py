import inflect
import random
import math
from factGenerators import basicUtils

siblingTypes = ["{younger/little} sister", "{older/big} sister", "{younger/little} brother", "{older/big} brother", "twin {brother/sister}"]

factTemplates = [
"{!HER! family consists of/Family:} [parentString], [siblingString]",
"!SHE! has [n] siblings, [siblingString]",
"!SHE! has [siblingString]",
]


def getSiblings():
    n = random.randint(0, 1) + random.randint(0, 1)
    if (random.random() < 0.5):
        n += random.randint(0, 2)
    listSiblings = [0, 0, 0, 0, 0]
    for i in range(n):
        listSiblings[math.floor(random.random() * 4.1)] += 1
    return listSiblings


def getSiblingString():
    p = inflect.engine()
    txtList = []
    listSiblings = getSiblings()
    for i in range(len(listSiblings)):
        if listSiblings[i] == 1:
            txtList.append("a " + siblingTypes[i])
        elif listSiblings[i] > 1:
            txtList.append(p.number_to_words(listSiblings[i]) + " " + siblingTypes[i] + "s")
    txt = " and ".join(txtList)
    n = sum(listSiblings)
    if n == 0:
        txt = "!SHE! {is an only child/doesn't have any siblings}"
    elif listSiblings[0] + listSiblings[2] + listSiblings[4] == 0:
        txt += ". !SHE! is the youngest {of/in} !HER! family"
    elif listSiblings[1] + listSiblings[3] + listSiblings[4] == 0:
        txt += ". !SHE! is the oldest {of/in} !HER! family"
    return txt, n


def getParentsString():
    if random.random() < 0.05:
        return "!HER! mother" if random.random() < 0.5 else "!HER! father"
    else:
        return random.choice(["!HER! parents", "!HER! mother and ((!HER! ))father", "!HER! father and ((!HER! ))mother"])


def processFactTemplate(txt):
    p = inflect.engine()
    siblingString, n = getSiblingString()
    if n == 0:
        return siblingString
    txt = txt.replace("[parentString]", getParentsString())
    txt = txt.replace("[siblingString]", siblingString)
    txt = txt.replace("[n]", p.number_to_words(n))
    return txt


def getFacts(n):
    return basicUtils.getFacts(n, factTemplates, processFactTemplate)
