import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client['test1']


#插入数据为主
def save_fans_info(task):
    task_id_collection = Collection(db,"test_insert")
    task_id_collection.update({'share_id': task['share_id']}, {'$set': task}, True)
    # try:
    #     task_id_collection.update_one({'share_id':task['share_id']},task,True)
    # except:
    #     task_id_collection.insert_one(task)

if __name__ == '__main__':
    task = {"share_id":9,'name':'xiang'}
    save_fans_info(task)