running = True
print("""WELCOME TO THE CALCULATOR
Each type of calculator has an assigned number, type the number of the desired calculator to use it:
    1: VAT
    2: Tax
    3: Times Table""")
calculator = input(">>> ")
while running:
    if calculator != "":
        if calculator == "1":
            typeOfVAT = input("What type of VAT would you like to perform? (include/exclude) - ").lower()[0]
            rate = 1 + float(input("What is the rate of VAT? (the percent, without the percent symbol) - "))/100
            amount = float(input("What is the amount? - "))
            if typeOfVAT == "i":
                print(amount*rate)
            elif typeOfVAT == "e":
                print(amount/rate)
            else:
                print("Invalid type of VAT input detected. Please try again")
        elif calculator == "2":
            rate = 1 - float(input("What is the rate of tax? (how much tax to deduct, in percent, without the % symbol) - "))/100
            amount = float(input("What is the amount to calculate the \"take-home\" from? - "))
            print(amount * rate)
        elif calculator == "3":
            num1 = int(input("What number do you want to base the times table around? - "))
            num2 = int(input("What number do you want to times the base number up to? - "))
            for i in range(num2):
                print(f"{num1} x {i+1} = {num1*(i+1)}")
        print("Would you like to perform another calculation? (y/n)")
        if input(">>> ").lower() == "y":
            print("""Which calculation would you like to do?  (or enter nothing to end the program)
    1: VAT
    2: Tax
    3: Times Table""")
            calculator = input(">>> ")
        else:
            running = False
    else:
        running = False
