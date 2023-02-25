import random


def perform_binary_search(l1, target):
    minimum = 0
    guesss = 0
    maximum = len(l1) - 1
    while minimum < maximum:
        guesss = (minimum + maximum)//2
        if target < l1[guesss]:
            maximum = guesss
        elif target > l1[guesss]:
            minimum = maximum
        else:
            return guesss + 1


# generate a random list
random_list = []
for item in range(1, 8):
    value1 = random.randint(1, 1000)
    random_list.append(value1)

# prints the generated list
print(random_list)
random_list.sort()
list_sorted = random_list.copy()

# print the sorted list
print("Sorted list: ", list_sorted)

# Enter the key to search from sorted list.
key = int(input("Enter the search key: "))
isFound = perform_binary_search(list_sorted, key)

print(isFound)
if isFound:
    print("The key value - {} is present in the list".format(key))
else:
    print("The key value - {} is NOT present in the list".format(key))
