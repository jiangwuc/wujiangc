
import time
fd = open("test.txt",'r+')
m = 1
for i in fd:
    m += 1

while True:
    s = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
    m +=1
    fd.write("%d. "%m)
    fd.write(s+'\n')
    time.sleep(1)

fd.close()