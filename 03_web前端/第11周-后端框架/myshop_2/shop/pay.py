
from shop import models

from django.http import HttpResponse
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse


def dopay(request):

    """
    设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
    """
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '2016092100565196'
    alipay_client_config.app_private_key = 'MIIEowIBAAKCAQEAuNAWigCAmgy8Xl7z2EBKN5FEt/EAnNRmeN5jTK3K0BfNBJuZa7mXTqF/AmZXdXX1ScCgWf55rJy9+Khh1xSobkeCqnD41kvYT8+zINiqsrE6+FtWqmzQigNJw3CK4zL6wJImqQGNA4O+THmaaDicDrXW0Pil4pkrKTOaDLeLscm+4MYHDEklfdTRuu0OJ/toXlL5fLLhInxG0qG23e32siMFlc9nVgui48pqxnHY76LkZ/QfkNQ+NKrY+fvrP1sgLlkHDfJ7/ZeEvzW5N5BSxXAV3rDfH4gRknZVuVslngzKGkutFRl9MZxDjfEdk2t6E36VC0/ZTUE0n12OeKi+QQIDAQABAoIBAFUvlTQHBz/6ntjg64TCHXN/gi1G6QFg5drQpvSxJsrELbvx/MWqxhN4XRK+GZIKzQUxxLe2lF774JS9CFwbKYerbo8hg5FDZHFlSyvYstWq24OellP31CfJXDa5qUsQNISO2UMNc/Iqx4x4gLOJZGVja6Dm+493Cm3zWw6Bi+JmUo0szLmaSLJKfCZpPIpgZlzZRqWyR3JLYtg1p0d83C7ii8LrNxW3CHLv59jAbnzYTDc30mhjEszqXF4lzzXvtzsGtn7GlGErH6Ip6/LGhIEphWd4ddmXNiXi6r9Adzl8rglNRTSwcGU4uHg+zizeduyATWtQBIOIpXD2rNAHIAECgYEA6Z0+uT+tgeD2zpiznJVAZlmRgxInKyGshOGhsNP0cEhHbdJSNhjm5gkvOl6sgxJ+CYB/VHrByfQSY5hEQknx53GFMhg8KwdzLiSJDcpY4FkSqEGMjOCk6d92QcphoJYfvZ9jtjbzo7VTzRoTGPsp1ZvyA1T8JtoRbfKgxd2i2K0CgYEAyoW0GfLJLc+wDzGi6QALaIzk9VcUjHkPCTuj0xSEEfmY7SQbnbSd+T53tTadrkswKws390mvyHSv+RswxGJv48PlT31UhtynlfMAE1GrlrJ7vtNlsy1rsx0XzSKtIDNrFjEu5GkVQ5tkahr99qpRnD0MFA3xH00b50VyxMCMimUCgYAmH6Inywt+oX7FckgFapnq2f0UHbdEo6cqvEONvtkqJbF6a5M8/s1XhvItHVwbu73TwSOGXs4XLfx+QlAJXVXbxjvNVAUlpH6Ybh/rnzTnz8Fqsd/E8bgX7n6299b8xOMDJ+q2xrr14VZ+px2suvg1wtA42PqZQIcNoUW5ZJT5tQKBgBFMhmvI/0I4gVNq6/13EYJmto/2Vj0BgjVJsN6w2+8lINjwwqMf8HZ/zX3fImzm40Bp/ufSlX9L6FQg7HN57RDJhObbT8MNSgtW7GS6DywaJtPP/tnlQVPVYlkVYzBi8/y7SsQb7cMOnO8rSxIszjfIRyXXYwdHcOC6X+lKgTa5AoGBANyTwWLqyCS5plpPHm+x+JyEsiIc37fwhZh5BOXEVQkjsgE1cNummv9be/+bAyyPuXrFfLMMpYOH2Ye7oJAD7OEL92mEpAgkb6c9gRWbkm6vrK+Fp3p5bx+/4KArwN/89s4oQEO/7dwIsioAuYlxC8mCjAf1Fh8UvoGPLvpMfFX5'
    alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA97wRQhe632w+Z8PUTJFatjpZQhXuiduZ7PoO5LtE/JpGpdk2Z/g4AiSV+/cwzQhlCnF/br4i0M8el4Y6MMCsG/YZABj5O4R40mOmecUKiFg8LyGEAZWvX3qFwOeL4HFoiNleO2A2jidtys2Y8odeginnIqQ+8leTFIKkwe1uWAL0N+SJwNz9zwYRwiywVmq8HYtOxZzXX89s4GxlaqpGTzbsyX6FEFxdf4vvOYbNtJZ0sSPCs3345R25wDsvHinZ6tACtwMROTjxgLz43HUQJSiWtKaR+yKBn+kbhN0awoPlxDo58onbhDhz3oSHUCLb6uSSWX+ba/BX+Kwdr/OY/wIDAQAB'

    """
    得到客户端对象。
    注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
    logger参数用于打印日志，不传则不打印，建议传递。
    """
    client = DefaultAlipayClient(alipay_client_config=alipay_client_config)

    """
    页面接口示例：alipay.trade.page.pay
    """

    user_id = request.session.get('user_id')
    order_from = models.Order_form.objects.filter(user_id_id=user_id, pay_status=0).first()

    id=order_from.id

    # 订单号
    danhao = order_from.code_num
    #总价
    zongjia = order_from.money

    cart=models.Shopping_cart.objects.filter(checked=1)
    name=''
    for i in cart:

        comm=models.Commodity.objects.filter(id=i.commodity_id_id).first()
        name = name + comm.name+', '

    print(name)


    # 对照接口文档，构造请求对象
    model = AlipayTradePagePayModel()
    model.out_trade_no = danhao
    model.total_amount = float(zongjia)
    model.subject = name
    model.body = "支付宝测试"
    model.product_code = "FAST_INSTANT_TRADE_PAY"

    request = AlipayTradePagePayRequest(biz_model=model)
    request.return_url='http://10.10.91.184:8000/shop/return_url/'
    # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
    response = client.page_execute(request, http_method="POST")
    print("alipay.trade.page.pay response:" + response)

    return HttpResponse(response)

