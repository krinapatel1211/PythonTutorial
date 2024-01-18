if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    list1 = []
    for i in arr:
        if i < max(arr):
            list1.append(i)
    print(max(list1))
