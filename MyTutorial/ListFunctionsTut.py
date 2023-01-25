"""
List Functions
To solve this problem :
1. Make a list that contains the values 5, 2, 9, 1 named my_list
2. Make a list using range with values 0, 1, 2, 3, 4
3. Output the following using the list functions
    Length : 4
    1st Index : 5
    1st 3 Values : [5, 2, 9]
    9 in List : True
    Index for 2 : 1
    How Many 2s : 1
4. Remove the value 1 from my_list
5. Remove the first index in my_list
6. Insert 10 in the first index
7. Print the sorted list and then the reversed list like this
    Sorted : [2, 9, 10]
    Sorted : [10, 9, 2]
"""

my_list = [5, 2, 9, 1]

rand_list = list(range(0, 5))

print("Length : ", len(my_list))
print("1st Index :", my_list[0])
First_3 = my_list[0:3]
print("1st 3 Values: [{}, {}, {}]".format(str(First_3[0]), str(First_3[1]), str(First_3[2])))
print("9 in list: ", 9 in my_list)
print("Index for 2: ", my_list.index(2))
print("How many 2s: ", my_list.count(2))
my_list.remove(1)
my_list.pop(1)
my_list.insert(1, 10)

print("Sorted: ")
for i in my_list:
    print(i, end=",")