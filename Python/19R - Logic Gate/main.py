print("LOGIC GATE: Enter a logic gate question, and the answer will be outputted")
print("(Type which number corresponding to the gate)")
print("""1: OR
2: AND
3: XOR
4: NAND
5: NOR""")
gate = int(input(">>> "))
input1 = int(input("Enter the first input  -  "))
input2 = int(input("Enter the second input -  "))
if gate == 1:
    if input1 == 1 or input2 == 1:
        result = 1
    else:
        result = 0

elif gate == 2:
    if input1 == 1 and input2 == 1:
        result = 1
    else:
        result = 0

elif gate == 3:
    if input1 == 1 or input2 == 1:
        if input1 == 1 and input2 == 1:
            result = 0
        else:
            result = 1
    else:
        result = 0

elif gate == 4:
    if input1 == 1 and input2 == 1:
        result = 0
    else:
        result = 1

elif gate == 5:
    if input1 == 1 or input2 == 1:
        result = 0
    else:
        result = 1

else:
    result = "Invalaid gate input (not 1, 2, 3, 4, or 5)"

print(result)
