# 汉诺塔问题  从 A -> C
count: int = 0


def hanoi(n, A, B, C):
    if n == 1:
        global count
        count += 1
        # 递归到 只处理 一个 的 问题  直接从 A 放到 C 上
        print('{}->{}  '.format(A, C))

    else:
        # 将 n-1 个 圆盘 从A移到B上 以 C中转
        hanoi(n - 1, A, C, B)
        # 将剩下的最后一个 从 A 移到 C上
        print('{}->{}  '.format(A, C))
        count += 1
        # 将 B 上的 圆盘 从 B 移到 C 上  以A中转
        hanoi(n - 1, B, A, C)
    return count


if __name__ == '__main__':
    hanoi(int(input('输入初始圆盘数 ')), 'A', 'B', 'C')
    print('\n共{}步'.format(count))
