def add_digits(number):
    num_list = list(number)
    add_num = sum([int(i) for i in num_list])

    return add_num

num_to_add = input('Enter the number to sum up: ')
result = add_digits(num_to_add)
print(result)

