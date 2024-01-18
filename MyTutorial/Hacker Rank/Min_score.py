if __name__ == '__main__':
    li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name, score])
    scr = [x[1] for x in li]
    min_li = sorted(set(scr))
    stud = []
    for y in li:
        if y[1] == min_li[1]:
            stud.append(y[0])
    for i in sorted(stud):
        print(i)

