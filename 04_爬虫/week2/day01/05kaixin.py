from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, requests

drive = webdriver.PhantomJS(
    executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

drive.get('http://www.kaixin001.com/')
#输入账号密码
drive.find_element_by_name('loginemail').send_keys('17739115043')
drive.find_element_by_name('password').send_keys('ying0229._')
drive.save_screenshot('kaixin01.png')

drive.find_element_by_id('btn_dl').click()
drive.save_screenshot('kaixin02.png')

# 获取验证码图片链接
con = drive.page_source
soup = BeautifulSoup(con, 'lxml')
img = soup.select('img[id="randimg"]')[0].attrs['src']
print(img)

#请求验证码 获得图片
res = requests.get(img)
print(res)
with open('kaixincode.png', 'wb') as f:
    f.write(res.content)

# 获取验证码图片链接
con = drive.page_source
soup = BeautifulSoup(con, 'lxml')
img = soup.select('img[id="randimg"]')[0].attrs['src']
print(img)


#输入验证码再次登录
code = input('请输入验证码：')
drive.find_element_by_id('code').send_keys('code')
drive.find_element_by_id('btn_dl').submit()
time.sleep(3)

js = 'document.body.scrollTop=5000'
drive.execute_script(js)

drive.save_screenshot('kaixin03.png')

# 获取验证码图片链接
con = drive.page_source
soup = BeautifulSoup(con, 'lxml')
img = soup.select('img[id="randimg"]')[0].attrs['src']
print(img)

with open('kaixin.html', 'w', encoding='gbk') as f:
    f.write(drive.page_source)
print(drive.current_url)