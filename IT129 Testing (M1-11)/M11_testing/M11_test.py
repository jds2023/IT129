#Object Oriented Programming: 
class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increment_age(self):
        self.age = self.age + 1

    def roll_over(self):
        print(f"{self.name} is rolling over!")

#Main Program

#CREATING AN INSTANCE
my_dog = Dog("Millie", 2)
your_dog = Dog("Dallas", 9)
doge = Dog("Kevo", 5)

#CALLING THE METHODS
my_dog.sit()
your_dog.roll_over()
doge.sit()

