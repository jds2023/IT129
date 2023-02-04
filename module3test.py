#list examples
food = input("What do you want at the grocery store? ")
grocery_list = []
grocery_list.append(food)

 
print(grocery_list)


#input examples
name = input("What is your name? ")
print(f"\nHello, {name.lstrip().title()}!")

age = input("How old are you? ")
age = int(age)
print(f"\tI am {age.strip()} years old!")