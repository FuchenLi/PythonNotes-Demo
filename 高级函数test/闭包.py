def createCounter():
    global i
    i = 0

    def counter():
        global i
        i += 1
        return i

    return counter

# 初始化时 已经 return 了 counter函数的闭包
# 后续 调用时  直接相当于调用 counter()
counterA = createCounter()
print(counterA(), counterA(), counterA())
# 再次 初始化  从 createCounter 函数体 从前往后 运行
counterB = createCounter()
print(counterB(), counterB(), counterB())
