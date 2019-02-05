import pymongo
from pymongo import MongoClient

# write correct link
client = MongoClient('mongodb://andrewxxxxmorgan%40gmail.com:\
    my_password@stitch.mongodb.com:27020/?authMechanism=PLAIN&\
    authSource=%24external&ssl=true&\
    appName=imported_trackme-etjzr:mongodb-atlas:local-userpass')

# fix this stuff
db = client.trackme
collection = db.comments

data = collection.find_one()
