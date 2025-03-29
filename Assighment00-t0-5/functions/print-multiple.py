def repeat_message(message:str,repeat:int):
    for i in range(repeat):
        print(message)
         
def main() :
    user_input1 = input("enter the message") 
    user_input2 = int(input("enter the number of times") ) 
    repeat_message(user_input1,user_input2)
main()    
        

