

# 二进制文件写操作
#以二进制文件打开
fd = open("test.txt",'wb')
#已wb方式打开的，写入的必须是字节串
fd.write(b"Hello,world")