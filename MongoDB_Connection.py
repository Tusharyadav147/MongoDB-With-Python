import pymongo

#To connect mongodb with python use this command
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient.MYDB.organization

mydb.update_one({"skills.Data analysis.0":"powerBI"}, {"$set": {"skills.Data analysis.0": "Yes"}})