import random
def game():
  
    computerscore = 0
    
    while True:
        my_randomNumber = random.randint(1,50)
        computersRandomNumber = random.randint(1,50)
        user_Input = str(input("Do you think your number is higher or lower than the computer's?:"))
        
        if user_Input == "higher":
            if my_randomNumber > computersRandomNumber:
               myscore += 1
               print(f"You were right! The computer's number was  {computersRandomNumber} my score = {myscore}")
             
            elif my_randomNumber < computersRandomNumber:
                 computerscore +=1
                 print(f"Aww, that's incorrect. The computer's number was  {computersRandomNumber} computer score = {computerscore} ") 
                 

        elif user_Input == "lower":
            if my_randomNumber < computersRandomNumber:
               myscore += 1
               print(f"You were right! The computer's number was   {computersRandomNumber}  my score = {myscore}")
               
            elif my_randomNumber > computersRandomNumber:
                 computerscore += 1
                 print(f"Aww, that's incorrect. The computer's number was  { computersRandomNumber} computer score = {computerscore}") 
                  
        if myscore == 5 or computerscore == 5:
           break          
    if myscore > computerscore:
        print(f"congratulations you wins your total score is  {myscore}")
    else:
        print( f"you loss! because computers score {computerscore} is more than yours {myscore}" )
game() 


        