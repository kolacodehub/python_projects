def remove_duplicates(number):
    duplicate_remove = set(number)
    return list(duplicate_remove)
def main():
    user_input = input('Enter a number to remove duplicates: ').split()
    numbers = list(map(int, user_input))
    result = remove_duplicates(numbers)
    print(result)


if __name__ == '__main__':
    main()