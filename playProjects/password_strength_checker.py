def check_password_strength(password):
    contains_lowercase = any((char.islower()) for char in password)
    contains_uppercase = any((char.isupper()) for char in password)
    contains_digits = any((char.isdigit()) for char in password)
    contains_special_character = any((char in "!#$%&()*+,-.:;<=>?@[]^_`{|}~") for char in password)
    is_long_enough = len(password) >= 8
    missing_criteria = []

    if not is_long_enough:
        missing_criteria.append('at least 8 characters long')
    if not contains_lowercase:
        missing_criteria.append('at least one lowercase letter')
    if not contains_uppercase:
        missing_criteria.append('at least one uppercase letter')
    if not contains_digits:
        missing_criteria.append('at least one digit')
    if not contains_special_character:
        missing_criteria.append('at least one special character')

    if len(missing_criteria) == 0:
        return 'strong'
    else:
        return f'Weak. it must contain' + ','.join(missing_criteria) + '.'


password = input('Input a password: ')
result = check_password_strength(password)
print(result)
