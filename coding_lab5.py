import os
os.system("cls")

import secrets

print("Hi! Welcome to the Calculator App!")

while True:
    print("\nWhat do you want to do?\n\t1) Addition\n\t2) Subtraction\n\t3) Multiplication\n\t4) Division\n\t5) Power\n\t6) Random\n\t7) Exit")
    user_input = int(input("Choose: "))
    if user_input == 1: #ADDITION

        def addition(a, b):
            return a + b 

        add1 = int(input("\nFirst number: "))
        add2 = int(input("Second number: "))

        sum1 = addition(add1, add2)

        print(f"The result is {sum1}")

    elif user_input == 2: #SUBTRACTION
        def subtraction(a, b):
            return a - b
        
        sub1 = int(input("\nFirst number: "))
        sub2 = int(input("Second number: "))

        sum2 = subtraction(sub1, sub2)
         
        print(f"The result is {sum2}")

    elif user_input == 3: #MULTIPLICATION
        def multiplication(a, b):
            return a * b
        
        multi1 = int(input("\nFirst number: "))
        multi2 = int(input("Second number: "))

        sum3 = multiplication(multi1, multi2)

        print(f"Result is {sum3}")

    elif user_input == 4: #DIVISION
        def division(a, b):
            return a / b
        
        div1 = int(input("\nFirst number: "))
        div2 = int(input("Second number: "))

        sum4 = division(div1, div2)

        print(f"Result is {sum4}")

    elif user_input == 5: #EXPONENTS
        def power(a, b):
            return a ** b
        
        exp1 = int(input("\nFirst number: "))
        exp2 = int(input("Second number: "))

        sum5 = power(exp1, exp2)

        print(f"Result is {sum5}")

    elif user_input == 6: #RANDOM OPERATOR
        computer_choice = secrets.choice(['ADDITION','SUBTRACTION','MULTIPLICATION','DIVISION','POWER'])
        def random(a, b):
            if computer_choice == 'ADDITION':
                return a + b
            elif computer_choice == 'SUBTRACTION':
                return a - b
            elif computer_choice == 'MULTIPLICATION':
                return a * b
            elif computer_choice == 'DIVISION':
                return a / b
            else:
                return a ** b
        
        random1 = int(input("\nFirst number: "))
        random2 = int(input("Second number: "))

        sum6 = random(random1, random2)

        print(f"Random generator chose the {computer_choice.upper()} operator. Result is {sum6}")

    elif user_input == 7:
        break

    else:
        print(f"The operator {user_input} is invalid.")






