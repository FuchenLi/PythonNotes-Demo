from functools import reduce


def strUpFirst(string: str):
    return string.capitalize()


def multi(a, b):
    return a * b


def prod(L: list):
    return reduce(multi, L)


def char2num(c):
    digital = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digital[c]


def integerPart(x, y):
    return x * 10 + y


def decimalPart(x, y):
    return x * 0.1 + y


def str2float(s: str):
    integer = s.split('.')[0]
    decimal = s.split('.')[1]

    # 首先添 0
    decimal = '0' + decimal
    print('de', decimal)
    # 切片方式 逆序
    reverseDecimal = decimal[::-1]
    print('re', reverseDecimal)

    inte = float(reduce(integerPart, map(char2num, integer)))
    deci = float(reduce(decimalPart, map(char2num, reverseDecimal)))

    return inte + deci


if __name__ == '__main__':
    a = list(map(strUpFirst, ['daf', 'dada', 'eqer']))
    print(a)

    print('3*5*7*9 = ', prod([3, 5, 7, 9]))

    print('str2float(\'123.456\') = ', str2float('123.456'), '  type(str2float(\'123.456\')) = ',
          type(str2float('123.456')))
