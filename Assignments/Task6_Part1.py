import random

random_number = random.randint(1, 100)
print(random_number)
guess = int(input("Guess the number: "))

no_of_tries = 1
while guess != random_number:
    if guess > random_number:
        print("Too high, try again!")
        no_of_tries += 1
    elif guess < random_number:
        print("Too low, try again!")
        no_of_tries += 1
    guess = int(input("Guess the number again: "))


print("You guessed it right!")
print("Number of tried = ", no_of_tries)