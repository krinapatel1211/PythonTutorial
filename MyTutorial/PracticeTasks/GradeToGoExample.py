age = int(input("Enter Age: "))

if age < 5:
    print("Too young to go to school")
elif age == 5:
    print("Go to Kindergarten")
elif (age >5) and (age <= 17):
    print("Go to Grade {}".format(age-5))
else:
    print("Go to College")
