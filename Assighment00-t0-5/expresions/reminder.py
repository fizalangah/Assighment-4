# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def reminder():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1: int = int(num1)
    num2: int = int(num2)
    div = num1 // num2
    rem = num1 % num2
    print("The result of dividing the first number by the second is", div)
    print("The remainder of the division is", rem)
reminder()    