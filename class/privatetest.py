class Test:
    @property
    def Age(self):
        return self.__age

    def __init__(self, name='noname', age=0):
        self.__name = name
        self.__age = age
    @Age.setter
    def Age(self, age=0):
        self.__age = age

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, name='notname'):
        self.__name = name

    def __str__(self):
        print('')
        return 'name: ' + self.__name + '\nage: ' + str(self.__age)

    __repr__ = __str__

    def __len__(self):
        return len(self.__name)

    def __del__(self):
        print('{}释放'.format(self.__name))

    def __call__(self, *args):
        print('{}被调用 获得{}'.format(self.__name, args))

    def __setitem__(self, key, value):
        if key == 0:
            self.Age =value
        elif key == 1:
            self.Name = value
        else:
            print('no change')

    def __getitem__(self, item):
        if item == 0:
            return self.__age
        elif item == 1:
            return self.__name
        else:
            return '无值'

    def __getattr__(self, item):
        if item == 'age':
            return self.__age


if __name__ == '__main__':
    p1 = Test('大小', 25)
    print(p1)
    print(len(p1))
    p1.Age = 26
    print(p1)
    p1.__getattr__('age')
    p1.Name = '小小'
    print(p1)
    print(len(p1))
    p1(666, 444, 555)

    p1[0] = '2'
    print(p1)

    print(p1[7])

    del p1

