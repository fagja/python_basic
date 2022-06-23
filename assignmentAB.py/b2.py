"""
$ python kuku_2.py
行数を入力してください: 4
列数を入力してください: 6
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
"""

N = int(input("行数を入力してください: "))
S = int(input("列数を入力してください: "))

for n in range(1, N + 1):
    for s in range(1, S + 1):
        print(n * s, end=" ")
    print()
