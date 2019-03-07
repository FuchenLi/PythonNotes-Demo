
diagonal = input('输入对角线长度（奇数）')

diagonal = int(diagonal)

if diagonal % 2 == 0:
    print('对角线长度不为奇数')
    exit(0)

for i in range(0, (diagonal + 1)//2):
    for j in range(0, (diagonal + 1)//2 - 1 - i):
        print('  ', end='')
    for p in range(0, 2*i + 1):
        print('* ', end='')
    print('')

for a in range((diagonal + 1)//2 - 2, -1, -1):
    for b in range(0, (diagonal+1)//2 - a - 1):
        print('  ', end='')
    for c in range(0, 2*a + 1):
        print('* ', end='')
    print('')



