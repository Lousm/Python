from flask import Flask
from flask import request

a=Flask(__name__)

@a.route('/',methods=['GET','POST'])#欢迎页面
def home():
    return '<h1>hello</h1>'

@a.route('/login',methods=['GET'])#登录页面
def signin_get():
    return '''
        <form method="POST">
        <p><input name="username"></p>
        <p><input type="password" name="password"></p>
        <p><button type="submit">提交</button></p>
        </form>
    '''

@a.route('/login',methods=['POST'])#登陆成功页面
def signin_post():
    if request.form['username']=='admin' and request.form['password']=='123456':
        return '''<h1>登录成功</h1>
            <h1>你好，admin</h1>
            '''
    return '<h1>错误的用户名或密码</h1>'
    
if __name__=='__main__':
    a.run()