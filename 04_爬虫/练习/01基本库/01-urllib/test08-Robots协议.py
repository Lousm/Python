import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/sign_in'))
          