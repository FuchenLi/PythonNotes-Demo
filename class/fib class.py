class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a >10000:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        if isinstance(item,int):
            # 索引
            a = 0
            b = 1
            for i in range(0, item + 1):
                a, b = b, a + b
            return a

        if isinstance(item, slice):
            # 切片
            start = item.start
            stop = item.stop
            step = item.step

            if start == None:
                start = 0
            i = 1
            a, b = 0, 1
            while a <= 10000:
                a, b = b, a + b
                i += 1
            if stop == None:
                stop = i + 1
            if step == None:
                step = 1

            if not((step > 0 and stop >= start)or(step<0 and stop <= start)):
                start = 0
                stop = i+1

            fib = []
            a,b = 0,1
            for j in range(start, stop):
                a,b = b,a+b
                if a > 10000:
                    break
                if j % step == 0:
                    fib.append(a)
            return  fib


f = Fib()
for i in f:
    print(i)
print('sss')
print(f[1:34])