if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    matrix = []
    matrix1 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sublist = [i, j, k]
                matrix1.append(sublist)
                print(matrix1)
                if sum(sublist) <= n:
                    matrix.append(sublist)
    print(matrix)
