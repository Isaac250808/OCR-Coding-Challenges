import random

symbols = ["Cherry","Bell","Lemon","Orange","Star","Skull"]
bal = 100
play = True
print("You have £1")

while play:
    input("Press enter to roll (-£0.2)")
    symb1 = symbols[random.randint(0,5)]
    symb2 = symbols[random.randint(0,5)]
    symb3 = symbols[random.randint(0,5)]
    print(f"SYMBOLS ROLLED:  {symb1}  {symb2}  {symb3}")
    bal -= 20
    if symb1 == symb2 or symb2 == symb3 or symb1 == symb3:
        if symb1 == symb2 and symb2 == symb3:
            if symb1 == "Bell":
                bal += 500
            elif symb1 == "Skull":
                bal = 0
            else:
                bal += 100
        else:
            if symb1 == "Skull" or symb2 == "Skull":
                bal -= 100
            else:
                bal += 50
    if bal <= 0:
        print("Ran out of money.")
        play = False
    else:
        print(f"Your balance is £{bal/100}")
        if input("Do you want to quit with your earnings? (y/anything else) --> ").lower() == "y":
            play = False
            print(f"You have quit with a balance of {bal}")

