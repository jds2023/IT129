#EXAMPLE 4
status = True

while status:
    application = input("type 'quit' or 'exit' to close the program ")
    if application == 'quit':
        break
    elif application == 'exit':
        status = False
    else:
        print(application)


#EXAMPLE 3
#active = True
#while active:
    #message = input("'quit' to exit ")
    #if message == 'quit': #break
        #active = False
    #else:
        #print(message)

#EXAMPLE 1
#buffet = ("eggs", "bacon", "croissant", "sausage", "pancakes")
#for food in buffet:
#    print(f"\t{food}")

#EXAMPLE 2
#current_number = 1

#while current_number <=5:
    #print(current_number)
    #current_number += 1 #OR number = number + 1
