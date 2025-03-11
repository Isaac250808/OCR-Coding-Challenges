classification_tree = [
    "Does it have legs?",
    [
        "Is it a mammal?",
        [
            "Is it a carnivore?",
            [
                "Is it commonly domesticated?",
                ["Does it have sharp claws?", ["ANSWERCat"], ["ANSWERDog"]],
                ["Does it have stripes?", ["ANSWERTiger"], ["ANSWERLion"]],
            ],
            [
                "Does it have wool?",
                ["ANSWERSheep"],
                [
                    "Is it often ridden?",
                    ["ANSWERHorse"],
                    ["Is it milked?", ["ANSWERCow"], ["ANSWERPig"]],
                ],
            ],
        ],
        [
            "Is it a bird?",
            [
                "Does it have very long legs?",
                ["ANSWEROstrich"],
                [
                    "Is it rare to find in a typical garden?",
                    ["ANSWERPenguin"],
                    ["ANSWERSparrow"],
                ],
            ],
            [
                "Can it fly?",
                ["Can it sting without dying?", ["ANSWERWasp"], ["ANSWERBee"]],
                [
                    "Does it have 8 legs?",
                    ["ANSWERSpider"],
                    ["Is it known to eat wood?", ["ANSWERTermite"], ["ANSWERAnt"]],
                ],
            ],
        ],
    ],
    [
        "Is it a mammal?",
        [
            "Does it have fins?",
            ["Does it have a long, narrow snout?", ["ANSWERDolphin"], ["ANSWERWhale"]],
            ["ANSWERSeal"],
        ],
        ["Does it have 8 arms and 2 tentacles?", ["ANSWERSquid"], ["ANSWEROctopus"]],
    ],
]


def checkAnswer(list):
    if list[0][0:6] == "ANSWER":
        return list[0][6:]
    else:
        print(list[0], "(yes/no)")
        while True:
            yesOrNo = input().lower()
            if yesOrNo == "yes" or yesOrNo == "y":
                return checkAnswer(list[1])
                break
            elif yesOrNo == "no" or yesOrNo == "n":
                return checkAnswer(list[2])
                break
            else:
                print("Invalid input. Try again")


print("Your animal is:", checkAnswer(classification_tree))
