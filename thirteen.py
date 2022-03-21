import os


def rec(x, d="start"):
    if ord(d[0]) - ord("0") >= 0 and ord(d[0]) - ord("0") <= 9:
        d = "_" + d
    d = "/" + d + "/"
    i, j, k = 0, 0, 0
    for r, t, y in os.walk(x):
        i, j, k = r, t, y
        break
    for a in j:
        q = a
        if ord(a[0]) - ord("0") >= 0 and ord(a[0]) - ord("0") <= 9:
            q = "_" + q
        q = "/" + q + "/"
        print(d + "->" + q)
        rec(i + "/" + a, a)
    for a in k:
        a = "/" + a + "/"
        print(d + "->" + a)

print('Введите путь к каталогу: ')
rec(input())
