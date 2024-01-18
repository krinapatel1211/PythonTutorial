
list1 = [5,3,7,6,8,4,3,4,6,8,5,7]

in_List = []
not_In_List = []

for i in list1:
    check = i
    count = 0
    if in_List is not [] and check not in in_List:
        for j in list1[list1.index(check)+1:]:
            if check == j:
                count += 1
                in_List.append(check)
        if count == 0:
            not_In_List.append(check)

if len(not_In_List) != 0:
    print("Elements not repeated twice in list are:")
    for i in not_In_List:
        print(i)
else:
    print("There is NO SINGLE element in the list!")

