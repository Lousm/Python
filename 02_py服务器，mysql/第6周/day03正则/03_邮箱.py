import re
string='245531198@163.com'
r=re.match('^\w+@\w+\.((com)|(cn)|(net))$',string)
print(r.group())