def dopay_1(request):
    """
       设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
       """
    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    alipay_client_config.app_id = '2016092100565196'
    alipay_client_config.app_private_key = 'MIIEowIBAAKCAQEAuNAWigCAmgy8Xl7z2EBKN5FEt/EAnNRmeN5jTK3K0BfNBJuZa7mXTqF/AmZXdXX1ScCgWf55rJy9+Khh1xSobkeCqnD41kvYT8+zINiqsrE6+FtWqmzQigNJw3CK4zL6wJImqQGNA4O+THmaaDicDrXW0Pil4pkrKTOaDLeLscm+4MYHDEklfdTRuu0OJ/toXlL5fLLhInxG0qG23e32siMFlc9nVgui48pqxnHY76LkZ/QfkNQ+NKrY+fvrP1sgLlkHDfJ7/ZeEvzW5N5BSxXAV3rDfH4gRknZVuVslngzKGkutFRl9MZxDjfEdk2t6E36VC0/ZTUE0n12OeKi+QQIDAQABAoIBAFUvlTQHBz/6ntjg64TCHXN/gi1G6QFg5drQpvSxJsrELbvx/MWqxhN4XRK+GZIKzQUxxLe2lF774JS9CFwbKYerbo8hg5FDZHFlSyvYstWq24OellP31CfJXDa5qUsQNISO2UMNc/Iqx4x4gLOJZGVja6Dm+493Cm3zWw6Bi+JmUo0szLmaSLJKfCZpPIpgZlzZRqWyR3JLYtg1p0d83C7ii8LrNxW3CHLv59jAbnzYTDc30mhjEszqXF4lzzXvtzsGtn7GlGErH6Ip6/LGhIEphWd4ddmXNiXi6r9Adzl8rglNRTSwcGU4uHg+zizeduyATWtQBIOIpXD2rNAHIAECgYEA6Z0+uT+tgeD2zpiznJVAZlmRgxInKyGshOGhsNP0cEhHbdJSNhjm5gkvOl6sgxJ+CYB/VHrByfQSY5hEQknx53GFMhg8KwdzLiSJDcpY4FkSqEGMjOCk6d92QcphoJYfvZ9jtjbzo7VTzRoTGPsp1ZvyA1T8JtoRbfKgxd2i2K0CgYEAyoW0GfLJLc+wDzGi6QALaIzk9VcUjHkPCTuj0xSEEfmY7SQbnbSd+T53tTadrkswKws390mvyHSv+RswxGJv48PlT31UhtynlfMAE1GrlrJ7vtNlsy1rsx0XzSKtIDNrFjEu5GkVQ5tkahr99qpRnD0MFA3xH00b50VyxMCMimUCgYAmH6Inywt+oX7FckgFapnq2f0UHbdEo6cqvEONvtkqJbF6a5M8/s1XhvItHVwbu73TwSOGXs4XLfx+QlAJXVXbxjvNVAUlpH6Ybh/rnzTnz8Fqsd/E8bgX7n6299b8xOMDJ+q2xrr14VZ+px2suvg1wtA42PqZQIcNoUW5ZJT5tQKBgBFMhmvI/0I4gVNq6/13EYJmto/2Vj0BgjVJsN6w2+8lINjwwqMf8HZ/zX3fImzm40Bp/ufSlX9L6FQg7HN57RDJhObbT8MNSgtW7GS6DywaJtPP/tnlQVPVYlkVYzBi8/y7SsQb7cMOnO8rSxIszjfIRyXXYwdHcOC6X+lKgTa5AoGBANyTwWLqyCS5plpPHm+x+JyEsiIc37fwhZh5BOXEVQkjsgE1cNummv9be/+bAyyPuXrFfLMMpYOH2Ye7oJAD7OEL92mEpAgkb6c9gRWbkm6vrK+Fp3p5bx+/4KArwN/89s4oQEO/7dwIsioAuYlxC8mCjAf1Fh8UvoGPLvpMfFX5'
    alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA97wRQhe632w+Z8PUTJFatjpZQhXuiduZ7PoO5LtE/JpGpdk2Z/g4AiSV+/cwzQhlCnF/br4i0M8el4Y6MMCsG/YZABj5O4R40mOmecUKiFg8LyGEAZWvX3qFwOeL4HFoiNleO2A2jidtys2Y8odeginnIqQ+8leTFIKkwe1uWAL0N+SJwNz9zwYRwiywVmq8HYtOxZzXX89s4GxlaqpGTzbsyX6FEFxdf4vvOYbNtJZ0sSPCs3345R25wDsvHinZ6tACtwMROTjxgLz43HUQJSiWtKaR+yKBn+kbhN0awoPlxDo58onbhDhz3oSHUCLb6uSSWX+ba/BX+Kwdr/OY/wIDAQAB'

    """
    得到客户端对象。
    注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
    logger参数用于打印日志，不传则不打印，建议传递。
    """
    client = DefaultAlipayClient(alipay_client_config=alipay_client_config)

    model = AlipayTradeAppPayModel()
    model.timeout_express = "90m"
    model.total_amount = "9.00"
    model.seller_id = "2088301194649043"
    model.product_code = "QUICK_MSECURITY_PAY"
    model.body = "Iphone6 16G"
    model.subject = "iphone"
    model.out_trade_no = "201800000001201"
    request = AlipayTradeAppPayRequest(biz_model=model)
    response = client.sdk_execute(request)
    print("alipay.trade.app.pay response:" + response)


def return_url(request):
    user_id = request.session.get('user_id')
    order_from = models.Order_form.objects.filter(user_id_id=user_id, pay_status=0).first()
    id = order_from.id

    models.Order_form.objects.filter(id=id).update(pay_status=1)

    return HttpResponse('asdasd')

