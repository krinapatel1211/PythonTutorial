if __name__ == '__main__':
    N = int(input())
    command_list = []
    list1 = []
    for i in range(N):
        command_list.append(input().split())
    for cmd in command_list:
        if cmd[0] == 'insert':
            list1.insert(cmd[1], cmd[2])
        elif cmd[0] == 'print':
            print(list1)
        elif cmd[0] == 'remove':
            list1.remove(cmd[1])
        elif cmd[0] == 'append':
            list1.append(cmd[1])
        elif cmd[0] == 'sort':
            list1.sort()
        elif cmd[0] == 'pop':
            list1.pop()
        elif cmd[0] == 'reverse':
            list1.reverse()






    print(command_list)
