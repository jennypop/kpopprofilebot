import csv
import random
import re
import csvPaths, factProcessor
from factGenerators import basicUtils

words = {
"suffix": ["they sleep in the big room",
"they are best friends",
"they lived next to a shopping mall",
"their room is the cleanest",
"they share the smallest room",
"!SHE! is the only clean member",
"they are the closest in the group",
"!SHE! is responsible for {cooking/cleaning/waking up early/doing the laundry/cleaning the dishes}",
"!SHE! has the top bunk",
"!SHE! has the bottom bunk",
"!SHE! is a noisy roommate",
"!SHE! stays up late",
"they fight a lot", ],
"updates": ["Update: !GROUPNAME! members ((moved out of the dorm and ))live separately now",
"Update: !SHE! is living alone now.",
"Update: In the new dorm, {!SHE! shares a room with/!HER! roommate is} !IDOLNAME!",
"Update: In the new dorm, {all the members have their/each member has their/!SHE! has !HER!} own room", ]
}


factTemplates = [
"!HER! roommate in the dorms is !MEMBERNAME!((, [suffix]))",
"!HER! roommates are !MEMBERNAME! and !MEMBERNAME!",
"!SHE! and !MEMBERNAME! are roommates((, [suffix]))",
"!SHE! shares a room with (!MEMBERNAME!)*2( and )((, [suffix]))",
"!SHE! wants to be roommates with !MEMBERNAME!(({ because they are [personalityTrait]/ because they are !HER! best friend}))",
"!SHE! and !MEMBERNAME! {are no longer/were/used to be} roommates(({, !SHE! was kicked out/, !SHE! kicked them out/, !SHE! was too messy/, they fought too much}))",
]


def processFactTemplate(txt):
    txt = basicUtils.addSuffix(txt, 0.3, words["updates"], ". ")
    txt = basicUtils.processFactTemplateBasic(txt, words)
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
