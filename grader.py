from closedtest import *
import sys  # we import sys module to read the command line arguments
# import smtplib  # sending emails
# from email.message import EmailMessage


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


def send_post_request_and_email_to_teacher(student_email_data):
    # teachers_email = "chinedua@umich.edu"
    # msg = EmailMessage()
    print(len(student_email_data))
    if len(student_email_data) > 0:
        print("sending student data to teacher! or to rest service")
        # now we send the data
        for i in range(len(student_email_data)):
            print("student with email: " + student_email_data[i] + " passed our test, now grade the student!")
    else:
        print("our list is empty :-(")

    # msg['Subject'] = 'The following students passed our test'
    # msg['From'] = 'chineduamadindukwe2016@gmail.com'
    # msg['To'] = teachers_email if " " else 'chinedua@umich.edu'  # Teachers email passed in from our function
    # # call in mail, ternary operator to sure we don't have an empty string

    # s = smtplib.SMTP('smtp.gmail.com')  # we could pass in our specific smtp server here,
    # i passed in gmail as an example

    # s.send_message(msg)
    # s.quit()


def main():
    student_info = sys.argv[1:]
    # line above creates a list of strings with the student details (username and email)
    # we had to slice the list above to remove our script name which of course is the first argument at index 0
    value_returned_from_test_method = check_unit_test_and_set_grade()
    print("the outcome from function call above is " + str(value_returned_from_test_method))
    if value_returned_from_test_method == 1:
        send_post_request_and_email_to_teacher(student_info)


if __name__ == '__main__':
    main()
