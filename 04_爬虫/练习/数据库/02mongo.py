import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.student

student = {
    'id': '20151515183',
    'name': '小gf',
    'age': 22,
    'height': 180
}
student2 = {
    'id': '20151515143',
    'name': '小as',
    'age': 232,
    'height': 170
}

# 插入的三种方法
# a = collection.insert(student)
# a=collection.insert_one(student)
# a=collection.insert_many([student,student2])
# print(a)
# print(a.inserted_ids)

# 查询
# a=collection.find_one({'height':170})
# print(a)

# a = collection.find({'age': 22})
# print(a)
# for i in a:
#     print(i)

# 指定使用正则表达式查询   查询name以 明 结尾的数据
a = collection.find({'name': {'$regex': '.*明'}})
for i in a:
    print(i)

# 排序  调用sort方法 在其中传入要排序的字段和排序规则即可    skip设置偏移量（从开始向后偏移几位）
b = collection.find().sort('name', pymongo.ASCENDING).skip(1)
print(b)
for i in b:
    print([i['name']])

# 更新
# 先将要更新的数据查询出来
old = {'name': '小gf'}
stu = collection.find_one(old)

# 指定要更新的字段
stu['age'] = 32


