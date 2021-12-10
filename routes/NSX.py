from fastapi import APIRouter,Body
from starlette.responses import Response
from config.db_NSX import receive_NSX,add_NSX,update_NSX,delete_NSX,get_NSX
from fastapi.encoders import jsonable_encoder
from models.user import NSX, ResponseModel,ErrorResponseModel

router = APIRouter()
#get all data
@router.get('/',summary="get all nha san xuat")
async def get_all_NSX():
    get_NSX= await receive_NSX()
    if get_NSX: 
        return ResponseModel(get_NSX,"successfull")
    else:
        return ResponseModel(get_NSX,"empty--rong")
#add data
@router.post('/',summary="add nha san xuat")
async def addNSX(add:NSX=Body(...)):
    new_add= await add_NSX(add.dict())
    if new_add:
        return ResponseModel(new_add,"successfull")
    else:
        return ErrorResponseModel("error",404,"cant add")
#get data with id
@router.get("/{id}",summary="read data with id")
async def get_NSXs(id:str):
    _id= await get_NSX(id)
    if _id.get("code")!=404:
        return ResponseModel(_id,"successfull")
    elif _id.get("code")==404:
        return ErrorResponseModel ("dont nsx",404,"dont exist")

#update data with id
@router.put("/{id}",summary="update by id")
async def update(id:str,data:NSX=Body(...)):
    NSX_update= await update_NSX(id,data.dict())
    if NSX_update:
        return ResponseModel("nsx by id","successfull")
    else:
        return ErrorResponseModel("error",404,"cant update")


#delete data with id
@router.delete("/{id}",summary="delete with id")
async def delete(id:str):
    del_NSX= await delete_NSX(id)
    if del_NSX:
        return ResponseModel("nsx by id delete","successfull")
    else:
        return ErrorResponseModel("error",404,"dont {id} exist")




