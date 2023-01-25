def new_function(x, y):
    print("x + y = ", x+y)


def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    print("x =", num2 - num1)


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(max_number):
    for i in max_number:
        get_primes(i)
    list_of_primes.append(get_primes(i))


solve_eq("x + 4 = 9")

# new_function(3, 2)

