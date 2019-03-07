num = input('输入一个整数: ')

num = int(num)

if num == 1:
    print('{}既不是素数也不是合数'.format(num))
else:
    i = 0
    for i in range(2, int(num ** 0.5) + 2):
        if num % i == 0:
            break

    if i == int(num ** 0.5) + 1:
        print('{}是一个素数'.format(num))
    else:
        print('{}是一个合数'.format(num))
