def answer(start, length):
    current = start
    cycle = 0
    ans = 0
    while (length > 0):
        ans ^= calcXor(current, current + (length - 1))
        current += length + cycle
        cycle += 1
        length -= 1
    return ans

def calcXor(frm, to):
    pattern = [to, 1, to ^ 1, 0] if frm % 2 == 0 else [frm, frm ^ to, frm - 1, (frm - 1) ^ to]
    return pattern[(to - frm) % 4]