import sys

try:
    i = int(input('输入'))
    print(i)


except:
    print('{}这不是个整数'.format(sys.exc_info()))
