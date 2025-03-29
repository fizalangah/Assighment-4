import random
def Game():
    paper = 1
    sessior = 2
    rock = 3
    myscore = 0
    computerscore = 0
    # computer = random.randint(0,3)
    while True:
        computer = random.randint(1,3) 
        user_input = str(input("Choose one option: paper,sessior : "))
        if user_input == "paper" and computer == paper or user_input == "rock" and computer == rock or user_input == "sessior"  and computer == sessior:
            print("game tie because your both choose same ")
        elif user_input == "paper" and computer == sessior: 
            computerscore +=1
            print(f"computer wins because you choose paper and computer choose sessior \n computer score is:  {computerscore}") 
        elif user_input == "sessior"  and computer == paper :
            myscore  += 1
            print(f"you wins because you choose sessior and computer choose paper \n your score is: { myscore}")
        elif user_input == "sessior"  and computer == rock :
            computerscore += 1
            print(f"computer wins because you choose sessior and computer choose rock \n computer score is:  {computerscore}")       
        elif user_input == "rock" and computer == sessior:
            myscore += 1
            print(f"you wins because you choose rock  and computer choose sessior \n your score is: {myscore}")
        elif user_input == "paper"  and computer == rock:
            myscore += 1
            print(f"you wins because you choose paper and computer choose rock  \n your score is:  { myscore}") 
        elif user_input == "rock"   and computer == paper:
            computerscore += 1
            print(f"computer wins because computer choose paper and you choose rock \n computer score is: { computerscore}")   
        if myscore == 5 or computerscore == 5:
            break
    if myscore > computerscore:
        print(f"you wins because your score is more than computer score:   {myscore}")
    else:
        print(f"you loose because computer score is more than your score:   {computerscore}")    
Game()     

    
