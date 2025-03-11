def fibo(n): # Returns the value at nth index in fibonacci sequence
    if n > 1:
        return fibo(n-1)+fibo(n-2)
    elif n == 1:
        return 1
    else:
        return 0
def fiboSeq(n): # Returns all values of fibonacci sequence until nth index's value as array
    arr = []
    for i in range(n+1):
        arr.append(fibo(i))
    return arr
def fiboTot(n): # Returns total of all values of fibonacci sequence until nth index's value
    arr = fiboSeq(n)
    tot = 0
    for i in arr:
        tot += i
    return tot
def reverse(arr): # Returns the array inputted reversed
    arr.reverse()
    return arr

print(fibo(3)) # Prints the value at 3rd index in fibonacci sequence
print(fiboSeq(10)) # Prints all values of fibonacci sequence until 10th index's value
print(fiboTot(10)) # Prints total of all values of fibonacci sequence until 10th index's value
print(reverse(fiboSeq(10))) # Prints all values of fibonacci sequence until 10th index's value reversed

userInput = int(input("How many places would you like to generate? "))
sequence = fiboSeq(userInput-1)
print(sequence)
print("In reverse:",reverse(sequence))
total = 0
for i in sequence:
    total += i
print("Sum of all numbers shown:",total)
