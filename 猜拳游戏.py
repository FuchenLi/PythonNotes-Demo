import random

while 1:
    player = input('''
    -------------------
    │出拳吧 :
    │   0.剪刀
    │   1.石头
    │   2.布           
    │   3.退出         
    -------------------
       ''')
    if player == '':
        continue
    player = int(player)
    if player < 0 or player > 3:
        print("输错了 重来")
        continue
    if player == 3:
        exit(0)
    pc = random.randint(0, 2)
    if pc == 0:
        print('我出了剪刀')
        if player == 0:
            print("我们平局")
        elif player == 1:
            print("你赢了")
        elif player == 2:
            print("我赢了")
    elif pc == 1:
        print('我出了石头')
        if player == 0:
            print("我赢了")
        elif player == 1:
            print("我们平局")
        elif player == 2:
            print("你赢了")
    elif pc == 2:
        print('我出了布')
        if player == 0:
            print("你赢了")
        elif player == 1:
            print("我赢了")
        elif player == 2:
            print("我们平局")

