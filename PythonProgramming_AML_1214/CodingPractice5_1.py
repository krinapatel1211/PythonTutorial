# 4-1. Pizzas
pizzas = ['Margerita', 'Peppi Paneer', 'Veg Extravegenza']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza} pizza!")

print("\nI love pizzas the most\nI like simple cheesy pizzas\nI am pizza lover.")
print("\nI really love Pizza!\n")

# 4-2. Animals
animals = ['Cat', 'Dog', 'Tiger']

print()
for animal in animals:
    print(animal)

for animal in animals:
    print("A {} would make a great pet.".format(animal))

print("\nThis animals are warm blooded\nThis animals belong to mammals\nThis animals stay on land")
print('\nAny of this animals would make a great pet!\n')

# 4-3. Counting to Twenty
for i in range(0, 21):
    print(i)

# 4-4. One Million
one_million_list = range(1000001)
# 1

# 4-5. Summing a million
one_million_list_1 = range(1, 10000001)
print("Minimum from List: ", min(one_million_list_1))
print("Minimum from List: ", max(one_million_list_1))
print("Sum of List: ", sum(one_million_list_1))

# 4-6. Odd Numbers
odd_numbers = range(1, 20, 2)
for i in odd_numbers:
    print(i)

# 4-13. Buffet
buffet_menu = ('Pulav', 'Burger', 'Pizza', 'Gulab Jamun', 'Masala Dosa')
print("Restaurant Buffet Menu: ")
for i in buffet_menu:
    print("\t", i)

# buffet_menu[0] = 'Samosa'

buffet_menu = ('Samosa', 'Masala idli', 'Pizza', 'Gulab Jamun', 'Masala Dosa')
print("Revised Buffet Menu: ")
for i in buffet_menu:
    print("\t", i)

# 8-3. T-Shirt
def make_shirt(size, message_text):
    print(f"The size of the shirt is {size} and the message printed on shirt is '{message_text}'")


make_shirt('XL', 'Hope Never Dies!')
make_shirt(size='XXL', message_text='Hope Never Dies!')


# 8-4. Large Shirts
def make_shirt(size='Large', message_text='I love Python'):
    print(f"The size of the shirt is {size} and the message printed on shirt is '{message_text}'")

make_shirt(size='Large')
make_shirt(size='Medium')
make_shirt(size='any size', message_text='All is Well!')

# 8-5. Cities
def describe_city(name, country='India'):
    print(f"{name} is in {country}")


describe_city(name='Bali', country='Indonesia')
describe_city(name='Toronto', country='Canada')
describe_city(name='Anand')

# 8-6. City Names
def city_country(city, country):
    print(f'"{city}, {country}"')

city_country('Bali', 'Indonesia')
city_country('Toronto', 'Canada')
city_country('Anand', 'India')

# 8-7. Album
def make_album(artist_name, album_title, no_of_songs=None):
    return {"Artist Name": artist_name, "Album Title": album_title, "Songs" : no_of_songs}

print(make_album("Arijit Singh", "Sun raha hai na tu"))
print(make_album("Atif Aslam", "Tere sang yaara"))
print(make_album("Taylor Shift", "Love Story"))

print(make_album("Selina", "Rare", 19))

# 8.8
while True:
    choice = input("Enter albums to dictionary(1/0):")
    if choice == "1":
        artist_name, album_title = input("Enter artist name and album title: ").split()
        print(make_album(artist_name, album_title))
    else:
        break













