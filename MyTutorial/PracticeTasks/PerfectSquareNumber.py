
num = int(input("Enter a number to check for perfect square :"))
print(num)

i = 1
while True:
    if i*i == num or num == 0:
        print(f"{num}  is a perfect square")
        break
    elif i*i > num:
        print(f"{num}  is NOT a perfect square")
        break
    else:
        i += 1

