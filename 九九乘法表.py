print('九九乘法表')

for i in range(1, 9):
    for j in range(1, i+1):
        print('{0}X{1}={2}\t'.format(j, i, j * i), end='')
    print('')
