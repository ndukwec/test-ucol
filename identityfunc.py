# Identity function
def id_func(*args):
    return args


def main():
    # line below calls id_func declared above main, calling that should return a tuple
    print(id_func(5))


if __name__ == '__main__':
    main()
