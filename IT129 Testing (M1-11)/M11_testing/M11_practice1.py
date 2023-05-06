#PRACTICE 1
class Restaurant:
    def __init__(self, name, cuisine):
        self.brand = name
        self.food = cuisine

    def describe_restaurant(self):
        print(f"Restaurant: {self.brand}")
        print(f"Cuisine: {self.food}")

    def open_restaurant(self):
        print(f"{self.brand} is open!")

restaurant = Restaurant("Jersey Mikes", "Subs")

restaurant.describe_restaurant()
restaurant.open_restaurant()
