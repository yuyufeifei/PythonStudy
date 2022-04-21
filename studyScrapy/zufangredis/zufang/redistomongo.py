import json

from redis import Redis
from pymongo import MongoClient

redis_client = Redis(host='127.0.0.1', port=6379)   # 默认为localhost:6379
mongo_client = MongoClient(host='127.0.0.1', port=27017)    # 默认为localhost:27017

while True:
    # 取数据，数据取完之后redis中就没了
    source, data = redis_client.blpop(['lianjia:items'])
    print(source, data)
    # 转换类型 从bytes转成json
    json_data = json.loads(data)

    lianjia = mongo_client.zufang.lianjiaredis
    lianjia.insert_one(json_data)
