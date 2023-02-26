#EXAMPLE 1
#def greet_user():
    #print("Hello!")

#def greet_user2(username):
    #print(f"Hello, {username.title()}") #username is a parameter, 'justin' is an argument

#def greet_user3():
    #print("Hello3!")

#greet_user2('justin')


#EXAMPLE 2
#def favorite_book(book, year):
    #print(f"One of my favorite books is {book.title()} from the year {year}")

#favorite_book('Lord of the Rings', '2007')
#favorite_book(year = 2000, book = "Harry Potter") <-- to assign 

#EXAMPLE 3
def city_country(city, country):
    formal_address = f"{city}, {country}"
    return formal_address.title()

pair1 = city_country("Quebec", "Canada")
print(pair1)
pair2 = city_country("Seattle", "USA")
print(pair2)
pair3 = city_country("Morrocco", "Mexico")

