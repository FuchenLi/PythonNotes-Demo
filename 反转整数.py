string = input('输入一个整数: ')

strList = list(string)
resList: list = list('')

for i in range(len(string) - 1, -1, -1):
    resList.append(strList[i])

resStr = ''.join(resList)

print("输出 {}".format(resStr))
