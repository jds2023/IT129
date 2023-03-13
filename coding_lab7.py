import os
os.system("cls")

student_1 = {'name':'Justin',
             'age': 19,
             'grade':'A'}
student_2 = {'name': 'Mark',
             'age': 18,
             'grade': 'D'}
student_3 = {'name': 'Sarah',
             'age': 21,
             'grade': 'B'}

while True:

    user_input1 = int(input("What do you want to do? \n\t1) See all the students information\n\t2) Modify their grade\n\t3) Exit\nPlease select a number "))

    if user_input1 == 1:
        print(f"\n{student_1['name']} is {student_1['age']} and his grade is {student_1['grade']}")
        print(f"{student_2['name']} is {student_2['age']} and his grade is {student_2['grade']}")
        print(f"{student_3['name']} is {student_3['age']} and his grade is {student_3['grade']}\n")

    elif user_input1 == 2:
        user_input2 = int(input("Which student's grade do you want to modify? (1, 2 or 3)? "))
        user_input3 = input("What grade does the student have now? ")

        if user_input2 == 1:
            student_1['grade'] = user_input3
        elif user_input2 == 2:
            student_2['grade'] = user_input3
        elif user_input2 == 3:
            student_3['grade'] = user_input3
        else:
            print(f"{user_input2} is not a valid option.")
    else:
        break


