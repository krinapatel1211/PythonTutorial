
s = "a"
count = 0
temp_str = []
longest_substr = []
list2 = []
if len(s) >= 2:
    for i in range(len(s)):
        if s[i] not in temp_str:
            temp_str.append(s[i])
        for j in s[i+1:]:
            if j not in temp_str:
                temp_str.append(j)
                longest_substr.append(len(temp_str))
            elif j in temp_str:
                list2.append("".join(temp_str))
                temp_str=[]
                break
    print(max(longest_substr))
else:
    print(len(s))


# print(sorted(list2, key=lambda x:len(x),reverse=True)[0])

