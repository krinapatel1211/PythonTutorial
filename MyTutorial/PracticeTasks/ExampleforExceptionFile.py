with open("mydata2.txt", encoding="utf-8", mode="w") as mydata2:
    mydata2.write("This is my file 2")

try:
    my_datafile = open("mydata3.txt", "r")

except FileNotFoundError as ex:
    print("This file does not exist!")
    print(ex.args)

else:
    print(my_datafile.read())
    my_datafile.close()

finally:
    print("File closed")



