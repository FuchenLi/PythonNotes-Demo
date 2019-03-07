def rounding(number):
    ten = number % 100
    number = number // 100 * 100

    if ten >= 50:
        number += 100
    print('四舍五入后: ', number)


if __name__ == '__main__':
    num = int(input('输入一个四位以上整数: '))

    rounding(num)
