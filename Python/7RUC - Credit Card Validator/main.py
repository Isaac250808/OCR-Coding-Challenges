def checkSum(number):
    if " " not in number:
        if len(number) == 16:
            total = 0
            for i in range(16):
                total += int(number[i])
            return total

print(checkSum("4217660123456784"))
