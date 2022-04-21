import pymongo

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
# 选择Database
db = client.test
# 选择Collection
collection = db.gzh
# collection = db['gzh']
# print(collection)

# 插入操作
# stu = {'name': '老郭', 'age': 30, 'gender': '男'}
# collection.insert_one(stu)

# stuList = [
#     {'name': '老郭11', 'age': 35, 'gender': '男'},
#     {'name': '老郭22', 'gender': '男'},
#     {'name': '老郭33', 'age': 40}
# ]
# collection.insert_many(stuList)

# 更新一条
# collection.update_one({'name': '老郭'}, {'$set': {'age': 88}})
# 更新多条
# collection.update_many({'name': '老郭11'}, {'$set': {'gender': '女'}})

# 删除一条
# collection.delete_one({'name': '老郭22'})
# 删除多条
# collection.delete_many({'name': '老郭22'})

# 查询
# result = collection.find()
# for item in result:
#     print(item)

# result = collection.find({'name': 'gzh'})
# for item in result:
#     print(item)

# result = collection.find({'name': {'$regex': '老郭.*'}})
# for item in result:
#     print(item)

# result = collection.find().sort('age', pymongo.ASCENDING)
# for item in result:
#     print(item)

# result = collection.find().sort('age', pymongo.ASCENDING).limit(2)
# for item in result:
#     print(item)

# result = collection.find_one({'name': {'$regex': '老郭.*'}})
# print(result)