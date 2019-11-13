def getdealNums(l, r):
    def isDeal(num):
        if num == 1:
            return True
        elif num % 5 == 0:
            return isDeal(num / 5)
        elif num % 3 == 0:
            return isDeal(num / 3)
        else:
            return False

    res = 0
    for i in range(l, r + 1):
        if isDeal(i):
            res += 1
            # print(i)

    return res


def getdealNums2(l, r):
    res = 0
    for i in range(21):
        for j in range(15):
            tmp = 3 ** i * 5 ** j
            if l <= tmp <= r:
                res += 1
            elif tmp >= r:
                break
    return res


l = 1
r = 20000000
print(getdealNums2(l, r))
print(getdealNums(l, r))

# print(getdealNums(1, 2000000000))
# 147
