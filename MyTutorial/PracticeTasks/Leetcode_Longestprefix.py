
def is_valid_parenthesis(s):
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if not stack:
                return False
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return not stack


str1 = "(){}[]]"
isValid = is_valid_parenthesis(str1)
print(isValid)
