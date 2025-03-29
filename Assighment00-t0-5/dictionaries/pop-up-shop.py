def fruit_shop():
    fruits = {
    "apple":200,"banana":100,"kiwi" :150,"mango":500   
    }

    total =  0

    for fruitnames in fruits:
        price = fruits[fruitnames]
        bought_amount = int(input(f"how many { fruitnames}  do you want"))
        total += ( price * bought_amount )
    print(total)
fruit_shop()   
         
     
         

# def main():
#     fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
#     total_cost = 0
#     for fruit_name in fruits:
#         price = fruits[fruit_name]
#         amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
#         total_cost += (price * amount_bought)
    
#     print("Your total is $" + str(total_cost))


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()
 
