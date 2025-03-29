import random
def guess_my_number():
    while True:
     user_input = int(input("Guess the number which I am thinking"))
     mynumber = random.randint(0,99)
    
     if user_input == mynumber:
        print("congratulations  you guess the correct number")
        break
     elif user_input > mynumber:
        print("your guessed number is too high")
     elif user_input < mynumber:
        print("your guessed number is too low ") 
     else:
        print("you guees the wrong number try again")  
guess_my_number()             

    