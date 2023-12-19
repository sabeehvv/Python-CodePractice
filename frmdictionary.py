def Butterchicken():
    for i in range (len(recipes["Butter chicken"])):
        items = recipes["Butter chicken"][i]
        pantry[items]-=1
    print("\n Butter Chicken is ready \n Items left in the pantry are : ",pantry)


def ChickenAndChips():
    for i in range(len(recipes["Chicken and chips"])):
        items =recipes["Chicken and chips"][i]
        pantry[items] -=1
    print("\n Chicken and Chips is ready \n Items lest in the pantry are :",pantry)

def pizza():
    for i in range(len(recipes["Pizza"])):
        items =recipes["Pizza"][i]
        pantry[items] -=1
    print("\n Pizza is ready \n Items lest in the pantry are :",pantry)

def EggSandwich():
    for i in range(len(recipes["Egg sandwich"])):
        items =recipes["Egg sandwich"][i]
        pantry[items] -=1
    print("\n Egg Sandwich is ready \n Items lest in the pantry are :",pantry)

def BeansOnToast():
    for i in range(len(recipes["Beans on toast"])):
        items =recipes["Beans on toast"][i]
        pantry[items] -=1
    print("\n Beans on Toast is ready \n Items lest in the pantry are :",pantry)

def SpamALaTin():
    for i in range(len(recipes["Spam a la tin"])):
        items = recipes["Spam a la tin"][i]
        pantry[items] -=1
    print("\n Spam a la tin is ready \n Items lest in the pantry are :",pantry)


pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
    "beans":5,
    "bread":5,
    "potatoes":5,
    "salt":3,
    "malt vinegar":3,
    "butter":4,
    "tin opener":4,
    "spoon":4
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}


choice = int(input("Enter: \n 1 :Butter Chicken \n 2 :Chicken and Chips \n 3 :Pizza \n 4:Egg Sandwich \n 5 : Beans on Toast \n 6 :spam a la tin \n"))

match choice:
    case 1:
        Butterchicken()
    case 2:
        ChickenAndChips()
    case 3:
        pizza()
    case 4:
        EggSandwich()
    case 5:
        BeansOnToast()
    case 6:
        SpamALaTin()
    case other:
        print("Enter correct Number")