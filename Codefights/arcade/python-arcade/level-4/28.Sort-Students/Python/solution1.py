# Python3

# 有限制修改區域
def sortStudents(students):
    students.sort(key= lambda x: x.split()[-1])
    return students
