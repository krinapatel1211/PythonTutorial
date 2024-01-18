# a,b,c,d,e,f = [int(i) for i in input("Enter a,b,c:").split()]

# list1 = [500, 200, 209, 300, 30, 50]
# max = 0
# for i in list1:
#     if i > max:
#         max = i
#
# print(max)
# -----------------------------------------------------
# a = ["Windows", "Linux", "Kernel"]
# b = ["Windows", "Linux", "Kernel"]
#
# c = a
# d = c
# e = b[:2]
#
# print(a, b, c, d, e)
# print(a is b)
# print(b is a)
# print(a is c)
# print(a is not c)
# print(a is d)
# print(e is b)

# ------------------------------------------------------

a = 0
b = -4

max = a if a > b and a != 0 else b

print(max)