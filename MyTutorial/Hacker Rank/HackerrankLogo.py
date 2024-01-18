# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    length = int(input())
    for i in range(1, length * 2, 2):
        H_string = ''
        for j in range(i):
            H_string = H_string + 'H'
        print(H_string.center(length * 2))
    for len in range(6, length*4 + 1):
        if len > 5 and len <= 11:
            print('HHHHH'.rjust(7) + 'HHHHH'.rjust(16))
        elif len > 11 and len <= 14:
            print('HHHHHHHHHHHHHHHHHHHHHHHHH'.rjust(27))
        elif len > 14 and len <= 20:
            print('HHHHH'.rjust(7) + 'HHHHH'.rjust(16))
    for i in range(length * 2 - 1,0, -2):
        H_string = ''
        for j in range(i):
            H_string = H_string + 'H'
        print((H_string.center(length*2).rjust(length*5+1)))