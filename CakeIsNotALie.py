def answer(s):
        for i in range(1, len(s)):
            if (len(s) % i == 0):
                st = ""
                for j in range(0, int(len(s) / i)):
                    for k in range(0, i):
                        st += s[k]
                    if (st == s):
                        return int(len(s) / i)
        return 1