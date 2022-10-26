"""
缓冲区
"""
#系统不支持无缓冲
# fd = open("test.txt",'w',0)
#行缓冲：遇到换行符，就会写入
# fd = open("test.txt",'w',1)

#指明缓冲区大小，关闭程序或者程序停止时，会写入（不识别）
#不写，默认缓冲区大小
fd = open("test.txt",'w',12)
n = 0
while n < 3 :
    s = input(">>")
    n += 1
    fd.write(s + '\n')
    #立即刷新缓冲区，将内容写入磁盘
    fd.flush()
fd.close()




