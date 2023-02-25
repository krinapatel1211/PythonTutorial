class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dog_name = input("What is your dog name: ")
    if any(char.isdigit() for char in dog_name):
        raise DogNameError
except DogNameError:
    print("Your dog's name can't contain a number")
