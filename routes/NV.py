from fastapi import APIRouter,Body
from starlette.responses import Response
from config.db_NV import receive_NV,add_NV,update_NV,delete_NV,get_NV
from fastapi.encoders import jsonable_encoder
from models.user import NV, ResponseModel,ErrorResponseModel

router = APIRouter()
#get all data
@router.get('/',summary="get all nhan vien")
async def get_all_NV():
    get_NV= await receive_NV()
    if get_NV: 
        return ResponseModel(get_NV,"successfull")
    else:
        return ResponseModel(get_NV,"empty--rong")
#add data
@router.post('/',summary="add nhan vien")
async def addNV(add:NV=Body(...)):
    new_add= await add_NV(add.dict())
    if new_add:
        return ResponseModel(new_add,"successfull")
    else:
        return ErrorResponseModel("error",404,"cant add")
#get data with id
@router.get("/{id}",summary="read data with id")
async def get_NVs(id:str):
    _id= await get_NV(id)
    if _id.get("code")!=404:
        return ResponseModel(_id,"successfull")
    elif _id.get("code")==404:
        return ErrorResponseModel ("dont NV",404,"dont exist")

#update data with id
@router.put("/{id}",summary="update by id")
async def update(id:str,data:NV=Body(...)):
    NV_update= await update_NV(id,data.dict())
    if NV_update:
        return ResponseModel("NV by id","successfull")
    else:
        return ErrorResponseModel("error",404,"cant update")


#delete data with id
@router.delete("/{id}",summary="delete with id")
async def delete(id:str):
    del_NV= await delete_NV(id)
    if del_NV:
        return ResponseModel("NV by id delete","successfull")
    else:
        return ErrorResponseModel("error",404,"dont {id} exist")




