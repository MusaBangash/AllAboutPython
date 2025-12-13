print("Student Grading System")

def student_details():
    std_name = input("Enter your name: ")
    std_stand = int(input("Enter your standard: "))
    std_subjects = int(input("Enter your number of subjects: "))

    subject_details(std_subjects)


def subject_details(std_subjects):
    for i in range(std_subjects):
        print(f"\nSubject {i + 1}")
        sub_name = input("Enter your subject name: ")
        sub_total = int(input("Enter subject total marks: "))
        sub_obtain = int(input("Enter obtained marks: "))

        print("Stored Data")
        print("Subject:", sub_name)
        print("Total Marks:", sub_total)
        print("Obtained Marks:", sub_obtain)


student_details()
