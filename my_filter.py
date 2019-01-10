def my_filter(function, iterator):
    result = [item for item in iterator if function(item)]

    return result


def main():
    my_list = [1, 5, 3, 7, 8, 3, 10, 4, 0]
    print("Input list: {0}".format(my_list))
    # Function examples for demo purpose
    print("\nlambda x: x % 2 == 0")
    print(my_filter(lambda x: x % 2 == 0, my_list))

    print("\nlambda x: x % 2 != 0")
    print(my_filter(lambda x: x % 2 != 0, my_list))

    print("\nlambda x: x != 4")
    print(my_filter(lambda x: x != 4, my_list))


if __name__ == '__main__':
    main()
