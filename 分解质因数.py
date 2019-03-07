num = input('输入一个正整数: ')
num = int(num)

num_list: list = []
temp_num = num

i = 0
min = 2
while 1:
    for i in range(min, temp_num+1):
        if temp_num % i == 0:
            num_list.append(i)
            break
    if i != temp_num:
        temp_num = temp_num//i
        if temp_num % min != 0:
            min += 1
    else:
        break

print('{} ='.format(num), end='')
for index in range(0, num_list.__len__()):
    print(' {} '.format(num_list[index]), end='')
    if index + 1 != num_list.__len__():
        print('X', end='')


