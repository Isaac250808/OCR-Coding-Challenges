factorialOfX = 4 # To try this out, put any number here

# Recursion
def factorial(num):
  if num == 0:
    return 1
  else:
    return num*factorial(num-1)
print("Recursion:",factorial(factorialOfX))

# Loop
total = 1
while factorialOfX > 0:
  total *= factorialOfX
  factorialOfX -= 1
print("Loop     :",total)
