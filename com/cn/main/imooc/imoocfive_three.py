# coding:utf-8
__author__ = 'Main'

# 文件的编码声明一定要放在文件的开始的地方有以下的几种方式
#       coding:utf-8
#       coding=utf-8    等号两遍不能有空格

# 判断对象的类型，这里使用的是isinstance


class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)

