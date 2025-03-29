def double_it():
    num = int(input("Enter the number"))
    
    while num < 100:
       double = num * 2
       print(f"{num} is double {double}")
       num = double
       
double_it()        

