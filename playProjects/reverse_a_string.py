def reverse_string(str):
    reverse_string = str[::-1]
    return reverse_string


string_to_reverse = input('Enter a string you want to reverse: ')
result = reverse_string(string_to_reverse)
print(result)

