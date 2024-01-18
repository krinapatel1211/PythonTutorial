s = "(){}}{"
parenthesis = {'(':')', '[':']', '{':'}'}
list_s = []
if s[0] not in parenthesis.keys():
    print('False')
else:
    list_s.append(s[0])
for i in range(1, len(s)):
    if len(list_s)>0 and s[i] == parenthesis[list_s[-1]]:
        list_s.pop()
        print(list_s)
    else:
        if s[i] in parenthesis.keys():
            list_s.append(s[i])
            print(list_s)
        else:
            print('False')
if len(list_s) > 0:
    print('False')
else:
    print("True")