group_info = []
#Groups user information into a list
group_info.append(input("What is the name of the reservations? ").title())
group_info.append(int(input("How many people are coming? ")))
group_info.append(input("Preferred location? (inside or outside) ").lower())

print(f"{group_info[0]}'s group booked a table for {group_info[1]} people. They want to eat {group_info[2]}.")