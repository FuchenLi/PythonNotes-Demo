class Student(object):
    __slots__ = ('name', 'set_age', 'age')


def set_age(self, age):
    self.age = age


s= Student()


from types import MethodType
s.set_age = MethodType(set_age, s)
#引入MethodType 为 s添加 方法


s.set_age(26)

print(s.age)
