from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
import json
mongo_uri="mongodb://baotran:Baobao99@baotran-shard-00-00.dx30e.mongodb.net:27017,baotran-shard-00-01.dx30e.mongodb.net:27017,baotran-shard-00-02.dx30e.mongodb.net:27017/mongo?ssl=true&replicaSet=atlas-b854c8-shard-0&authSource=admin&retryWrites=true&w=majority"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db=client.mongo


NV_collection = db.get_collection('NHANVIEN')

async def receive_NV():
    NV = []
    a = NV_collection.find()
    async for dh in a:
        dh['_id'] = str(dh['_id'])
        NV.append(dh)
    return NV

#add NV
async def add_NV(add:dict)->dict:
    NV= await NV_collection.insert_one(add)
    new_NV= await NV_collection.find_one({"_id":NV.inserted_id})
    new_NV['_id']=str(new_NV['_id'])
    return  new_NV
      
#get data wiht id

async def get_NV(id:str)->dict:
    
    NV= await NV_collection.find_one({"_id":ObjectId(id)})
    if NV:
        NV['_id'] = str(NV['_id'])
        return NV
    else:
        return {"error":"dont exist","code":404}

#update with id
async def update_NV(id:str,data:dict):
    if len(data)<1:
        return False
    NV= await NV_collection.find_one({"_id":ObjectId(id)})
    if NV:
        update_NV= await NV_collection.update_one({"_id":ObjectId(id)},{"$set":data})
        if update_NV:
            return True
        else:
            return{"error":"fail"}
    else:
        return{"error":"not find"}

#delete with id
async def delete_NV(id:str):
    NV= await NV_collection.find_one({"_id":ObjectId(id)})
    if NV:
        await NV_collection.delete_one({"_id":ObjectId(id)})
        return True
    else:
        return False


