import os
os.system("cls")

while True:
    print("Welcome to the Read/Writer APP\n\t1) Read\n\t2) Write\n\t3) Exit\n")
    user_input1 = int(input("Choose between 1-3: "))
    if user_input1 == 1:
        user_input2 = input("You selected 'READ' Which file from? ")
        with open(user_input2, "r") as f:
            print(f.read())
    elif user_input1 == 2:
        user_input3 = input("You selected 'WRITE'. Which file to? ")
        user_input4 = input("What do you want to write? ")
        with open(user_input3, "w") as f:
            f.write(user_input4)
    else:
        break



