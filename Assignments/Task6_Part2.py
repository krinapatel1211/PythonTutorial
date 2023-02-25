

n = int(input("Enter the value of N :"))
no_of_terms = n
sum1 = 1
for i in range(2, n+1):
    if (i % 2) == 0:
        isEven = True
    else:
        isEven = False
    if isEven:
        sum1 = sum1 - (1/i)
    else:
        sum1 = sum1 + (1/i)
    n = n - 1


print("Sum of {} terms: {}".format(no_of_terms, sum1))
