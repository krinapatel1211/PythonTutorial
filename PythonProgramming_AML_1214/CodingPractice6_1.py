# 5-1 Conditional Tests:
car = 'audi'
print("Is car == 'Ferrari' ? I predict True")
print(car == 'Ferrari')

print("Is car == 'audi' ? I predict False")
print(car == 'audi')

print("Is car == 'Limousine' ? I predict False")
print(car == 'Limousine')

print("Is car == 'Lambourghini' ? I predict False")
print(car == 'Lambourghini')

print("Is car == 'Rogue' ? I predict False")
print(car == 'Rogue')

print("Is car == 'Bentley' ? I predict False")
print(car == 'Bentley')

print("Is car == 'Qualis' ? I predict False")
print(car == 'Qualis')

print("Is car == 'Swift' ? I predict False")
print(car == 'Swift')

print("Is car == 'Wagonar' ? I predict False")
print(car == 'Wagonar')

print("Is car == 'Civic' ? I predict False")
print(car == 'Civic')

# 5-2 More Conditional Tests:
car = "Honda City"
print("\nIs car == 'Honda City' ? I predict False")
print(car == 'Honda City')

car = "Honda City"
print("\nIs car == 'Fortuner' ? I predict False")
print(car == 'Fortuner')

car = "Fortuner"
print("Test for equality: ", car == "Fortuner")
print("Test for inequality: ", car != "Fortuner")
print("Test for equality : ", car.lower() == "Fortuner")

no_of_cars, no_of_bike = 10, 5
print("Test for equality: ", no_of_cars == no_of_bike)
print("Test for inequality: ", no_of_cars != no_of_bike)
print("Test for greater than : ", no_of_cars > no_of_bike)
print("Test for less than : ", no_of_cars < no_of_bike)
print("Test for greater than or equal to : ", no_of_cars >= no_of_bike)
print("Test for less than or equal to : ", no_of_cars <= no_of_bike)

a, b = 2, 4
print("and keyword: ", a and b)
print("or keyword", a or b)

list1 = ['Bread', 'butter','Ghee','bagel']
print("Bread exist in list1 or not: ")
for i in list1:
    if i == 'Bread':
        print("{} exists".format(i))
        break;
    else:
        print("{} does not exists".format(i))

# 5-3. Alien Colors #1:
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points!")
else:
    pass

# 5-4. Alien Colors #2:
color = 'green'
if color == 'green':
    print("The player just earned 5 points for shooting the alien!")
else:
    print("The player just earned 10 points!")

color = 'yellow'
if color == 'green':
    print("The player just earned 5 points for shooting the alien!")
else:
    print("The player just earned 10 points!")

# 5-5. Alien Colors #3:
color = 'yellow'
if color == 'green':
    print("The player just earned 5 points!")
elif color == 'yellow':
    print("The player just earned 10 points!")
elif color == 'red':
    print("The player just earned 15 points!")

# 5-6. Stages of Life:
age = 2
if age < 2:
    print("the person is baby")
elif age == 2 or age < 4:
    print("the person is toddler")
elif age == 4 or age < 13:
    print("the person is kid")
elif age == 13 or age < 20:
    print("the person is teenager")
elif age == 20 or age < 65:
    print("the person is adult")
elif age >= 65:
    print("the person is an elder")

# 5-7. Favourite Fruit:
favourite_fruits = ['Apple', 'Strawberry', 'Kiwi']
if "Apple" in favourite_fruits:
    print("You really like Apple!")

if "Strawberry" in favourite_fruits:
    print("You really like Strawberry!")

if "Kiwi" in favourite_fruits:
    print("You really like Kiwi!")

if "banana" in favourite_fruits:
    print("You really like banana!")

if "grapes" in favourite_fruits:
    print("You really like grapes!")

# 5-8. Hello Admin
username = 'admin'
if username == 'admin':
    print("Hello {}, would you like to see a status report?".format(username))
else:
    print("Hello {}, Thank you for logging in again")

# 5-9. No User
username = ["Krina", "Neel", "Deep", "Parth", "Nirjari"]
for i in username:
    if i == "Admin":
        print("Hello", i, ", would you like to see a satus report?")
    else:
        print("Hello", i, ", Thank you for logging in again.")
username.clear()
if len(username) == 0:
    print("We need to find some users!")


# 5.10 - Checking username
current_users = ["Krina", "Neel", "Deep", "Parth", "Nirjari", "Admin"]
lower_current_users = [i.lower() for i in current_users]
new_users = ["Krina", "Neel", "Deep", "Parth", "Nirjari", "Admin"]
for i in new_users:
    if i.lower() in lower_current_users:
        print("Person will need to enter a new username.")
    else:
        print("Username exists.")

# 5.11 - Ordinal Numbers
list_of_numbers = list(range(1,10))

for i in list_of_numbers:
    if i == 1:
        print(str(i) + "st")
    elif i == 2:
        print(str(i) + "nd")
    elif i == 3:
        print(str(i) + "rd")
    else:
        print(str(i) + "th")


