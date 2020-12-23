import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client['douyin']


#插入数据为主
def save_fans_info(task):
    task_id_collection = Collection(db,"fans_info")
    task_id_collection.update({'share_id': task['share_id']}, {'$set': task}, True)
