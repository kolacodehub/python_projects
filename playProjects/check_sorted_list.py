def check_if_list_is_sorted(list):
    sort_list = sorted(list)
    if list == sort_list:
        return True
    return False


def main():
    question = input('Enter a list to check if sorted: ').split()
    num_list = list(map(int, question))

    result = check_if_list_is_sorted(num_list)
    if result:
        print('The list is sorted')
    else:
        print('The list is not sorted')



if __name__ == '__main__':
    main()