dateStr = input('输入日期 (格式：xxxx/xx/xx)')

date = dateStr.split('/')

# 预留 每个月 天数
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 算闰年
year = int(date[0])
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days[1] = 29

count = 0
for i in range(0, int(date[1])-1):
    count += days[i]

count += int(date[2])

print('这是{0}年的第{1}天'.format(date[0], count))
