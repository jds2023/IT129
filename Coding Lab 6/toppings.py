def check_pizza(toppings):
    print("Your pizza has the following toppings:")
    for x in toppings:
        print(f"{x.title()}")

def add_toppings(top, toppings):
    toppings.append(top)

def remove_toppings(top, toppings):
    toppings.remove(top)


