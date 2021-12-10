from fastapi import APIRouter,Body
from starlette.responses import Response
from config.db_KH import receive_KH,add_KH,update_KH,delete_KH,get_KH
from fastapi.encoders import jsonable_encoder
from models.user import KH, ResponseModel,ErrorResponseModel

router = APIRouter()
#get all data
@router.get('/',summary="get all khach hang")
async def get_all_KH():
    get_KH= await receive_KH()
    if get_KH: 
        return ResponseModel(get_KH,"successfull")
    else:
        return ResponseModel(get_KH,"empty--rong")
#add data
@router.post('/',summary="add khach hang")
async def addKH(add:KH=Body(...)):
    new_add= await add_KH(add.dict())
    if new_add:
        return ResponseModel(new_add,"successfull")
    else:
        return ErrorResponseModel("error",404,"cant add")
#get data with id
@router.get("/{id}",summary="read data with id")
async def get_KHs(id:str):
    _id= await get_KH(id)
    if _id.get("code")!=404:
        return ResponseModel(_id,"successfull")
    elif _id.get("code")==404:
        return ErrorResponseModel ("dont KH",404,"dont exist")

#update data with id
@router.put("/{id}",summary="update by id")
async def update(id:str,data:KH=Body(...)):
    KH_update= await update_KH(id,data.dict())
    if KH_update:
        return ResponseModel("KH by id","successfull")
    else:
        return ErrorResponseModel("error",404,"cant update")


#delete data with id
@router.delete("/{id}",summary="delete with id")
async def delete(id:str):
    del_KH= await delete_KH(id)
    if del_KH:
        return ResponseModel("KH by id delete","successfull")
    else:
        return ErrorResponseModel("error",404,"dont {id} exist")




