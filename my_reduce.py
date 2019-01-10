def my_reduce(function, iterate):
    if len(iterate) == 2:
        result = sum(iterate)
    else:
        new_iterate = iterate[2:]
        new_iterate.insert(0, function(iterate[0], iterate[1]))
        result = my_reduce(function, new_iterate)

    return result


def main():
    my_iterate = [47, 11, 42, 13]
    print(my_reduce(lambda x, y: x + y, my_iterate))


if __name__ == '__main__':
    main()
