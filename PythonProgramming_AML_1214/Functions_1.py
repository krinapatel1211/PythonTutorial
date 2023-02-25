
grade = "A+"


def helloworld():
    print("Hello World! without variable")


def addition():
    a, b = input("Enter 2 numbers to add:").split()
    a, b = int(a), int(b)
    print("Result: ", a+b)


def addition_parameterised(a, b, c, d):
    print("Result (a+b+c+d): ", a+b+c+d)


def addition_with_return(a, b, c, d):
    result = a+b+c+d
    return result


def my_grade():
    grade = "B+"
    print("My Grade: ",  grade)


helloworld()

# addition()
# a1, b1, c1, d1 = input("Enter 4 numbers to add: ").split()
# a1, b1, c1, d1 = int(a1), int(b1), int(c1), int(d1)
#
# addition_parameterised(a1, b1, c1, d1)
#
# print("Result = ", addition_with_return(a1, b1, c1, d1))

my_grade()
print(grade)
