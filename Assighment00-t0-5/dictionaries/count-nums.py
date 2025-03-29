def count_nums():
    numlist = [] 
    while True:
         userInput = input("enter number")
         if userInput == ""  :
             break 
         num = userInput   
         numlist.append(num) 
    return numlist         

def count_dic(numlistt):
    nums_dic = {}
    for num in numlistt:
        if num not in nums_dic:
            nums_dic[num] = 1
        else:
            nums_dic[num] += 1
    return nums_dic 
       
def print_counts(nums_dic):
    for num in nums_dic:
        print(f"{num} appears {nums_dic[num]} times ")

def main():
    user_number = count_nums()
    num_count =  count_dic(user_number)
    print_counts(num_count)
main()   