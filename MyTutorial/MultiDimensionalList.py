multiD_list = [[0] * 10 for i in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        multiD_list[i][j] = "{}".format(i*j)


for i in range(1, 10):
    for j in range(1, 10):
        print(multiD_list[i][j], end=", ")
    print()