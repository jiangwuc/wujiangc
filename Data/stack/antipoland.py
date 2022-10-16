"""
逆波兰表达式
"""

import sstack


date = "1 2 3 + 6 - p"
parents = ["+","-","p"]
def antipoland(date):
    i,date_len = 0,len(date)
    while True:
        while i < date_len and ord(date[i]) != 32:
            yield date[i]
            i += 1
        if i>= date_len:
            print("conut end")
            break
        elif ord(date[i]) == 32:
            i += 1
            continue
def sum(target):
    i = 0
    for item in target:
        i += int(item)
    return i

def subtract(target):
    i = 0
    for item in target:
        i -= int(item)
    return i

# for pr,i in antipoland(date):
#     print(pr,i)

st = sstack.SStack()
for pr in antipoland(date):
    if pr not in parents:
        st.push(pr)
    elif pr == "+":
        list = []
        n = 0
        while n < 2:
            n += 1
            list.append(st.pop())
        print(sum(list))
        st.push(sum(list))
    elif pr == "-":
        list = []
        n = 0
        while n < 2:
            n += 1
            list.insert(0,st.pop())
        print(subtract(list))
        st.push(subtract(list))
    else:
        print("结束")










