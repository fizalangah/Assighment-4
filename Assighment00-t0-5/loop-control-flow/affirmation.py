def correct_sentence():
    affirmation = "I am capable of doing anything I put my mind to."
    while True:
        userInput = input("Please type the following affirmation: I am capable of doing anything I put my mind to.\n")
        if userInput == affirmation:
            print("thats right sentence")
            break
        else:
            print("incorrect sentence try again")    
correct_sentence()       