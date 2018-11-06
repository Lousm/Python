from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

drive = webdriver.PhantomJS(
    executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

drive1=webdriver.Chrome()
drive1.get('http://langlang2017.com/')
print(drive1.page_source)
drive1.save_screenshot('langlang-Chrome.png')

# drive.get('http://langlang2017.com/')
#
# print(drive.page_source)
#
# drive.save_screenshot('langlang01.png')

# drive.get('https://www.baidu.com')
# # print(drive.page_source)
# #截图
# drive.save_screenshot('baidu01.png')
#
# drive.find_element_by_id('kw').send_keys('美女')
# drive.save_screenshot('baidu02.png')
#
# #点击百度一下
# drive.find_element_by_id('su').click()
# time.sleep(3)
# drive.save_screenshot('baidu03.png')
#
# #获取cookie
# # print(drive.get_cookies())
#
# #模拟键盘操作
# #1全选
# drive.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# time.sleep(2)
# drive.save_screenshot('baidu04.png')
# #2剪切
# drive.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
# drive.save_screenshot('baidu05.png')
# #粘贴
# drive.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
# drive.save_screenshot('baidu06.png')
