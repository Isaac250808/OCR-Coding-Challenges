import random

def askQuestion():
    operator = random.randint(0,3)
    if operator == 0:
        num1 = random.randint(1,24)
        num2 = random.randint(1,24)
        print(f"What is {num1} + {num2}?")
        answer = num1+num2
        userAnswer = float(input("--->  "))
        if answer == userAnswer:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect, the correct answer is {answer}.")
            return 0
    elif operator == 1:
        num1 = random.randint(1,24)
        num2 = random.randint(1,24)
        print(f"What is {num1} - {num2}?")
        answer = num1-num2
        userAnswer = float(input("--->  "))
        if answer == userAnswer:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect, the correct answer is {answer}.")
            return 0
    elif operator == 2:
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        print(f"What is {num1} x {num2}?")
        answer = num1*num2
        userAnswer = float(input("--->  "))
        if answer == userAnswer:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect, the correct answer is {answer}.")
            return 0
    else:
        num1 = random.randint(1,6)*2
        num2 = random.randint(1,5)*2
        print(f"What is {num1} / {num2}?")
        answer = num1/num2
        userAnswer = float(input("--->  "))
        if answer == userAnswer:
            print("Correct!")
            return 1
        else:
            print(f"Incorrect, the correct answer is {answer}.")
            return 0

name = input("What is your name? ")
form = input("What is your class (1, 2 or 3)? ")
score = 0
for i in range(10):
    score += askQuestion()
print(f"Your score was {score}!")

f = open("results.txt","r")
lines = f.readlines()
f.close()
print(lines)
for i in range(len(lines)):
    lines[i] = lines[i][:-1].split(";")
print(lines)
lines.append([name,form,str(score)])
lines.sort()
grouped = []
for i in range(len(grouped)):
    if grouped[i][]
#f.write(f"{name};{form};{score}\n")
