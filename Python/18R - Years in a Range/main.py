def checkRepeated(num):
    flag = False
    for i in range(len(str(num))):
        count = 0
        for j in range(len(str(num))):
            if str(num)[i] == str(num)[j]:
                count += 1
        if count > 1:
            flag = True
    return flag

yearStart = int(input("What is the start of the range (incl.) - "))
yearEnd = int(input("What is the end of the range (excl.) - "))

total = 0
for i in range(yearStart,yearEnd):
    result = checkRepeated(i)
    print(f"{i}: {result}")
    if result == True:
        total += 1
print(f"The total number of years with repeated digits is: {total}")
