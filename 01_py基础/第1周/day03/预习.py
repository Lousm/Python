info={'name':'小明','age':21,'height':184,'id':110,'tel':503598}

# 访问字典元素
print(info['name'])
print(info.get('age'))

# 得到字典所有的键 keys() 返回一个字典所有的键。返回列表
print(info.keys())

# 得到字典所有的值 values() 返回一个字典所有的值。返回列表
print(info.values())

#items() 把一个字典的每个键值对包装成元组，并将这些元组写入到列表中返回。返回列表
print(info.items())

# 删除字典元素
del info['name']
print(info)

print(info.pop('age'))
print(info)

print(info.popitem())
print(info)