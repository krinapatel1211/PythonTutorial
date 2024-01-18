# This program compares two strings.
# Get a password from the user.
password = ""

# Determine whether the correct password
# was entered.
while password != 'prospero':
    password = input("Enter the password: ")
    if password == 'prospero':
        print("Password Matched!")
    else:
        print("Passwords DOES NOT match!")
