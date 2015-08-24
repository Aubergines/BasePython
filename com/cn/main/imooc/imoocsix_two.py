# coding=utf-8
__author__ = 'Main'

#  自定义的__str__和__repr__    其中str适当使用print的时候使用，而repr则是调试的时候使用的

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '<Student: %s,%s,%s>' % (self.name, self.gender, self.score)

s = Student('Bob', 'male', 88)
print s
