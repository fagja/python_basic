"""  B1
下記のような出力が得られる kuku_1.py を実装してください。

1 2 3 4 5 6 7 8 9
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
"""


""" for before_asterisk in range(1, 10):
    for after_asterisk in range(1, 10):
        print(before_asterisk * after_asterisk)
"""


""" for n in range(1, 10):
    for s in range(1, 10):
        print(n * s, end="")
    print() """

"""
for after_asterisk in range(1, 10):
    argument1 = 1 * after_asterisk
    argument2 = 2 * after_asterisk
    argument3 = 3 * after_asterisk
    argument4 = 4 * after_asterisk
    argument5 = 5 * after_asterisk
    argument6 = 6 * after_asterisk
    argument7 = 7 * after_asterisk
    argument8 = 8 * after_asterisk
    argument9 = 9 * after_asterisk

    print(
        argument1,
        argument2,
        argument3,
        argument4,
        argument5,
        argument6,
        argument7,
        argument8,
        argument9,
    )
"""
for n in range(1, 10):
    for s in range(1, 10):
        print(n * s, end=" ")
    print()
