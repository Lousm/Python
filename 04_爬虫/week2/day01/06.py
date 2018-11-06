from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, requests

drive = webdriver.PhantomJS(
    executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

drive.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')
time.sleep(5)

drive.save_screenshot('06电影01.png')

js = 'document.body.scrollTop=10000'
drive.execute_script(js)

time.sleep(5)

js = 'document.body.scrollTop=10000'
drive.execute_script(js)

time.sleep(5)
drive.save_screenshot('06电影02.png')
