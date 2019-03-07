

def get_soulution():
    print('ax^2 + bx + c =0 求解两个根')
    a: float = float(input('输入a: '))
    b: float = float(input('输入b: '))
    c: float = float(input('输入c: '))
    x0: float = 0
    x1: float = 0
    dilta = b ** 2 - 4 * a * c

    if a == 0:
        if b == 0:
            print('b不应为0')
            get_soulution()
        else:
            x = -c / b
            print('x值为{}'.format(x))
            return
    else:
        if dilta > 0:
            x0 = (-b + dilta ** 0.5) / (2 * a)
            x1 = (-b - dilta ** 0.5) / (2 * a)
            print('方程有两实根 {0} , {1}'.format(x0, x1))
            return
        else:
            if dilta == 0:
                x0 = (-b + dilta ** 0.5) / (2 * a)
                print('方程有一实根 {}'.format(x0))
                return
            else:
                print('方程无实根')
                return


if __name__ == '__main__':
    get_soulution()



