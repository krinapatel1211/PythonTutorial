def is_it_odd(number):
    if (number % 2) == 0:
        return False
    else:
        return True


def change_list(odd_number, new_list):
    if is_it_odd(odd_number):
        new_list.append(odd_number)
    return new_list


def main():
    list1 = list(range(1, 20))
    new_list1 = []
    for i in list1:
        change_list(i, new_list1)
    print(new_list1)


main()

