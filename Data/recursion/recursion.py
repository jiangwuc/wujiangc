
"""
阶乘函数
"""

def recursion(n):
    if n <= 1:
        return 1
    return (n * recursion(n - 1))

r = recursion(5)
print(r)
