class Err(Exception):
    def __init__ (self ,msg):
        self.msg=msg
    
    def __str__ (self):
        return self.msg

try:
    raise Err('自定义异常')
except Err as e:
    print(e)