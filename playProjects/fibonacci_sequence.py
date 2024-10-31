def fibonnacci_sequence(num):
    fib_sequence = [0, 1]

    for i in range(2, num):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    return fib_sequence[:number]

number = int(input('Enter a number: '))
result = fibonnacci_sequence(number)

for term in result:
    print(term)