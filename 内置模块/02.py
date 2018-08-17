import hashlib
#md5加密
mima=hashlib.md5()
mima.update('ying0229._'.encode('gbk'))
print(mima.hexdigest())

#sha1加密
mima2=hashlib.sha1()
mima2.update('ying0229._'.encode('gbk'))
print(mima2.hexdigest())

