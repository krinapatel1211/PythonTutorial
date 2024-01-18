import os
#
# This is my file
# My name is Krina Patel
# I am a student in Canada
# Line 1
# Number of words :  4
# Average word Length: 3.00
# Line 2
# Number of words :  5
# Average word Length: 3.60
# Line 3
# Number of words :  6
# Average word Length: 3.17
#

with open("myfile.txt", encoding="utf-8", mode="w") as myfile:
    myfile.write("This is my file\nMy name is Krina Patel\nI am a student in Canada")

with open("myfile.txt", encoding="utf-8") as myfile:
    print(myfile.read())

word_count = 0
with open("myfile.txt", encoding="utf-8") as myfile:
    line_number = 1
    while True:
        line = myfile.readline()
        if not line:
            break
        else:
            print("Line {}".format(line_number))
            word_list = line.split()
            print("Number of words : ", len(word_list))
            char_count = 0
            for word in word_list:
                for char in word:
                    char_count += 1
                    avg_num_chars = char_count/len(word_list)
            print("Average word Length: {:.2f}".format(avg_num_chars))
            line_number += 1
