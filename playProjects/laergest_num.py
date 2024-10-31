def check_largest_number(number):
    large_num = max(number)
    return large_num


def main():
    number = input('Enter number: ').split()
    # num_list = [int(i) for i in number] or
    num_list = list(map(int, number))
    result = check_largest_number(num_list)
    print(f'The largest number is: {result}')


if __name__ == '__main__':
    main()
