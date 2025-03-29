# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a workin

# num1 =  int(input ("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# sum = int(num1 + num2)
# print("The sum of the two numbers is", sum)

def addNumbers():

    num1  = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1: int = int(num1)
    num2: int = int(num2)
    sum = num1 + num2
    print("The sum of the two numbers is",str( sum))
addNumbers()