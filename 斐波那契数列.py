f0 = 1
f1 = 1
temp0 = f0
temp1 = f1
temp = 0
fList = [f0]

for i in range(0, 28):
    temp = temp0 + temp1
    fList.append(temp)
    temp1 = temp0
    temp0 = temp
print('[1]1')
for l in fList:
    print('[{0}]{1}'.format(fList.index(l) + 2, l))
print('')
