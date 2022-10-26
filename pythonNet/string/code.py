
s1 = "Hello,world"
s2 = "你好"
#字符串 ---> 字节串
print("Str:",s1)
print("Str:",s2.encode()) #--重点函数
#一个字节 8位，
#一个汉字占3个字节。
#Str: b'\xe4\xbd\xa0\xe5\xa5\xbd'

# s3 =
#字节串转换成字符串  --重点函数
s3 = bytes.decode(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print("Str:",s3)
#字节串
print("Bytes:",b"Hello,world")
#通过字节串的转换函数转成字节串
#int 1: b'\x01\x02\x03\x04'
print("int 1:",bytes([1,2,3,4]))