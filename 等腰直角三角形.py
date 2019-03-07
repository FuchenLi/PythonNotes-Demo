edge = input('输入三角形的底: ')
edge = int(edge)

for i in range(0, edge):
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
