from flask import Flask,request,render_template
a=Flask(__name__)

@a.route('/',methods=['GET','POST'])#欢迎页面
def home():
    return render_template('index.html')

@a.route('/login',methods=['GET'])#登录页面
def signin_get():
    return render_template('from.html')

@a.route('/login',methods=['POST'])#登陆成功页面
def signin_post():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='123456':
        return render_template('succeed.html',username=username)
    return render_template('from.html',message='用户名或密码错误',username=username)
    
if __name__=='__main__':
    a.run()