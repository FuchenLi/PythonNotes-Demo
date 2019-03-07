# while 1:
#     numStr = input('输入一个4位以上的整数: ')
#     numArr = list(numStr)
#     result: str
#     if int(numStr) < 1000:
#         print('整数过小')
#         continue
#     else:
#         # 判断 十位 是否 大于 5
#         if int(numArr[len(numArr) - 2]) >= 5:
#             numArr[len(numArr) - 1] = '0'
#             numArr[len(numArr) - 2] = '0'
#             numArr[len(numArr) - 3] = str(int(numArr[len(numArr) - 3]) + 1)
#             # 判断 进位后 百位 是否产生 进位
#             if numArr[len(numArr) - 3] == '10':
#                 # 百位 产生进位  循环 判断 更高一位 是否向上产生 进位
#                 for x in range(len(numArr) - 3, -1, -1):
#                     if numArr[x] != '10':
#                         break
#                     else:
#                         numArr[x] = '0'
#                         if x - 1 == -1:
#                             # 最高位产生进位 重新 生成 表示该数的 list
#                             num: list = ['1']
#                             for i in range(1, len(numArr)):
#                                 num.append('0')
#                             result = ''.join(num)
#                             break
#                         else:
#                             numArr[x - 1] = str(int(numArr[x - 1]) + 1)
#                             result = ''.join(numArr)
#             else:
#                 result = ''.join(numArr)
#         else:
#             numArr[len(numArr) - 1] = '0'
#             numArr[len(numArr) - 2] = '0'
#             result = ''.join(numArr)
#         print('四舍五入后: {}'.format(result))
#         break


num = int(input('输入一个四位以上整数: '))

ten = num % 100
num = num // 100 * 100

if ten >= 50:
    num += 100
print('四舍五入后: ', num)
