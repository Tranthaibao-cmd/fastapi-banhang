from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
import json
mongo_uri="mongodb://127.0.0.1:27017"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db=client.config


NSX_collection = db.get_collection('NHASANXUAT')

async def receive_NSX():
    NSX = []
    a = NSX_collection.find()
    async for dh in a:
        dh['_id'] = str(dh['_id'])
        NSX.append(dh)
    return NSX

#add NSX
async def add_NSX(add:dict)->dict:
    NSX= await NSX_collection.insert_one(add.dict())
    new_NSX= await NSX_collection.find_one({"_id":NSX.inserted_id})
    new_NSX['_id']=str(new_NSX['_id'])
    return  new_NSX
      
#get data wiht id

async def get_NSX(id:str)->dict:
    
    NSX= await NSX_collection.find_one({"_id":ObjectId(id)})
    if NSX:
        NSX['_id'] = str(NSX['_id'])
        return NSX
    else:
        return {"error":"dont exist","code":404}

#update with id
async def update_NSX(id:str,data:dict):
    if len(data)<1:
        return False
    NSX= await NSX_collection.find_one({"_id":ObjectId(id)})
    if NSX:
        update_NSX= await NSX_collection.update_one({"_id":ObjectId(id)},{"$set":data})
        if update_NSX:
            return True
        else:
            return{"error":"fail"}
    else:
        return{"error":"not find"}

#delete with id
async def delete_NSX(id:str):
    NSX= await NSX_collection.find_one({"_id":ObjectId(id)})
    if NSX:
        await NSX_collection.delete_one({"_id":ObjectId(id)})
        return True
    else:
        return False


