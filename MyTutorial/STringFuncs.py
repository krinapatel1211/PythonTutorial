sampleString = "This is an important string"
print("Lenght :", len(sampleString)) # Length : 31
print(sampleString[0]) # T
print(sampleString[-1]) # g
print(sampleString[0:4]) # This
print(sampleString[0:4]) # This
print("Hello" * 5) # Hello Hello Hello Hello Hello

# a - z 97 - 122
# A - Z 65 - 90

upperCaseString = "KRINA"
secret_string = ""
for char in upperCaseString:
    secret_string += str(ord(char))
print("Secret Message :", secret_string)

for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    upperCaseString += chr(int(char_code))
print("The normal string : ", upperCaseString)