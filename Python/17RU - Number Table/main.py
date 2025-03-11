flag = True
while flag:
    userInput = input("Enter an operation and a number to make a number table (e.g. \"+4\") >>> ")
    if userInput[0] in ["+","-","*","/"]:
        if int(userInput[1:]) > 0:
            flag = False
        else:
            print("Number needs to be more than 0")
    else:
        print("First character must be either +, -, /, or *")

baseNums = []
if userInput[0] != "/":
    for i in range(int(userInput[1:])+1):
        baseNums.append(i)
else:
    for i in range(int(userInput[1:])):
        baseNums.append(i+1)

lineAcc = ""
lineAcc += userInput[0]+ " |"
for i in baseNums:
    lineAcc += " "+str(i)
print(lineAcc)
print(len(lineAcc)*"-")

for i in baseNums:
    lineAcc = str(i)+" |"
    if userInput[0] == "+":
        for j in baseNums:
            lineAcc += " "+str(j+i)
    elif userInput[0] == "-":
        for j in baseNums:
            lineAcc += " "+str(j-i)
    elif userInput[0] == "*":
        for j in baseNums:
            lineAcc += " "+str(j*i)
    else:
        for j in baseNums:
            lineAcc += " "+str(j/i)
    print(lineAcc)
