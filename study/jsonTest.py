import json

# # 把python对象转换成json字符串
# json.dumps()
# # 把json格式的字符串转换成python对象
# json.loads()
# # 将python内置类型序列化为json对象后写入文件
# json.dump()
# # 读取文件中json形式的字符串转化成python类型
# json.load()

str1 = '{"name":"张三"}'
obj = json.loads(str1)
print(type(obj))
print(obj)

str2 = json.dumps(obj, ensure_ascii=False)
print(type(str2))
print(str2)

json.dump(obj, open('json.txt', 'w', encoding='utf-8'), ensure_ascii=False)

obj2 = json.load(open('json.txt', encoding='utf-8'))
print(type(obj2))
print(obj2)