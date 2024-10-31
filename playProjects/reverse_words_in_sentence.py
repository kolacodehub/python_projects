def reverse_words_in_sentence(sentence):
    # reversed = sentence[::-1]
    reversed_sentence = ' '.join(reversed(sentence))
    return reversed_sentence


def main():
    user_input = input('Enter a sentence to reverse the words in it: ').split()

    result = reverse_words_in_sentence(user_input)
    print(result)


if __name__ == '__main__':
    main()