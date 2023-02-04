group_info = []
#Groups user information into a list
group_info.append(input("What is the name of the reservations? ")
group_info.append(input(int("How many people are coming? ")))
group_info.append(input("Preferred location? (inside or outside) "))

#User inputs for (), customers is integer
# reservation_name = input("What is the name of the reservations? ")
# customers = input("How many people are coming? ")
# customers = int(customers)
# location = input("Preferred location? (inside or outside) ")

print(f"{group_info[0].capitalize()} booked a table for {group_info[1]} people. They want to eat {group_info[2].lower()}.")