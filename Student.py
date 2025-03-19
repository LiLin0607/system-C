import os

class Student:
    def __init__(self,name,department,schoolsystem,classs):
        self.name = name
        self.department = department
        self.schoolsystem = schoolsystem
        self.classs = classs
        
    def getName(self):
        print(self.name)
        print(self.department)
        print(self.schoolsystem)
        print(self.classs)
        
if __name__ == "__main__":
    Student = Student("你老公","戀愛系","碩士班","五戀一甲")
    Student.getName()
    