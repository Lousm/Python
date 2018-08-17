class Payment():
    def pay (self):
        raise NotImplementedError

class WechatPay(Payment):
    def fuqian (self,money):
        print('微信支付%s元'%money)

def pay(p,money):
    p.pay(p,money)

p = WechatPay()
pay(p,200)