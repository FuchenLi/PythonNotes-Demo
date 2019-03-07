class Student(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1




lisa =  Student('lisa')
print(lisa.count)
bart = Student('bart')
print(bart.count)