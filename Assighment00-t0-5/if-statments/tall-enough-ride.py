def tall_enough_for_ride():
    user_height = float(input("Enter your height in inches: "))
    if user_height >= 100:
        print("You are tall enough to ride!")
    elif user_height >= 10 and user_height <= 99:    
         print (" you can ride")
    else: 
        print("You are not tall enough to ride!")    
tall_enough_for_ride()        