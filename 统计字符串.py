string = input("输入一个字符串: ")

count = {}

for s in string:
    count[s] = string.count(s)

for key, value in count.items():
    print(key, end=':')
    print('{}次'.format(value))
