while 1:
    print('输入三角形的三条边')
    a = input('a= ')
    b = input('b= ')
    c = input('c= ')

    a = int(a)
    b = int(b)
    c = int(c)

    aa = a ** 2
    bb = b ** 2
    cc = c ** 2
    if not (a + b > c) or not (a + c > b) or not (b + c > a):
        print('不是三角形')
        continue

    if a == b or a == c or b == c:
        if (a == b) and (b == c):
            print('这是个等边三角形')
            continue

        elif (aa + bb == cc) or (aa + cc == bb) or (bb + cc == aa):
            print('这是个等腰直角三角形')
            continue

        else:
            print('这是个等腰三角形')
            continue

    if (aa + bb == cc) or (aa + cc == bb) or (bb + cc == aa):
        print("这是个直角三角形")
        continue
