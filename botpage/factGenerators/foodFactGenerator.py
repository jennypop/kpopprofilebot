import csv
import random
import re
from botpage import csvPaths, factProcessor

words = {"food": [],
         "noExpressionFood": [],
        "eatsVerb": ["{likes/dislikes/loves/hates}(( to eat))", "eats", "wants to eat", "will eat", "supports", "cannot handle", "{can't/cannot} eat", "{does/doesn't} eat", "has problems eating", "dislikes", "{does not/doesn't} like(( to eat))", ],
        "flavoredFood": ["oreos", "ice cream", "chips", "yogurt", "cup ramen"],
        "foodFlavor": ["sweet", "sour", "salty", "spicy", "smoky"],
        "everyAllFood": ["every food", "all foods", "everything", "anything"],
        "foodDish": ["food", "dish"],
        "condiment": ["salt", "sugar", "cheese", "ketchup", "parmesan", "mustard", "hot sauce", "kimchi", "rice", "noodles", "aioli", "barbecue sauce", "chili sauce", "chutney", "fish paste", "dip", "fruit preserves", "soy sauce", "horseradish", "guac", "mayonnaise", "pesto", "sauerkraut", "sriracha", "teriyaki sauce", "vinegar"],
        "meal": ["breakfast", "brunch", "lunch", "tea", "supper", "dinner", "midnight snack", "late night snack"],
        }

foodExpressions = ["anything [foodFlavor]",
                "[everyAllFood] [exceptBut] [food]",
                "[foodFlavor] food",
                "[food] that {!SHE!/[closePerson]} cooked",
                "[food](( that has been)) cooked by {!HER!/closePerson}",
                "[food] that has been reheated the next day",
                "[closePerson]'s [food]",
                "[food] that [closePerson] makes",
                "[food] with [condiment]"
                ]
badFoodExpressions = ["[food] flavored [flavoredFood]",
                "[food] fried rice",
                "[food] noodles",
                "[food] sushi",
                "mayo [food]",
                "jellied [food]"]

prefixExpressions = ["!SHE! eats {a lot/the most in the group}[prefixCombiner]",
        "!SHE! is a picky eater[prefixCombiner]",
        "!SHE! is a big food lover[prefixCombiner]",
        "When it comes to food ", ]

foodFacts = ["!SHE! ((also ))[eatsVerb] ([food])*3( and )",
"!SHE! ((also ))[eatsVerb] [food] [whenSituation]",
"!HER! ((second ))favorite ((type of ))[foodDish] ((to cook ))is [food]",
"[food] is !HER! ((second ))favorite food",
"[food] is one of !HER! favorite foods",
"A food !SHE! ((really ))[eatsVerb] is [food]",
"((Least ))favorite food: ([food])*4(, )",
"!SHE! prefers [food] to [food]",
"!SHE! {gets an allergic reaction to/is allergic to} ([food])*2( and )",
"!SHE! hiccups when !SHE! eats [food] ((-Update: It seems !SHE! has fixed this problem))",
"!SHE! doesn't usually eat [food], but sometimes wants to eat it",
"!SHE! will eat [food] only [whenSituation]",
"!SHE! only eats ([food])*2( and )",
"If !SHE! [wasWere] a food !SHE! would be [food]",
"Once !SHE! only ate ([food])*2( and ) for [timePeriod]",
"A food that !SHE! will eat without doubt is [food]",
"If !SHE! had to eat one food for [timePeriod] !SHE! would eat [food]",
"!SHE! can finish [food] in [shortTimePeriod]",
"A food !SHE! wants to eat even after !SHE! just ate it is [food]",
"!HER! nickname is [noExpressionFood]nator",
"!HER! go-to snack [whenSituation] is [food]",
"When dieting, !SHE! craves [food] the most",
"!SHE! is addicted to [food]",
"!SHE! can guess the brand of [food] just from the taste",
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
    txt = factProcessor.processABCChoice(txt)
    txt = factProcessor.processAsterisk(txt)

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
    return txt


words["food"] = getFoods()
words["noExpressionFood"] = words["food"]


def debug():
    for i in range(10):
        txt = random.choice(foodFacts)
        txt = processFactTemplate(txt)
        print(txt)


def getFacts(n):
    factList = random.sample(foodFacts, n)
    processedList = [processFactTemplate(txt) for txt in factList]
    return processedList
