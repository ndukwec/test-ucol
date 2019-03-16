from closedtest import *


def check_unit_test_and_set_grade():
    student_score = 0
    # below will check again to make sure we pass our test
    result_from_unittest = unittest.TextTestRunner().run(ClosedTest('test_closed_test')).wasSuccessful()
    if result_from_unittest:
        student_score = 1
        # we could make a post request here with the students info to grade the student
        print("Student passed test")
    else:
        print("Student failed test")
    return student_score


def main():
    check_unit_test_and_set_grade()


if __name__ == '__main__':
    main()

