import pymongo
client = pymongo.MongoClient("mongodb+srv://RRB:Rlr26152792@rbt50.8rqtaok.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name' : 'rohit',
    'email' : 'iafmigrohit4@gmail.com',
    'surname' : 'Bansod'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)