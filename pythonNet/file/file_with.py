
# with语句
#生成文件对象
#语句结束之后，with生成的对象f会被自动释放掉。
with open("test.txt") as f:
    data = f.read()
    print(data)
