def happyNumber(n):
    tried = []
    while n != 1 and n not in tried:
        tried.append(n)
        temp = str(n)
        total = 0
        for i in range(len(temp)):
            total += int(temp[i])**2
        n = total
    if n == 1:
        return True
    else:
        return False

for i in range(1,9):
    print(f"{i}: {happyNumber(i)}")
