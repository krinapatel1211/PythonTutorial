list2 = [1,1,1,2,2,2,3,3]
list2.sort()
count = 1
number_counts = {}
for i in range(len(list2)):
    number_counts[list2[i]] = count
    if i < len(list2)-1:
        if list2[i] == list2[i+1]:
            count += 1
        else:
            number_counts[list2[i]] = count
            count = 1
print(number_counts)
for k,v in number_counts.items():
    if v == 1:
        print("Single elements in the list = ", k)
