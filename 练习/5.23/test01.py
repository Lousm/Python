import os
# 查看目录列表（列出目录下所有的文件和目录） 
# 显示出是文件还是目录
def isWjMl():
    mllb=os.listdir(os.getcwd())
    print('当前工作目录',os.getcwd())
    print('当前工作目录列表',mllb)
    # for i in mllb:
    #     if os.path.isfile(i):
    #         print("%s是文件"%i)
    #     else:
    #         print("%s是目录"%i)
# isWjMl()

#创建目录
# os.mkdir('测试目录')

# 删除文件或目录
# 需要检查文件或目录是否存在
#   可以删除文件也可以删除目录
def dell(s):#传入目录或文件
    if os.path.exists(s):
        if os.path.isfile(s):
            os.remove(s)
            print('删除成功')
        else:
            os.rmdir(s)
            print('删除成功')
    else:
        raise Exception('‘%s’ 不存在'%s)

# dell('测试目录')

# 4、重命名文件或目录
#     需要检查文件或目录是否存在
def renname(s):#传入目录或文件
    if os.path.exists(s):
        newname=input('请输入新的文件名：')
        os.rename(s,newname)
        print('将"%s"重命名为"%s",成功！'%(s,newname))
    else:
        raise Exception('‘%s’ 不存在'%s)
# renname('测试目录')

# 为文件添加前缀
#   为当前目录下的所有文件，添加文件名前缀，前缀需要用户输入
def qz(s):#传入目录
    mllb=os.listdir(s)#得到文件夹下的所有文件
    abspath=os.path.abspath(s)#得到绝对路径
    qz=input('请输入文件前缀（目录下的所有文件）：')
    for i in mllb:
        os.rename((abspath+'\\'+i),(qz+i))
    print('将"%s"目录下的文件添加前缀"%s",成功！'%(s,qz))

# qz('测试目录')

# 删除文件前缀
#       删除当前目录下所有文件名的前缀，前缀需要用户输入
def scqz(s):#传入目录
    mllb=os.listdir(s)#得到文件夹下的所有文件
    abspath=os.path.abspath(s)#得到绝对路径
    qz=input('请输入要去掉的文件前缀（目录下的所有文件）：')
    for i in mllb:
        try:
            if i.index(qz)==0:#首次出现的位置是0
                newname=i[len(qz):]
                os.rename((abspath+'\\'+i),newname)
                print('将"%s"目录下的文件%s去掉前缀"%s",成功！'%(s,i,qz))    
        except :
            print('这个文件（文件夹）没有指定的前缀')
        
scqz('测试目录')
# 切换目录 
# 切换目录后，显示目录下所有文件和目录
