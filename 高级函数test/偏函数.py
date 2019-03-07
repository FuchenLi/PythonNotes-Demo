import functools


def func(h, i, j):
    print(h, i, j)


func2 = functools.partial(func, j=9)

func2(1, 2)
