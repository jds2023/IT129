name = input("Before playing this game, what is your name? ")
print(f"\nHi {name}! Let's see if you can win this decision making game\n")

print("You are standing in a dark room")
print("There are three doors in front of you with the following signs:")

option_list = ["Angry Tiger","Bear with chains","Ghost with knife"]
for x in option_list:
    print(f"\t{x}")

option1 = int(input("Which door do you want to pick (1, 2 or 3: )? "))

if option1 == 1:
    print (f"You chose \"{option_list[0]}\" \nThat was a terrible mistake!\nThe tiger is so angry, you don't stand a changes")
elif option1 == 2:
    print (f"You chose \"{option_list[1]}\" \nOh no! When the bear see's you it breaks its chains and eats you alive!")
else:
    print('Right choice! The ghost is too busy making fun of the tiger and the bear that its knife is on the floor')
    print("You have two choices")
    print("\t1.) Pick up the knife and try to kill him before he kills you")
    print("\t2.) Wait until the ghost stops making fun of them")

    option2 = int(input("Which door do you want to pick (1, or 2: )? "))

    if option2 == 1:
        print("The ghost sees you trying to pick up the knife\nHowever the ghost is faster and kills you before you can kill it")
    else: 
        print("You Win!")
        

print ("\nGAME OVER")