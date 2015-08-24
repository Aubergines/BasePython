__author__ = 'Main'


class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ( 'score',)

    def __init__(slef, name, gender, score):
        super(Student,slef).__init__(name, gender)
        slef.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score

