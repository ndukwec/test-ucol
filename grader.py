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


def send_email_to_teacher(student_email):
    # here we will send the students email (who passed our test) to the teacher's email
    # teachers_email = "chinedua@umich.edu"
    # msg = EmailMessage()
    # msg.set_content("The student with the following email passed the test " + student_email)
    #
    # msg['Subject'] = 'Student Passed Our Test'
    # msg['From'] = 'chineduamadindukwe2016@gmail.com'
    # msg['To'] = teachers_email if " " else 'chinedua@umich.edu'
    #
    # s = smtplib.SMTP('smtp.gmail.com')
    # # we could pass in our specific smtp server above,
    # # i passed in gmail just as an example
    #
    # s.send_message(msg)
    # s.quit()
    print("hey teacher, student with email: " + student_email + " passed our test.")


def send_post_request_to_api(student_email):
    # Here we'll send a post request with the students email to our custom api built with flask or django.
    # we could also integrate other learning platforms api e.g canvas, moodle etc here
    print("student with email: " + student_email + " will be sent in a post request here.")


def utility_func(student_email_data):
    print(len(student_email_data))
    if len(student_email_data) > 0:
        # now we send the students email by calling our functions defined above
        for i in range(len(student_email_data)):
            send_email_to_teacher(student_email_data[i])
            send_post_request_to_api(student_email_data[i])
    else:
        print("our list is empty :-(")


def main():
    student_info = sys.argv[1:]
    # line above creates a list of strings with the student details (username and email)
    # we had to slice the list above to remove our script name which of course is the first argument at index 0
    value_returned_from_test_method = check_unit_test_and_set_grade()
    print("the outcome from function call above is " + str(value_returned_from_test_method))
    if value_returned_from_test_method == 1:
        utility_func(student_info)


if __name__ == '__main__':
    main()
