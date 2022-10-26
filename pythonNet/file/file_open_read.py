

#文件操作
try:
   # fd = open(r"F:\work\wujiangc\pythonNet\string\code.py",'r',)
    fd = open("test.py",'r',encoding='utf-8')
except FileNotFoundError as e:
    print(e)
else:
    print("open file success")
#w 会清空原有文件的内容，pycharm上执行不会清空，在linux上会清空

#开始文件读写 read
#文件过大时，循环读取
# n = 0
# while True:
#     data = fd.read(1025)
#     n += 1
#     print("读取第%d次"%n)
#     #如果读到空，表示文件已经读取完
#     if not data:
#         break
#     print(data)

#readline() 读取一行，重复执行时，接上一次的再接着读
data = fd.readline()
print("读取到的内容：",data)
data = fd.readline()
print("读取到的内容：",data)

#readlines()将读取内容作为列表返回
#每行做为列表的一个元素
#size如果超过1行，则返回2行
data = fd.readlines()
print(data)

#fd 为可迭代对象，使用for循环读取没一行
for i in fd:
    print(i)


#关闭文件
fd.close()