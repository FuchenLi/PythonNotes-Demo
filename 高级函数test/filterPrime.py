# 素数
# 算法 1.取2，删除后续2的倍数
#     2.取 3 ， 删除 后续 3 的倍数
#      3.取5， 删除后续5的 倍数
# …………………………………………

def odd_iter():
    # 3开始的奇数 生成器
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisiable(n):
    return lambda x: x % n > 0


def prime():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)

        yield n

        it = filter(not_divisiable(n), it)


ite = prime()
for i in range(0, 100):
    print(next(ite))
