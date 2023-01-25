# def factorial(number):
#     if number <= 1:
#         return 1
#     else:
#         fact = number * factorial(number - 1)
#         return fact
#
#
# print(factorial(5))

# Calculate Fibonacci series
# 1, 1, 2, 3, 5, 8, 13 ...

def fibonacci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        series = fibonacci(number - 1) + fibonacci(number - 2)
        return series


number_of_fib_values = int(input("How many fibonacci values should be found: "))
i = 1
while 
print(fibonacci(number_of_fib_values))
