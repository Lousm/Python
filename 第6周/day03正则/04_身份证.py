import re
# a=re.match('[1922-2019]{4}','19')
strs='410882199602296551'

r=re.match(r'^[1-9]\d{5}[1-2][0-9]{3}((([0][13578])([0-2][0-9]|[3][01]))|'
           r'(([0][46])([0-2][0-9]|[30]{2}))|(([02]{2})([0-2][0-9]))|'
           r'(([1][02])([0-2][0-9]|[3][01]))|(([11]{2})([0-2][0-9]|[30]{2})))\d{4}$',strs)
print(r.group())
print(len('^[1-9]\d{5}[1-2][0-9]{3}((([0][13578])([0-2][0-9]|[3][01]))|(([0][46])([0-2][0-9]|[30]{2}))|(([02]{2})([0-2][0-9]))|'r'(([1][02])([0-2][0-9]|[3][01]))|(([11]{2})([0-2][0-9]|[30]{2})))\d{4}$'))