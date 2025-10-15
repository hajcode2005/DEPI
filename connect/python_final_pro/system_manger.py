from DEPI.connect.C_DATA_base.course import Course
from DEPI.connect.Projects.python_final_pro.student import Student

class systemManeger:

    def __init__(self):
        self.students = {}

        self.courses ={}

    def add_student(self,name) :
        student = Student(name)  
        self.students[student.student_id] = student
        print("student add")
        return student.student_id
    def remove_student(self,student_id):
        if student_id in self.students:
            student = self.students[student_id]
            if not student.enrolled_courses :
                del self.students[student_id]
                print("student remove")
            else:
                print("student alredy enrolled") 
        else:
            print("invailled student")   
    def enroll_course(self, student_id,course_id) :
        if student_id in self.students and course_id in self.courses :
            student = self.students[student_id]
            course = self.courses[course_id]
            if course.name not in student.enrolled_courses :
                student.enroll_in_course(course.name)
                course.enroll_student(student.name)
                print("student enrolled in course")
            else:
                print("student is alredy enrolled")   
        else:
            print("invalid student id") 
    def  recored_grade(self,student_id,course_id,grade)  :
        if student_id in self.students and course_id  in self.courses :
            student =self.students[student_id]  
            course =   self.courses[course_id]   
            student.add_grade(course.name,grade)  
            print("grade recorded")   
        else:
            print("invalid student grade")   
    def get_all_students(self)  :
        return list(self.students.values) 
    def   get_all_courses(self)  :
        return list(self.courses.values)     
           

