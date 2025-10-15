class Course :
    _id_counter =1 


    def __init__(self,name):
        self.course_id = Course._id_counter
        Course._id_counter += 1

        
        self.name = name
        
        #self.student_id = student._id_counter
        #self.grades = {}
        self.enrolled_students = []

    def __str__(self):
        return  f"course id :{self.course_id},name :{self.name},enrolled: {len(self.enrolled_students)}"  
    def enroll_student (self,student) : 
     if student not in self.enrolled_students:
        self.enrolled_students.append(student)
        print("student enrolled")
     else: 
        print("student alredy enrolled")  
    def remove_student(self, student) :
       for course in self.Courses.values() :
          if student in course.enrolled_students:
             course.enrolled_students.remove(student)   