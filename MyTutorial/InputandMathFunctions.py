#input functions
name = input("What is your name : ")
print("Hello", name)

num_1, num_2 = input("Enter 2 Numbers: ").split()
num_1 = int(num_1)
num_2 = int(num_2)
sum_1 = num_1+num_2
difference_1 = num_1-num_2
Multiply = num_1 * num_2
Divide =  num_1 / num_2
remainder =  num_1 % num_2

print("{} + {} = {}".format(num_1,num_2,sum_1))
print("{} + {} = {}".format(num_1,num_2,difference_1))
print("{} + {} = {}".format(num_1,num_2,Multiply))
print("{} + {} = {}".format(num_1,num_2,Divide))
print("{} + {} = {}".format(num_1,num_2,remainder))