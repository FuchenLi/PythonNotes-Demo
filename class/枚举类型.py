from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender, type(Gender.Male)):
            self.gender = gender
        else:
            raise Exception('TypeError:gender类型错误')


bart = Student('张三', Gender.Male)

print(bart.gender)