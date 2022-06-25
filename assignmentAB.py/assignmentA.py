users = ["Bob", "Tom", "Ken"]
int_numbers = [1, 2, 3, 4, 5]
bob_info = ["Bob", "Dylan", 79]
members = ["Bob", "Tom", "Ken"]

# A4
"""
print(members[0])
print(members[1])
"""

# A5
"""
print("Name: " + bob_info[0] + " " + bob_info[1] + ", Age: " + str(bob_info[2]))
"""

# A6
"""
for i in range(10):
    if i % 2 == 1:
        print(i)
"""

# A7 for を使って even_numbers のそれぞれの値を2倍した値を出力してください
"""
even_numbers = [2, 4, 6, 8]

for content in range(4):
    print(even_numbers[content] * 2)
"""

# A8
"""
A8 users_info を使って次のような出力をしてください
Name: Bob, Age: 79
Name: Tom, Age: 59
Name: Ken, Age: 61
"""


users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

for order in range(3):
    print("Name: " + users_info[order][0] + ", Age: " + str(users_info[order][1]))


# A9 下記のコードが期待通り動作するような辞書を定義してください
"""
print(bob_info["first_name"]) # "Bob"
print(bob_info["family_name"]) # "Dylan"
print(bob_info["age"]) # 79
"""

"""
bob_info = {"first_name": "Bob", "family_name": "Dylan", "age": 79}  # A-9
print(bob_info["first_name"])
print(bob_info["family_name"])
print(bob_info["age"])
"""

# A10

import random

def dice():
    return random.randint(1, 6)

print(dice())
