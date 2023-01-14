num1, operator, num2 = input("Enter Calculation: ").split()
num1 = int(num1)
num2 = int(num2)

if operator=="+":
    ans = num1+num2
    print("{} {} {} = {}".format(num1,operator,num2,ans))
elif operator=="-":
    ans = num1-num2
    print("{} {} {} = {}".format(num1,operator,num2,ans))
elif operator=="*":
    ans = num1*num2
    print("{} {} {} = {}".format(num1,operator,num2,ans))
elif operator=="/":
    ans = num1/num2
    print("{} {} {} = {}".format(num1,operator,num2,ans))
