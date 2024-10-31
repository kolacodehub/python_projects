def num_is_perfect_square(num):
    perfect_square = num ** 0.5
    if perfect_square.is_integer():
        return f'{num} is a perfect square'
    return f'{num} is not a perfect square'

def main():
    user_input = int(input('Enter a number: '))
    result = num_is_perfect_square(user_input)
    print(result)


if __name__ == '__main__':
    main()