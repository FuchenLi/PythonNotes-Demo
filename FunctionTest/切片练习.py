
def trim(string: str):


    ldone = False
    rdone = False
    while not(ldone and rdone):
        # 判定条件 左右 都 done
        lindex = 0
        rindex = len(string)

        # 左find 非 0 则 左 find done
        if string.find(' ') == 0:
            lindex = 1
        else:
            ldone = True

        # 右find 非 0 则 右 find done
        if string.rfind(' ') == len(string) -1:
            rindex = len(string) -2
        else:
            rdone = True

        string = string[lindex:rindex]
    return string


if __name__ == '__main__':
    print(trim(' s  sdada      '))




