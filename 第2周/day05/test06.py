import time
import os
t1 = "2018-07-19 15:27:30"
a = time.strptime(t1, "%Y-%m-%d %H:%M:%S")
afreezingTime = time.mktime(a)

b = time.localtime(time.time())
now = time.strftime("%Y-%m-%d %H:%M:%S", b)

sy = (7*24*60*60)-(time.time()-afreezingTime)

jd = time.time()+sy

c = time.localtime(jd)
jd1 = time.strftime("%Y-%m-%d %H:%M:%S", c)
print('冻结时间为：', t1)

print('解冻时间为：', jd1)


while True:
    b = time.localtime(time.time())
    now = time.strftime("%Y-%m-%d %H:%M:%S", b)

    sy = (7*24*60*60)-(time.time()-afreezingTime)

    jd = time.time()+sy

    c = time.localtime(jd)
    jd1 = time.strftime("%Y-%m-%d %H:%M:%S", c)
    sy1 = sy-(int(sy/24/60/60)*24*60*60)
    ts = int(sy/24/60/60)

    os.system('cls')

    m, s = divmod(sy1, 60)
    h, m = divmod(m, 60)
    print('现在的时间', now)
    print('剩余时间为：%s天 %d:%02d:%02d' % (ts, h, m, s))
    # print("%d:%02d:%02d" % (h, m, s))

    time.sleep(1)
