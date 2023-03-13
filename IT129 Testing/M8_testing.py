#LISTS
#user = ["justins4645", "mario"]
#TUPLES 
#dimensions = (200,50)
#DICTIONATIES
#alien_1 = {'color':'green','points':5}
#alien_1['x_position'] = 0

#-----EXAMPLE 1-----
friend_1 = {'name':'Nathan',
            'age':17,
            'city':'Fairfax'}

name_student = friend_1.get('food', "There is no favorite food")
print(name_student)

for x in friend_1.items():
    print(f"{x}")
#get(), items(), keys(), values()


