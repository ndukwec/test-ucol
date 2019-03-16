from closedtest import *
import sys  # we import sys module to read the command line arguments


def check_unit_test_and_set_grade():
    student_score = 0
    # code below will check again to make sure the student passed our test
    result_from_unittest = unittest.TextTestRunner().run(ClosedTest('test_closed_test')).wasSuccessful()
    if result_from_unittest:
        student_score = 1
        print("Student passed test")
    else:
        print("Student failed test")
    return student_score


def send_post_request_and_email_to_teacher(student_data):
    # this function will take the student_data list and send a post request and an email to the teacher,
    # we can implement another simple rest api with django or flask that'll receive the request and auto update the
    # students score on a website we build or integrate that with any learning platforms i.e moodle, canvas etc.
    print(len(student_data))
    if len(student_data) > 0:
        print("sending student data to teacher! or to rest service")
        # now we send the data
        for i in range(len(student_data)):
            print("student details are: " + student_data[i])
    else:
        print("our list is empty :-(")


def main():
    student_info = sys.argv[1:]
    # line above creates a list of strings with the student details (username and email)
    # we had to slice the list above to remove our script name which of course is the first argument at index 0
    value_returned_from_test_method_above = check_unit_test_and_set_grade()
    print("the outcome from function call above is " + str(value_returned_from_test_method_above))
    if value_returned_from_test_method_above == 1:
        send_post_request_and_email_to_teacher(student_info)


if __name__ == '__main__':
    main()

