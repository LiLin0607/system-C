from Teacher import Teacher
from Student import Student
from Lesson import Lesson
from Course_Day_Time import Time

teacher = Teacher('王老師', '123456', '123456@gmail.com')
student = Student('林同學', '人工智慧應用工程系', '四技日間部', '四慧二甲')
lesson = Lesson('系統架構', '4106', '選修', '人工智慧系')
time = Time('星期三', '2', '4')

teacher.getTeacher()
student.getStudent()
lesson.getCourse()
time.getTime()