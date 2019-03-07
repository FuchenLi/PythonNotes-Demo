edge = input('输入平行四边形\n边: ')
height = input('高: ')

edge = int(edge)
height = int(height)

for i in range(0, height):
    for j in range(height - 1 - i, 0, -1):
        print('  ', end='')

    for q in range(0, edge + height - 1):
        print('* ', end='')
    print('')
