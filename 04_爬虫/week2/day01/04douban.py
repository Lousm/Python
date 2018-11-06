from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

drive = webdriver.PhantomJS(
    executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

drive.get('https://www.douban.com/')

drive.save_screenshot('douban01.png')

with open('douban.html', 'w', encoding='utf-8') as f:
    f.write(drive.page_source)

drive.find_element_by_id('form_email').send_keys('245531198@qq.com')
drive.find_element_by_id('form_password').send_keys('ying0229._')
# a=drive.find_element_by_id('fodefsfdssword')
# a=drive.find_element_by_id('fpioulyukrth').send_keys('ying0229._')
drive.save_screenshot('douban02.png')


try:
    if drive.find_element_by_id('captcha_image'):
        cood = input('请输入验证码：')
        drive.find_element_by_id('captcha_field').send_keys(cood)
        drive.save_screenshot('douban03.png')
except:
    print('验证码没有')

drive.find_element_by_class_name('bn-submit').click()
time.sleep(5)
drive.save_screenshot('douban04.png')

# cood=input('请输入验证码：')
# drive.find_element_by_id()
