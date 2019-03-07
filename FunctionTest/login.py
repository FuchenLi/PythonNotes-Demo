user = 'admin'
psw = '123'


def login_tips():
    option = int(input('''
        ================================
        =       欢迎进入身份认证系统
        =       1.登录
        =       2.退出
        =       3.认证
        =       4.修改密码
        ================================\n'''))
    if option == 1:
        login_handle()
    elif option == 2:
        exit(0)
    elif option == 3:
        print('认证模式 按0返回')
        if int(input()) == 0:
            login_tips()
    elif option == 4:
        print('认证模式 按0返回')
        if int(input()) == 0:
            login_tips()
    else:
        print('错误')
        login_tips()


def login_handle(times=3):
    get_user = input('输入用户名： ')
    get_psw  = input('输入密  码： ')
    if get_user == user:
        if get_psw == psw:
            print('登录成功')
            return
        else:
            while times > 0:
                if input('重新输入密码') == psw:
                    print('登录成功')
                else:
                    print('登录失败 ', end='')
                    times -= 1
            else:
                print('登录次数用光 程序关闭')
                exit(0)


    else:
        print('用户名错误')
        login_handle()


if __name__ == '__main__':
    login_tips()