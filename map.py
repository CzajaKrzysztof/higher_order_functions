def my_map(function, *args):
    result = []
    print(args)
    print(list(zip(args)))
    if len(args) == 1:
        for i in args[0]:
            result.append(function(i))
    else:
        list_of_args = list(zip(args))
        # for i in list_of_args:
        #     result.append(function(i[0], i[1]))

    return result


def main():
    input_list_one = [2, 5, 6, 1, 9, 6, 3]
    input_list_two = [5, 2, 5, 6, 7, 1, 5]
    print(my_map(lambda x, y: x + y, input_list_one, input_list_two))


if __name__ == '__main__':
    main()
