import pymongo

url = 'mongodb://localhost:27017'
myclient = pymongo.MongoClient(url)

db = myclient["test"]
collection = db['users']


def insert_test_user():
    test_user = {
        "name": "rino",
        "age": 26
    }

    post_id = collection.insert_one(test_user).inserted_id
    print post_id

def query_test_user():
    test_user = collection.find_one({'name':'rino'})
    print test_user

if __name__ == "__main__":
    insert_test_user()
    query_test_user()
