import random

unsorted_list = []
for i in range(1, 8):
    value = random.randint(1, 100)
    unsorted_list.append(value)

print(unsorted_list)
unsorted_list.sort()
print("Sorted List : ", unsorted_list)

key = int(input("Enter the number to search from 1 to 100: "))

beg = 0
mid = 0
end = len(unsorted_list) - 1

while beg < end:
    mid = (beg + end)//2
    if key == unsorted_list[mid]:
        print("Found")
        break
    elif key > unsorted_list[mid]:
        beg = mid + 1
        # continue
    elif key < unsorted_list[mid]:
        end = mid - 1
        # continue
    else:
        print("not Found")
        break






