import csv
import random
import re
#import csvPaths
from . import csvPaths

words = {"food": [],
         "noExpressionFood": [],
        "eatsVerb": ["likes(( to eat))", "dislikes", "loves(( to eat))", "hates(( to eat))", "eats", "wants to eat", "will eat", "supports", "cannot handle", "can't eat", "cannot eat", "does not eat", "doesn't eat", "has problems eating", "dislikes", "does not like(( to eat))", "doesn't like(( to eat))"],
        "flavoredFood": ["oreos", "ice cream", "chips", "yogurt", "cup ramen"],
        "foodFlavor": ["sweet", "sour", "salty", "spicy", "smoky"],
        "everyAllFood": ["every food", "all foods", "everything", "anything"],
        "foodDish": ["food", "dish"],
        "cookedByPerson": ["!HER! mom", "!HER! dad", "!MEMBERNAME!", "!HER! sister", "!HER! brother", "!HER! grandmother", "!HER! grandpa", "!HER! manager"],
        "condiment": ["salt", "sugar", "cheese", "ketchup", "parmesan", "mustard", "hot sauce", "kimchi", "rice", "noodles"],
        "meal": ["breakfast", "brunch", "lunch", "tea", "supper", "dinner", "midnight snack", "late night snack"],
        "wasWere": ["was", "were"],
        "situation": ["!SHE! is alone", "!SHE! is with others", "!SHE! is at home", "the night comes"],
        "timePeriod": ["a month", "two months", "three months", "a week", "two weeks", "half a year", "a year", "the rest of !HER! life"],
        "shortTimePeriod": ["five seconds", "a minute", "three minutes", "the blink of an eye", "ten minutes", "twenty seconds"],
        "prefixCombiner": [" and ", ", ", ": "],
        "exceptBut": ["except", "but"],
        }

foodExpressions = ["anything [foodFlavor]",
                "[everyAllFood] [exceptBut] [food]",
                "[foodFlavor] food",
                "[food] that !SHE! cooked",
                "[food] that [cookedByPerson] cooked",
                "[food](( that has been)) cooked by !HER!",
                "[food](( that has been)) cooked by [cookedByPerson]",
                "[food] that has been reheated the next day",
                "[cookedByPerson]'s [food]",
                "[food] that [cookedByPerson] makes",
                "[food] with [condiment]"
                ]
badFoodExpressions = ["[food] flavored [flavoredFood]",
                "[food] fried rice",
                "[food] noodles",
                "[food] sushi"]

prefixExpressions = ["!SHE! eats a lot[prefixCombiner]",
        "!SHE! eats the most in the group[prefixCombiner]",
        "!SHE! is a picky eater[prefixCombiner]",
        "!SHE! is a big food lover[prefixCombiner]",
        "When it comes to food ", ]

foodFacts = ["!SHE! ((also ))[eatsVerb] [food]",
"!SHE! ((also ))[eatsVerb] [food] when [situation]",
"!HER! ((second ))favorite ((type of ))[foodDish] ((to cook ))is [food]",
"[food] is !HER! ((second ))favorite food",
"[food] is one of !HER! favorite foods",
"A food !SHE! ((really ))[eatsVerb] is [food]",
"!SHE! prefers [food] to [food]",
"!SHE! gets an allergic reaction to [food]",
"!SHE! is allergic to [food]",
"!SHE! hiccups when !SHE! eats [food] ((-Update: It seems !SHE! has fixed this problem))",
"!SHE! doesn't usually eat [food], but sometimes wants to eat it",
"!SHE! will eat [food] only when [situation]",
"!SHE! only eats [food]",
"If !SHE! [wasWere] a food !SHE! would be [food]",
"Once !SHE! only ate [food] for [timePeriod]",
"A food that !SHE! will eat without doubt is [food]",
"If !SHE! had to eat one food for [timePeriod] !SHE! would eat [food]",
"!SHE! can finish [food] in [shortTimePeriod]",
"A food !SHE! wants to eat even after !SHE! just ate it is [food]",
"!HER! nickname is [noExpressionFood]nator"
]

# foodlist generator
def getFoods():
    foodPath = csvPaths.foodPath
    foodfile = open(foodPath, 'r', encoding="utf8")
    foods = []

    with foodfile:
        foodReader = csv.reader(foodfile)
        for line in foodReader:
            foods.append(line[0])
    return foods


def processFactTemplate(txt):
    # Use a foodExpression
    matchFood = re.compile(r'\[food\]')
    if random.random() > 0.8:
        if random.random() > 0.8:
            txt = matchFood.sub(lambda match: random.choice(foodExpressions), txt)
        else:
            txt = matchFood.sub(lambda match: random.choice(badFoodExpressions), txt)

    # Use a prefix
    if random.random() > 0.92:
        txt = txt[0].lower() + txt[1:]
        txt = random.choice(prefixExpressions) + txt

    # Substitute all [] words
    matchKeys = re.compile(r'\[({})\]'.format('|'.join(words)))
    txt = matchKeys.sub(lambda match: random.choice(words[match.group(1)]), txt)

    # Flip the coin on all optional words
    matchParen = re.compile(r"\(\(([^)]*)\)\)")
    txt = matchParen.sub(lambda match: random.choice([match.group(1), ""]), txt)
    return txt


words["food"] = getFoods()
words["noExpressionFood"] = words["food"]


def debug():
    for i in range(10):
        txt = random.choice(foodFacts)
        txt = processFactTemplate(txt)
        print(txt)


def getFoodFact():
    txt = random.choice(foodFacts)
    txt = processFactTemplate(txt)
    return txt
