from wsgiref.simple_server import make_server

def response(e,s_response):
    s_response('200 ok',[('Content-Type', 'text/html')])
    data='<h1>hello %s</h1>'%(e['PATH_INFO'][1:] or 'web')
    return [data.encode('utf-8')]

httpd=make_server('',8000,response)
print('HTTP服务器启动8000端口')
httpd.serve_forever()