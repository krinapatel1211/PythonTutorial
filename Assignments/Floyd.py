row = int(input("Enter number of rows-"))
digit = 1
for i in range(1,row*2+1):
    if i <= row:
        for j in range(i):
            print(digit, end=" ")
            digit = digit + 1
    elif i >= row:
        for k in range(row, i-row-1, -1):
            print(digit, end=" ")
            digit = digit + 1
    print()