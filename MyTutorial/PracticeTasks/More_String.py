'''rand_string ="       Krina             krina    "

# rand_string = rand_string.lstrip()
# rand_string = rand_string.rstrip()
rand_string = rand_string.strip()
print(rand_string)

rand_string1 = "My name is Krina Patel"
print("Capitalise = ", rand_string1.capitalize())
print("Upper Case = ", rand_string1.upper())
print("Lower Case = ", rand_string1.lower())

fruit_list = ["mango", "apple", "banana"]
print(" ".join(fruit_list))
print(", ".join(fruit_list))

# print all list items from a sentence
fruit_list2 = rand_string1.split()
for i in fruit_list2:
    print(i)

# find a specific substring or string in sentence
print("How many 'my' = ", rand_string1.count("a"))
print("Where is = ", rand_string1.find("a"))
print("Replace it is = ", rand_string1.replace("a", "K"))

# Create an Acronym ==> Random Access Memory = RAM
full_form = input("Enter Full Forms = ")
list1 = full_form.split()
for i in list1:
    print(i[0].upper(), end="")
'''

# Decrypt a message
message = "Krina Krina"  # input("Enter the input message = ")
key = int(input("Enter key to shift = "))
listOfWords = message.split()

messageEncryption = ""
for word in listOfWords:
    for char in word:
        messageEncryption = messageEncryption + str(ord(char) + key)
print("Encrypted Message = ", messageEncryption)

messageEncryption 

