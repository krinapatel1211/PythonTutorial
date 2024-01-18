import datetime
from datetime import date


def CalculateAge(year, month, day):
    currentDate = datetime.datetime.now()
    age = currentDate.year - year - ((currentDate.month, currentDate.day) < (month, day))
    return age


def CalculateDifferenceLeft(birthdayNext):
    dateNow = datetime.datetime.now()
    currentDate = datetime.date(dateNow.year, dateNow.month, dateNow.day)
    delta = birthdayNext - currentDate
    print(delta)


# birthYear = int(input("Enter Birthday Year: "))
# birthMonth = int(input("Enter Birthday Month: "))
# birthDay = int(input("Enter Birthday Date: "))
birthYear, birthMonth, birthDay = 1995, 11, 12
birthDate = date(birthYear, birthMonth, birthDay)
print(birthDate)

age = CalculateAge(birthYear, birthMonth, birthDay)
print("Age = ", age)

birthdayNext = datetime.date(2023, 11, 12)
CalculateDifferenceLeft(birthdayNext)



