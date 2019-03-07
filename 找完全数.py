numList = []
print('10000以内完全数如下: ')
for num in range(2, 10001):
    inList = []
    for i in range(1, num):
        if num % i == 0:
            inList.append(i)

    count = 0
    for l in inList:
        count += l

    if count == num:
        numList.append(num)

for l in numList:
    print(l)

