from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
import json
mongo_uri="mongodb://baotran:Baobao99@baotran-shard-00-00.dx30e.mongodb.net:27017,baotran-shard-00-01.dx30e.mongodb.net:27017,baotran-shard-00-02.dx30e.mongodb.net:27017/mongo?ssl=true&replicaSet=atlas-b854c8-shard-0&authSource=admin&retryWrites=true&w=majority"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db=client.mongo


MH_collection = db.get_collection('MATHANG')
NSX_collection = db.get_collection('NHASANXUAT')

async def receive_MH():
    MH = []
    a = MH_collection.find()
    async for dh in a:
        # nsx= await NSX_collection.find_one({"_id":ObjectId( dh["idNSX"])})
        # dh["tennsx"]=nsx['ten']
        dh['_id'] = str(dh['_id'])
        MH.append(dh)
    return MH

#add MH
async def add_MH(add:dict)->dict:
    MH= await MH_collection.insert_one(add)
    new_MH= await MH_collection.find_one({"_id":MH.inserted_id})
    new_MH['_id']=str(new_MH['_id'])
    return  new_MH
      
#get data wiht id

async def get_MH(id:str)->dict:
    
    MH= await MH_collection.find_one({"_id":ObjectId(id)})
    if MH:
        MH['_id'] = str(MH['_id'])
        return MH
    else:
        return {"error":"dont exist","code":404}

#update with id
async def update_MH(id:str,data:dict):
    if len(data)<1:
        return False
    MH= await MH_collection.find_one({"_id":ObjectId(id)})
    if MH:
        update_MH= await MH_collection.update_one({"_id":ObjectId(id)},{"$set":data})
        if update_MH:
            return True
        else:
            return{"error":"fail"}
    else:
        return{"error":"not find"}

#delete with id
async def delete_MH(id:str):
    MH= await MH_collection.find_one({"_id":ObjectId(id)})
    if MH:
        await MH_collection.delete_one({"_id":ObjectId(id)})
        return True
    else:
        return False


