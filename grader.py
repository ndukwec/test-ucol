from closedtest import *

# her we implement a Grader class to grade our student by running tests from our closedtest


class Grader(object):
    # student score
    score = 1


def check_unit_test_and_set_grade():
    student_grade = Grader()
    # Here we check what if the student passed the test but running our test and grading the student
    result_from_unittest = unittest.TextTestRunner().run(ClosedTest('test_closed_test')).wasSuccessful()
    if result_from_unittest:
        student_grade.score = 0
        print("Student passed test")
        return 0
    print("Student failed the test")
    return 1


def main():
    if check_unit_test_and_set_grade() == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()

