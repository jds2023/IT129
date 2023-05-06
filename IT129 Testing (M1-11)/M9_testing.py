#user_input = input("Which file do you want to read from?")

with open("test1.txt") as f:
    contents = f.readlines()

print(contents)