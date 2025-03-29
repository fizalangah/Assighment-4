def febonic_number(num1,num2, maxValue):
   
    
    while num1 <= maxValue:
        print(num1)
        total =num1 + num2 
        num1 = num2
        num2 = total
 
febonic_number(0,1,2000)     

    
    