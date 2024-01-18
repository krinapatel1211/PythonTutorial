
n = int(input("Enter the value of N: "))
list1 = [5,3,3,4,4,3,4]
list1.sort()
count = 1
number_dict = {}
for i in range(0, len(list1)):
    number_dict[list1[i]] = count
    if i < len(list1)-1:
        if list1[i] == list1[i+1]:
            count += 1
        else:
            number_dict[list1[i]] = count
            count = 1
print(number_dict)

for k, v in number_dict.items():
    if v != n:
        print("Single numbers that doesn't occur {} times are: {}".format(n, k))
