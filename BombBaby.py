import math

def answer(M, F):
    m = long(M)
    f = long(F)
    counter = 0
    while (True):
        if (m <= 0 or f <= 0 or (m == f)):
            break
        if m > 64 or f > 64:
            if (m > f):
                multiplier = getMultiplier(m, f)
                m -= f * multiplier
                counter += multiplier
            else:
                multiplier = getMultiplier(f, m)
                f -= m * multiplier
                counter += multiplier
        else:
            if m > f:
                m -= f
            else:
                f -= m
            counter += 1
    if (m == 1 and f == 1):
        return counter
    else:
        return "impossible"

def getMultiplier(x, y):
    dif = long(x) - long(y)
    mul = (dif / long(y)) + long(1)
    return mul