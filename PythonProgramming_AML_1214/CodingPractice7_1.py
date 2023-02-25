# Strings
# 1)	Write a Python function that takes a string and calculates the length of a string and returns it.
# Print the returned value.
import string


def calculate_length(str):
    return len(str)


string1 = "Krina"
print("Length of string : ", calculate_length(string1))


# 2)	Write a Python function that takes a string and counts the number of characters (character frequency) in a string.
# For example, if we send 'google.com' to the function, it should return a dictionary like this
# {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def calculate_chars(str):
    dict = {}
    for i in str:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    print(dict)


string2 = "google.com"
calculate_chars(string2)

# 3)	Create a string of your choice and apply a minimum of 8 of  following methods to it and print the result.
string3 = "Krina"
string4 = "Patel"
print("string.split() function: ", string3.split(", "))
print(string3.capitalize())
print(string3.casefold())
print(string3.count("a"))
print(string3.isdecimal())
print(string3.isdigit())
print(string3.islower())
print(string3.isupper())
print(string3.replace("a", "A"))
print(string.capwords(string3))

# 4)	Write a Python function that converts temperatures from Fahrenheit to Celsius.
def convert_to_celcius(temperature):
    temp_celsius = ((temperature - 32) / 1.8)
    print("{} degree Celsius = {} degree Fahrenheit.".format(temp_celsius, temperature))


convert_to_celcius(95)
