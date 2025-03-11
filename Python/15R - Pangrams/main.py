print("Enter a string (on one line), then True will be outputted if it is a panagram, and False if not. (enter nothing to end program)")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
flag = True
while flag:
    string = input()
    if len(string) != 0:
        total = 0
        for i in range(26):
            if alphabet[i] in string:
                total += 1
        if total != 26:
            print("False")
        else:
            print("True")
    else:
        flag = False
