n = int(input("Enter number of elements in AP: "))
list1 = []

for i in range(n):
    list1.append(int(input("Enter the elements of list:")))

diff = list1[1] - list1[0]
for i in range(1,len(list1)-1):
    if (list1[i+1] - list1[i]) != diff:
        break
else:
    print("The sequence is an AP")

