def qiuhe(a,b):
    return a+b

def qcj(a,b):
    return a*b

def jisuan(a,b):
    he=qiuhe(a,b)
    cj=qcj(a,b)
    return he,cj

x,y=jisuan(3,5)
print(x,y)