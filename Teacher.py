import os

class Teacher:
    def __init__(self, name):
        self.name = name
        self._email = None
        
        @property
        def email(self):
            return self._email
            
        @email.setter
        def email(self, value):
            #最簡 email 格式: 中間要有@
            if re.match(r"^[^@]+@[^@]+$", value):
                self._email = value
            else:
                raise ValueError(F"無效的 EMAIL 格式: {value}")
                
if __name__== "__main__":
    name = input("請輸入老師姓名：")
    teacher = Teacher(name)
   
    while True:
        email_input = input("請輸入老師email(中間需包含 @):")
        try:
            teacher.email = email_inputbreak
        except ValueError as e:
            print("錯誤:", e)
            
    print(f"{teacher.name}的email是:{teacher.email}")
    
    #def getName(self):
        #print(self.name)
        
        
