#User inputs for (), customers is integer
reservation_name = input("What is the name of the reservations? ")
customers = input("How many people are coming? ")
customers = int(customers)
location = input("Preferred location? (inside or outside) ")
#Groups user information into a list
group_info = [] 
group_info.append(reservation_name)
group_info.append(customers)
group_info.append(location)

print(f"{group_info[0].capitalize()} booked a table for {group_info[1]} people. They want to eat {group_info[2].lower()}.")