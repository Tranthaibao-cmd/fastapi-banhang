from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
import json
mongo_uri="mongodb://baotran:Baobao99@baotran-shard-00-00.dx30e.mongodb.net:27017,baotran-shard-00-01.dx30e.mongodb.net:27017,baotran-shard-00-02.dx30e.mongodb.net:27017/mongo?ssl=true&replicaSet=atlas-b854c8-shard-0&authSource=admin&retryWrites=true&w=majority"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db=client.mongo


CTDH_collection = db.get_collection('CHITIETDONHANG')

async def receive_CTDH():
    CTDH = []
    a = CTDH_collection.find()
    async for dh in a:
        dh['_id'] = str(dh['_id'])
        CTDH.append(dh)
    return CTDH

#add CTDH
async def add_CTDH(add:dict)->dict:
    CTDH= await CTDH_collection.insert_one(add.dict())
    new_CTDH= await CTDH_collection.find_one({"_id":CTDH.inserted_id})
    new_CTDH['_id']=str(new_CTDH['_id'])
    return  new_CTDH
      
#get data wiht id

async def get_CTDH(id:str)->dict:
    
    CTDH= await CTDH_collection.find_one({"_id":ObjectId(id)})
    if CTDH:
        CTDH['_id'] = str(CTDH['_id'])
        return CTDH
    else:
        return {"error":"dont exist","code":404}

#update with id
async def update_CTDH(id:str,data:dict):
    if len(data)<1:
        return False
    CTDH= await CTDH_collection.find_one({"_id":ObjectId(id)})
    if CTDH:
        update_CTDH= await CTDH_collection.update_one({"_id":ObjectId(id)},{"$set":data})
        if update_CTDH:
            return True
        else:
            return{"error":"fail"}
    else:
        return{"error":"not find"}

#delete with id
async def delete_CTDH(id:str):
    CTDH= await CTDH_collection.find_one({"_id":ObjectId(id)})
    if CTDH:
        await CTDH_collection.delete_one({"_id":ObjectId(id)})
        return True
    else:
        return False


