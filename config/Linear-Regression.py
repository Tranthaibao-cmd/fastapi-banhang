from pymongo import MongoClient
import motor.motor_asyncio 
import motor
from bson.objectid import ObjectId
import json
import matplotlib.pyplot as plt
from scipy import stats
import asyncio

mongo_uri="mongodb://baotran:Baobao99@baotran-shard-00-00.dx30e.mongodb.net:27017,baotran-shard-00-01.dx30e.mongodb.net:27017,baotran-shard-00-02.dx30e.mongodb.net:27017/mongo?ssl=true&replicaSet=atlas-b854c8-shard-0&authSource=admin&retryWrites=true&w=majority"

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
db=client.mongo
mathang_collection = db.get_collection('MATHANG')
don_hang_collection = db.get_collection('DONHANG')
X1=[]
Y2=[]

async def regression():
  a =  mathang_collection.find()
  async for x in a:
    X1.append(x['giatien'])
  b =  don_hang_collection.find()
  async for y in b:
    Y2.append(y['giatien'])
  return X1,Y2


# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
#y = [99,86,87,88,111,86,103,87,94]
loop = asyncio.get_event_loop()
loop.run_until_complete(regression() )
print("X1:",X1,"Y2",Y2)
slope, intercept, r, p, std_err = stats.linregress(X1, Y2) #Hồi Quy Tuyến Tính


def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, X1))

plt.scatter(X1, Y2)
plt.plot(X1, mymodel)
plt.show()
