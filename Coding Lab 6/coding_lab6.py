import os
from toppings import check_pizza as check
from toppings import add_toppings as add
from toppings import remove_toppings as remove

os.system("cls")
print("*****Greetings, welcome to Pizza!*****")
pizza_toppings = []
while True:
    print("\n\t1) Add toppings\n\t2) Remove toppings\n\t3) Check out your pizza\n\t4) Exit")
    user_input = int(input("Please select a number: "))
    if user_input == 1:
        user_input2 = input("Which topping would you like to add: ").title()
        add(user_input2, pizza_toppings)
    elif user_input == 2:
        user_input3 = input("Which topping would you like to remove: ").title()
        remove(user_input3, pizza_toppings)
    elif user_input == 3:
        check(pizza_toppings)
    else:
        break
    
    




