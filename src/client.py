import pymongo

class client:
    def __init__(self):
        # write correct link
        self.client = pymongo.MongoClient('mongodb://test:testingtesting123@cluster0-shard-00-00-g0o5k.mongodb.net:27017,cluster0-shard-00-01-g0o5k.mongodb.net:27017,cluster0-shard-00-02-g0o5k.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
        # print(self.client)
        # self.client = pymongo.MongoClient('mongodb+srv://test:testingtesting123@cluster0-g0o5k.mongodb.net/test?retryWrites=true')

    def checkNewData(self):
        # db = self.client.stopBang
        # collection = db.answers # correct this collection
        # returnData = collection.find_one()
        db = self.client.general
        collection = db.checkState # correct this collection
        returnData = collection.find_one()['done']
        # returnData = collection.find_one()
        data = collection.find_one_and_replace({'done': 1}, {'done': 0})

        print(data)
        return returnData
        # pass

    def getNewData(self, _db):
        db = self.client[_db]
        collection = db["answers"] # correct this collection
        returnData = collection.find_one()

        return returnData

    def sendData(self, data):
        db = self.client.general
        collection = db.score # correct this collection
        data = collection.find_one_and_replace({}, {
            'score': data['score'],
            'heartRate': data['heartRate'],
            'breathing': data['breathing'],
            'eeg': data['eeg']
        })
        print(data)

# self.db = self.client.postSleep
# self.collection = self.db.questions # correct this collection
# print(self.collection.find_one())
