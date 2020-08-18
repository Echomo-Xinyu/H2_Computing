from pymongo import MongoClient

# start the mongo client app
client = MongoClient("localhost", 27017)
con = client["database"]["connection"]
con.drop()

con.insert_one({"a":1, "b":2})
con.insert_many([{"a":1, "b":2}, {"a":2, "b":3}])

cur = con.find()
cur = con.find({"$or":[{"Region":"Sub-Saharan Africa"}, {"Region":"East Asia"}]}, {"_id":0, "Country":1})
cur = con.find({"$and":[{"NT":{"$gt":200}}, {"LC":{"$gt":1000}}]}, {"_id":0, "Country":1})
cur = con.find({"Region":{"$not":{"$eq":"South & Southeast Asia"}}}, {"_id":0, "Country":1})

for i in cur:
    print(cur)
