import random
def guess_my_number():
    myNumber = random.randint(0,99)
    while True:
       numberInput = int(input("guess your number"))

       if numberInput == myNumber:
           print("congratulations you guesses the correct number")
           break
       elif numberInput > myNumber:
            print("your guessed number is too high try again")
       elif numberInput < myNumber:
            print("your gueesed number is too loo try again") 
           

   
guess_my_number()   