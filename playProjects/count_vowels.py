def count_vowel(user_input):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1
    return count


def main():
    user_input = input('Enter a sentence to search No of vowels in it: ')
    result = count_vowel(user_input)
    print(f'Total no of vowels is: {result}')


if __name__ == '__main__':
    main()
