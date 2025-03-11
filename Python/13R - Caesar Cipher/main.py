def encode(string,key):
    alphabet = [["a", "a"], ["b", "b"], ["c", "c"], ["d", "d"], ["e", "e"], ["f", "f"],
 ["g", "g"], ["h", "h"], ["i", "i"], ["j", "j"], ["k", "k"], ["l", "l"],
 ["m", "m"], ["n", "n"], ["o", "o"], ["p", "p"], ["q", "q"], ["r", "r"],
 ["s", "s"], ["t", "t"], ["u", "u"], ["v", "v"], ["w", "w"], ["x", "x"],
 ["y", "y"], ["z", "z"]]

    for i in range(key):
        last = alphabet[0][1]
        for i in range(25):
            alphabet[i][1] = alphabet[i+1][1]
        alphabet[25][1] = last
    result = ""
    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(26):
                if string[i].lower() == alphabet[j][0]:
                    if string[i].isupper():
                        result += alphabet[j][1].upper()
                    else:
                        result += alphabet[j][1]
        else:
            result += string[i]
    return result

def decode(string,key):
    alphabet = [["a", "a"], ["b", "b"], ["c", "c"], ["d", "d"], ["e", "e"], ["f", "f"],
 ["g", "g"], ["h", "h"], ["i", "i"], ["j", "j"], ["k", "k"], ["l", "l"],
 ["m", "m"], ["n", "n"], ["o", "o"], ["p", "p"], ["q", "q"], ["r", "r"],
 ["s", "s"], ["t", "t"], ["u", "u"], ["v", "v"], ["w", "w"], ["x", "x"],
 ["y", "y"], ["z", "z"]]

    for i in range(key):
        last = alphabet[0][1]
        for i in range(25):
            alphabet[i][1] = alphabet[i+1][1]
        alphabet[25][1] = last
    result = ""
    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(26):
                if string[i].lower() == alphabet[j][1]:
                    if string[i].isupper():
                        result += alphabet[j][0].upper()
                    else:
                        result += alphabet[j][0]
        else:
            result += string[i]
    return result

flag = False
while not flag:
    print("Do you want to encode or decode? [1/2]")
    encodeORdecode = input(">>> ")
    if encodeORdecode == "1" or encodeORdecode == "2":
        flag = True
    else:
        print("Try again. 1 OR 2 was not inputted")
flag = None
if encodeORdecode == "1":
    print("You have chosen to encode!")
    encoded = encode(input("What string would you like to encode? "),int(input("What key would you like to use? ")))
    print(f"""
Your encoded message is:
    {encoded}""")
else:
    print("You have chosen to decode!")
    decoded = decode(input("What string would you like to decode? "),int(input("What key would you like to use? ")))
    print(f"""
Your decoded message is:
    {decoded}""")
