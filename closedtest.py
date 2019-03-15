import identityfunc


# our closed test (main method) here will run the id function to make sure we are getting the expected output

def main():
    score = 0
    result = identityfunc.id_func(6)

    if result == (6,):
        score += 1

    print(score)


if __name__ == '__main__':
    main()
