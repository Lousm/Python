import requests, json, jsonpath
from openpyxl import workbook

wb = workbook.Workbook()
ws = wb.active
ws.append(['id', 'name', 'parentId', 'code'])

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

con = requests.get(url).content.decode('utf-8')

jsonobj = json.loads(con)

data_list = jsonpath.jsonpath(jsonobj, '$..allCitySearchLabels')
print(data_list[0])
for k, v in data_list[0].items():
    for i in v:
        id = jsonpath.jsonpath(i, '$..id')
        name = jsonpath.jsonpath(i, '$..name')
        parentId = jsonpath.jsonpath(i, '$..parentId')
        code = jsonpath.jsonpath(i, '$..code')
        ws.append([id[0], name[0], parentId[0], code[0]])
        # print(id)

wb.save('拉钩.xlsx')
