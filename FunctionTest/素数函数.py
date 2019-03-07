from typing import List


def checkPrime(min, max):
    j = 0
    returnVal: List[int] = list()
    for num in range(min, max + 1):
        for j in range(2, num + 1):
            if num % j == 0:
                break
        if j == num:
            returnVal.append(num)
    return returnVal


if __name__ == '__main__':
    minN = int(input('输入最小值 '))
    maxN = int(input('输入最大值 '))
    print(checkPrime(minN, maxN))
