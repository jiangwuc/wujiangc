"""
文件偏移量
"""

fd = open("test.txt",'r+')
print("当前文件偏移量位置：",fd.tell())
print(fd.read(2))
print("当前文件偏移量位置：",fd.tell())
print(fd.read(2))
#人为调整文件的偏移。
fd.seek(5,0)
print(fd.read(2))

fd.close()

import os
#判断文件大小
s = os.path.getsize('111.jpg')
print(s)
#判断文件夹
s = os.listdir('..')
print(s)
#判断文件是否存在
s = os.path.exists("test.txt")
print(s)
# 5.  判断文件类型 普通文件True，文件夹：False
s = os.path.isfile("test.txt")
print(s)
# 5.  删除文件
s = os.remove("test.txt")

