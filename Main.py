from Teacher import Teacher

teacher_name_list=['王老師','朱老師','陳老師']
teacher_list=[]
for i in range(len(teacher_name_list)):
    teacher = Teacher(teacher_name_list[i])
    teacher_list.append(teacher)
print(teacher_list)

print('====================')
for i in range(len(teacher_name_list)):
    print(str(i),':',teacher_name_list[i])
print('====================')

print('[Message End]')

#teacher1 = Teacher('王老師')
#teacher2 = Teacher('朱老師')


#teacher = Teacher()
#teacher.getName()