from random import randint as r
from time import sleep as s

f = open("questions.txt","r")
questions = f.readlines()
f.close()

print(f"""Welcome to my general knowledge quiz!

=====================================

10 Questions will be picked at random from {len(questions)}.
Enter the letter, NOT the content of the answer
Get as many as you can right!""")

s(5)
print("")
qus = []
while len(qus) < 10:
    num = r(0,len(questions)-1)
    qus.append(questions[num])
    questions.remove(questions[num])
for i in range(len(qus)):
    qus[i] = qus[i][:-1].split(";")

score = 0

for i in range(len(qus)):
    print(f"""{i+1}) {qus[i][0]}
    {qus[i][1]}
    {qus[i][2]}
    {qus[i][3]}""")
    answer = input(">>> ").lower()
    if answer == qus[i][4]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect, the answer was",qus[i][4])
    print("")

print(f"Your score was overall {score} out of 10.")
if score == 10:
    print("What a genius!")
elif score >= 8:
    print("Great score!")
elif score >= 5:
    print("Well done")
elif score >= 3:
    print("Good attempt")
elif score >= 1:
    print("You'll do better next time?")
else:
    print("This is statistically very unlikely.")
if score >= 9:
    g = "A*"
elif score >= 7:
    g = "A"
elif score == 6:
    g = "B"
elif score == 5:
    g = "C"
elif score >= 3:
    g = "D"
elif score >= 2:
    g = "E"
else:
    g = "FAIL"
print("Your grade is:",g)

