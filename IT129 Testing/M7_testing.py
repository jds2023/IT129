#Passing a List
#def format_list(names):
    #for x in names:
        #print(x.upper())

#usernames = ["Hannah", "Colton", "Mark"]
#format_list(usernames)

def print_students(class_size, *students):
    print(students)
    print(class_size)

print_students(1,"Sarah")
print_students(20, "Alex")