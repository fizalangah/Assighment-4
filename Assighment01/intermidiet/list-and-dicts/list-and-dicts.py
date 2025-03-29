# list and dicts
#1: List Practice
list_of_fruit = list(['apple', 'banana', 'orange', 'grape', 'pineapple']
)
def access():
    user_input = int(input("Enter the index of list: "))
    print(list_of_fruit[user_input])
     
def update():
    curr_input = int(input("Enter the index number: "))
    update_input = str(input("Enter the new element: "))
    list_of_fruit[curr_input] = update_input
    print(list_of_fruit)

def slicing():
    start_input = int(input("Enter the start index: "))
    end_input = int(input("Enter the end index: "))
    lst = list_of_fruit[start_input:end_input]
    print(lst)
      
def final_game():
    stop = ""
    while True:
       
        operation = str(input("Which operation do you want to perform? Access, Update , Slicing! "))    

        if operation == "access":
           access()
        elif operation == "update":
             update()
        elif operation == "slicing":
             slicing()
       
        if operation == stop:
           break
    
             
final_game()
    
     
       
        
