
list1 = [1,2,3,4,5,6,7,8]

sequence = list1[0]
count = 0
for i in list1[1:]:
    sequence += 1
    if sequence != i:
        print(f"{sequence} is missing!")
        sequence += 1
        count += 1
if count == 0:
    print("No missing number found!!")
