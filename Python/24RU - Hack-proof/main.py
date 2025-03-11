import urwid

def read():
    f = open("cred.txt", "r")
    cred = f.readlines()
    f.close()
    print("Which file would you like to open?")
    for i in range(len(cred)):
        cred[i] = cred[i].strip().split(";")
        print(f"{i+1}: {cred[i][2]} - {cred[i][0]}")
    choice = int(input(">>> "))-1

    passAttempt = input("Password - ")
    while passAttempt != cred[choice][1]:
        print("""Invalaid password.
(password must have at least: 8 characters, one uppercase, one lowercase, and one special)
Please try again.""")
        passAttempt = input("Password - ")
    print("Well done, you are in!\nHeres the file:")
    f = open(cred[choice][2]+".txt","r")
    file = f.readlines()
    f.close()

    for i in file:
        print(i[:-1])

def signUp():
    name = input("What would you like your username to be? - ")+"\n"
    f = open("users.txt","r")
    file = f.readlines()
    f.close()
    while name in file:
        print("Name taken. Please try again.")
        name = input(">>> ")
    f = open("users.txt","a")
    f.append(name)
    f.close()

def make():
    pass

def edit():
    pass

print("Welcome to the secure file vault!")
print("""Which function would you like to perform?
1: Signup
2: Read file
3: Make file
4: Edit file""")
option = input(">>> ")

while option not in ["1","2","3","4"]:
    print("Invalid input. Please try again.")
    option = input(">>> ")

if option == "1":
    signUp()
elif option == "2":
    read()
elif option == "3":
    make()
else:
    edit()

