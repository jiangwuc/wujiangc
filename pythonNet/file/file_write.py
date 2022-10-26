
# fd = open("test.py",'w')
#a 追加
fd = open("test.txt",'w')
#会覆盖原来的内容
fd.write("'hello,world'")
fd.write("'hello'\n ")
#writelines()将列表写入文件中
fd.writelines(["1,2,3,4"])
#关闭文件
fd.close()