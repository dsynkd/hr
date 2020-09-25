def sockMerchant(n, ar):
    p = 0
    m = dict()
    for i in range(0, n):
        if ar[i] in m:
            p += 1
            m.pop(ar[i])
        else:
            m[ar[i]] = True
    return p
