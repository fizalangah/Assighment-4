def divisor_numbers(num):
    for i in range(num):
        curr = i + 1
        if num % curr == 0:
            print(curr)
def main():
    userinput = int(input("enter the number")) 
    divisor_numbers(userinput)
main()               


    


    