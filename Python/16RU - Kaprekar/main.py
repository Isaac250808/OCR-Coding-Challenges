def kaprekar(number):
    squareNumber = number ** 2
    squareDigits = [0]
    for i in range(len(str(squareNumber))):
        squareDigits.append(int(str(squareNumber)[i]))
    flag = False
    for i in range(len(squareDigits)-1):
        list1 = squareDigits[0:i+1]
        list2 = squareDigits[i+1:]
        num1 = ""
        for j in list1:
            num1 += str(j)
        num1 = int(num1)
        num2 = ""
        for j in list2:
            num2 += str(j)
        num2 = int(num2)
        if num1+num2 == number:
            flag = True
    return flag

print(kaprekar(9))
