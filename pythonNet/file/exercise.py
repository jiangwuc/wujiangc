#先读取文件，
try:
    fd = open("F:\笔记.docx", 'rb')
except FileNotFoundError as e:
    print(e)
else:
    #创建新的文件，并将原文件的内容复制到新的文件里
    fdw = open("biji.docx", 'wb')
    while True:
        data = fd.read()
        if not data:
            break
        fdw.write(data)

    with open("biji.docx",'rb') as f:
        print(f.read())
    fd.close()
    fdw.close()