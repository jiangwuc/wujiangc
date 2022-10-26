

#二进制文件读取操作
fd = open('test.txt','rb')
#得到的是一个字节串
data = fd.read()
print(data)
print(data.decode())
fd.close()
#打开图片，只能用二进制方式打开
fd = open("111.jpg","rb")
date = fd.read()
print(date)
fd.close()