import os

class Teacher:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(self.name)
        
        
if __name__== "__main__":
    teacher = Teacher("朱邵威")
    teacher = Teacher("黃詰琳")
    teacher.getName()