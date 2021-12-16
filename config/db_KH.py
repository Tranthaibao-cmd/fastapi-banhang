from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
import json
mongo_uri="mongodb://baotran:Baobao99@baotran-shard-00-00.dx30e.mongodb.net:27017,baotran-shard-00-01.dx30e.mongodb.net:27017,baotran-shard-00-02.dx30e.mongodb.net:27017/mongo?ssl=true&replicaSet=atlas-b854c8-shard-0&authSource=admin&retryWrites=true&w=majority"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db=client.mongo


KH_collection = db.get_collection('KHACHHANG')

async def receive_KH():
    KH = []
    a = KH_collection.find()
    async for dh in a:
        dh['_id'] = str(dh['_id'])
        KH.append(dh)
    return KH

#add KH
async def add_KH(add:dict)->dict:
    KH= await KH_collection.insert_one(add)
    new_KH= await KH_collection.find_one({"_id":KH.inserted_id})
    new_KH['_id']=str(new_KH['_id'])
    return  new_KH
      
#get data wiht id

async def get_KH(id:str)->dict:
    
    KH= await KH_collection.find_one({"_id":ObjectId(id)})
    if KH:
        KH['_id'] = str(KH['_id'])
        return KH
    else:
        return {"error":"dont exist","code":404}

#update with id
async def update_KH(id:str,data:dict):
    if len(data)<1:
        return False
    KH= await KH_collection.find_one({"_id":ObjectId(id)})
    if KH:
        update_KH= await KH_collection.update_one({"_id":ObjectId(id)},{"$set":data})
        if update_KH:
            return True
        else:
            return{"error":"fail"}
    else:
        return{"error":"not find"}

#delete with id
async def delete_KH(id:str):
    KH= await KH_collection.find_one({"_id":ObjectId(id)})
    if KH:
        await KH_collection.delete_one({"_id":ObjectId(id)})
        return True
    else:
        return False


