import random as r

unscrambled = input("Enter the 4 digits: ")
a = unscrambled[0]
b = unscrambled[1]
c = unscrambled[2]
d = unscrambled[3]
combinations = [a + b + c + d]

while len(combinations) < 24:
    pos = [0, 1, 2, 3]
    comb = ["", "", "", ""]
    num = r.randint(0, 3)
    comb[pos[num]] = a
    pos.remove(pos[num])
    num = r.randint(0, 2)
    comb[pos[num]] = b
    pos.remove(pos[num])
    num = r.randint(0, 1)
    comb[pos[num]] = c
    pos.remove(pos[num])
    comb[pos[0]] = d
    comb = comb[0] + comb[1] + comb[2] + comb[3]
    if comb not in combinations:
        combinations.append(comb)
print("The different combinations of", unscrambled, "are as follows:")
for i in combinations:
    print(i)
