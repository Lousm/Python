class Alipay():
    def pay(self,money):
        print('支付宝支付%d元'%money)

class Applepay():
    def pay (self,money):
        print('apple pay支付%d元'%money)#pay方法是该类留的接口

def pay(payment,money):#支付函数，总体负责支付,对应支付的对象和要支付的金额
    payment.pay(money) #根据支付对象，选择调用相应的接口

p=Alipay()
pay(p,200)