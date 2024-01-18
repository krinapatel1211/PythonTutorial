
# Program 2

import datetime

# Get the user's birthday as input

birthday = input("Enter your birthday (YYYY-MM-DD): ")



# Convert the input to a date object

birthdate = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()



# Calculate the user's age

today = datetime.date.today()

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))



# Calculate the time until the next birthday

next_birthday = datetime.date(today.year, birthdate.month, birthdate.day)

if next_birthday < today:

    next_birthday = datetime.date(today.year + 1, birthdate.month, birthdate.day)

time_until_birthday = next_birthday - today



# Print the age and time until the next birthday

print("You are", age, "years old.")

print("Your next birthday is in", time_until_birthday.days, "days,",

      time_until_birthday.seconds//3600, "hours,",

      (time_until_birthday.seconds//60) % 60, "minutes, and",

      time_until_birthday.seconds % 60, "seconds.")
