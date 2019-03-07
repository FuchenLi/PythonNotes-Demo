user = 'admin'
password = '123'
# 预留初始用户
count = 3
#可输入密码次数
while 1:
    option = input('''
    ================================
    =       欢迎进入身份认证系统
    =       1.登录
    =       2.退出
    =       3.认证
    =       4.修改密码
    ================================\n''')

    option = int(option)

    if option == 1:
        getUser = input("用户名")
        getPsw = input("密码")
        if getUser != user:
            print('错误的用户名')
            continue

        if getPsw != password:
            count -= 1
            print("错误的密码,还有{}次机会".format(count))
            if count == 0:
                print("连续输错三次，程序中止")
                exit(1)
            else:
                continue

        print('登录成功')
        break
    elif option == 2:
        exit(0)
    elif option == 3:
        # TODO
        continue
    elif option == 4:
        # TODO
        continue
