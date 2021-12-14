from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
mongo_uri="mongodb://baotran:Baobao99@baotran-shard-00-00.dx30e.mongodb.net:27017,baotran-shard-00-01.dx30e.mongodb.net:27017,baotran-shard-00-02.dx30e.mongodb.net:27017/mongo?ssl=true&replicaSet=atlas-b854c8-shard-0&authSource=admin&retryWrites=true&w=majority"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db=client.mongo


don_hang_collection = db.get_collection('DONHANG')

# def donhang_sup(don_hang)->dict:
#     return{
#         "id":str(don_hang["_id"]),
#         "idCTDonHang":don_hang["idCTDONHANG"],
#         "idNV":don_hang["idNV"],
#         "idKH":don_hang["idKH"],
#         "giatien":don_hang["giatien"]
#     }
#get all data collection
async def receive_don_hangs():
    don_hang = []
    a = don_hang_collection.find()
    async for dh in a:
        dh['_id'] = str(dh['_id'])
        don_hang.append(dh)
    
    return don_hang
#add donhang
async def add_donhangs(add:dict)->dict:
    donhang= await don_hang_collection.insert_one(add.dict())
    new_donhang= await don_hang_collection.find_one({"_id":donhang.inserted_id})
    new_donhang['_id']=str(new_donhang['_id'])
    return  new_donhang
      
#get data wiht id

async def get_donhang(id:str)->dict:
    
    donhang= await don_hang_collection.find_one({"_id":ObjectId(id)})
    if donhang:
        donhang['_id'] = str(donhang['_id'])
        return donhang
    else:
        return {"error":"dont exist","code":404}

#update with id
async def update_donhang(id:str,data:dict):
    if len(data)<1:
        return False
    donhang= await don_hang_collection.find_one({"_id":ObjectId(id)})
    if donhang:
        update_dh= await don_hang_collection.update_one({"_id":ObjectId(id)},{"$set":data})
        if update_dh:
            return True
        else:
            return{"error":"fail"}
    else:
        return{"error":"not find"}

#delete with id
async def delete_dh(id:str):
    donhang= await don_hang_collection.find_one({"_id":ObjectId(id)})
    if donhang:
        await don_hang_collection.delete_one({"_id":ObjectId(id)})
        return True
    else:
        return False


