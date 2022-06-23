"""
行数を入力してください: 9
列数を入力してください: 9
"""

N = int(input("行数を入力してください: "))
S = int(input("列数を入力してください: "))

""" for n in range(1, N + 1):
    for s in range(1, S + 1):
        sn = s * n
        # print(ns, end=" ")
        if sn < 10:
            print(end=" ")
        print(s, "×", n, "=", sn , end=" | ")
    print()
 """


for n in range(1, N + 1):
    for s in range(1, S + 1):
        sn = s * n
        if sn < 10:
            print(s, "×", n, "= ", sn, end=' | ')
        else:
            print(s, "×", n, "=", sn, end=' | ')
    print()
