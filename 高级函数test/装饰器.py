import time
import functools


def log(text):
    def get(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('{}--{}-at{}'.format(text, func.__name__, time.ctime()))
            print('end call')
            return func(*args, **kw)

        return wrapper

    return get

# 需求 @superlog 与 @superlog('sometex')  都能使用
# 这是使用 try 检测 len(funortext)==0 是否报 TypeError 异常 判断是否有字符串函数
def superlog(funortext):
    try:
        len(funortext) == 0
        def decotext_call(func):
            def wrapper(*args, **kw):
                print('{}--function__name__ is {}'.format(funortext, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decotext_call
    except:
        def wrapper(*args, **kw):
            print('{} is excuted'.format(funortext.__name__))
            return funortext(*args, **kw)

        return wrapper

# 第二种想法  使用 type 检测参数类型
def elog(funortext):
    if type(funortext) == type(''):
        def decotext_call(func):
            def wrapper(*args, **kw):
                print('{}--function__name__ is {}'.format(funortext, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decotext_call
    else:
        def wrapper(*args, **kw):
            print('{} is excuted'.format(funortext.__name__))
            return funortext(*args, **kw)

        return wrapper

@log('begin call')
def fun(x):
    return x * x


@superlog('super_log')
def funct(x):
    return x * 10


@elog('e_log')
def ff(x):
    print(x)


f = fun(2)

s = funct(5)

k = ff('')