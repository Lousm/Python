from selenium import webdriver
import time

drive=webdriver.PhantomJS(executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

drive.get('https://www.baidu.com')

drive.save_screenshot('baidu.png')

