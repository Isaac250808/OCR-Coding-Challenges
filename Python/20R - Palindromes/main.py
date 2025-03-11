def checkPalin(string):
    reverse = string[::-1]
    count = 0
    for i in range(len(string)):
        if reverse[i] == string[i]:
            count += 1
    if count == len(string):
        return True
    else:
        return False

print(checkPalin("t2552t"))
