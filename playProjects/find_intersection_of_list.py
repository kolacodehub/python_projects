def find_intersection(num1, num2):
    # intersection_list = list(set(num1) & set(num2)) or
    intersection_list = set(num1).intersection(set(num2))
    return intersection_list

def main():
    user_input1 = input('Enter first list of numbers: ').split()
    num1_list = list(map(int, user_input1))
    user_input2 = input('Enter second list of numbers: ').split()
    num2_list = list(map(int, user_input2))

    result = find_intersection(num1_list, num2_list)
    print(f'Common elements: {result}')

if __name__ == '__main__':
    main()