import Models
import re
class StudentDAO:
    def __init__(self):
        self.studentList = []
        with open('students.csv', mode='r') as fo:
            for line in fo:
                s_name, email, s_password = line.strip().split(',')
                student = Models.Student(s_name, email, s_password)
                self.studentList.append(student)

        # This returns the data as a List
    def get_students(self):
        return self.studentList

#This method takes a Student’s email as a String searches the List of Students for a Student with that email and returns a Student Object.
    def get_student_by_email(self, email):
        for student1 in self.studentList:
            if (student1.get_email() == email):
                return student1

#This method takes an email and a password from the user input. Return whether or not a Student with the given information is found.
    def validate_user(self, email, pw):
        for student in self.studentList:
            if(email == student.get_email() and pw == student.get_password()):
                return True
        return False

#At the time of registering this method check if student email is already registered
    def is_student(self,email):
        for student in self.studentList:
            if student.get_email() != email:
                return True

#This method register a new student
    def register_student(self, name, email, pw):
        if self.is_student(email) == True:
                self.studentList.append(Models.Student(name, email, pw))
        self.save_student()

#This method converts the new student object into string and write it into the student.csv file
    def save_student(self):
        with open('students.csv', mode='w', encoding='utf8') as file:
            for student in self.studentList:
                file.write(f"{student.get_name()},{student.get_email()},{student.get_password()}\n")

class CourseDAO:
    def __init__(self):
        self.courseList = []
        with open('courses.csv', mode='r', encoding='utf8') as co:
            for line in co:
                self.c_id, self.c_name, self.instructor = line.strip().split(',')
                course = Models.Course(self.c_id, self.c_name, self.instructor)
                self.courseList.append(course)

#This method takes no parameters and returns every Course in the system.
    def get_courses(self):
        return self.courseList

class AttendingDAO:
    def __init__(self):
        self.attendList = []
        with open('attending.csv', mode='r', encoding='utf8') as attend:
            for line in attend:
                self.course_id, self.student_email = line.strip().split(',')
                attendance = Models.Attending(self.course_id, self.student_email)
                self.attendList.append(attendance)

#This method reads the Attending.csv file and returns the data as a List
    def get_attending(self):
        return self.attendList

    # This method takes a student's email and course Id and a Course_list
    #Checks if the student with email is currently attending a Course with that ID.
    def register_student_to_course(self, email, course_id, course_list):
            li = []
            course_register_status = False
            for course in course_list:
                if (course_id == course.get_id()):
                    course_register_status=True

            for attending in self.attendList:
                if (attending.get_student_email() == email and attending.get_course_id() == course_id):
                    print("Already registered in the course")
                    course_register_status = False

            if (course_register_status == True):
                self.attendList.append(Models.Attending(course_id, email))
                self.save_attending()
                return True

#This method takes a Student’s Email and a Course List as parameters and searches the Attending List for all the courses a student is registered to.
    def get_student_courses(self, course_list, email):
        l1 = []
        for course in course_list:
            for attList in self.attendList:
                if (attList.get_student_email() == email and attList.get_course_id() == course.get_id()):
                    l1.append(course)
        return l1

#This method overwrites the original Attending.csv file with the new data
    def save_attending(self):
        with open('attending.csv', mode='w', encoding='utf8') as file:
            for attending in self.attendList:
                file.write(f"{attending.get_course_id()},{attending.get_student_email()}\n")