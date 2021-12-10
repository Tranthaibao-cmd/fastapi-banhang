from fastapi import APIRouter,Body
from starlette.responses import Response
from config.db_MH import receive_MH,add_MH,update_MH,delete_MH,get_MH
from fastapi.encoders import jsonable_encoder
from models.user import MH, ResponseModel,ErrorResponseModel

router = APIRouter()
#get all data
@router.get('/',summary="get all mat hang")
async def get_all_MH():
    get_MH= await receive_MH()
    if get_MH: 
        return ResponseModel(get_MH,"successfull")
    else:
        return ResponseModel(get_MH,"empty--rong")
#add data
@router.post('/',summary="add mat hang")
async def addMH(add:MH=Body(...)):
    new_add= await add_MH(add.dict())
    if new_add:
        return ResponseModel(new_add,"successfull")
    else:
        return ErrorResponseModel("error",404,"cant add")
#get data with id
@router.get("/{id}",summary="read data with id")
async def get_MHs(id:str):
    _id= await get_MH(id)
    if _id.get("code")!=404:
        return ResponseModel(_id,"successfull")
    elif _id.get("code")==404:
        return ErrorResponseModel ("dont MH",404,"dont exist")

#update data with id
@router.put("/{id}",summary="update by id")
async def update(id:str,data:MH=Body(...)):
    MH_update= await update_MH(id,data.dict())
    if MH_update:
        return ResponseModel("MH by id","successfull")
    else:
        return ErrorResponseModel("error",404,"cant update")


#delete data with id
@router.delete("/{id}",summary="delete with id")
async def delete(id:str):
    del_MH= await delete_MH(id)
    if del_MH:
        return ResponseModel("MH by id delete","successfull")
    else:
        return ErrorResponseModel("error",404,"dont {id} exist")




