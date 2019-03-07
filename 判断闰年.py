year = input('输入一个年份： ')
year = int(year)

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('这是一个闰年')

else:
    print('这是一个平年')
