color = ['♠', '♥', '♣', '♦']
number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', '王']
allCard = set()

# 生成0-53的数
for i in range(0, 54):
    # 以字符串 保存 进 set  保证 pop时 随机
    allCard.add(str(i))

player1 = set()
player2 = set()
player3 = set()
# 随机 pop 发牌 不接受重复
for i in range(0, 18):
    player1.add(int(allCard.pop()))
    player2.add(int(allCard.pop()))
    player3.add(int(allCard.pop()))
# 转 list
player = [sorted(list(player1)) , sorted(list(player2)), sorted(list(player3))]
p = list()
p = [list(), list(), list()]

for j in range(0, 3):
    print('\n\nplayer{}: '.format(j + 1), end='')
    for i in range(0, 18):
        # 打印 手牌   同时 将 0-53 的数字 转为 0-13 的数
        print('│', number[player[j][i] // 4], color[player[j][i] % 4], end='│ ')
        p[j].append(number[player[j][i] // 4])
print('')

# i 为temp下标 到18归零， temp 保存 0-13数 的玩家手牌 p:list i到18 则 更换 下一玩家list
# countTime 是一个 数据字典  用来 保存 手牌与张数的 键值对
i = -1
index: int = 0
temp = list(p[index])
countTime = {}
while True:
    i += 1
    if i == 18:
        # 判断是否 到达 18 是 则打印countTime奇数 同时temp 引用下一玩家  list 玩家全部遍历完 则 break while
        print('玩家', index + 1, '统计: ', end='')
        for key, val in countTime.items():
            # 只打印 2 3 4 张的情况
            if val >= 2:
                print('[{1}张{0}]'.format(key, val), end='')
                if val ==4:
                    print('-!!炸弹 ', end='')
                elif key == '王':
                    print('-!!王炸 ', end='')
                else:
                    print(' ', end='')
        print('')
        countTime.clear()

        index += 1
        i = 0
        if index == 3:
            break

        temp = list(p[index])
    # 键值对 方式 保存 玩家 手牌 各 数字 张数
    countTime[temp[i]] = temp.count(temp[i])
