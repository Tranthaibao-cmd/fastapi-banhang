from fastapi import APIRouter,Body
from starlette.responses import Response
from config.db_CTDH import receive_CTDH,add_CTDH,update_CTDH,delete_CTDH,get_CTDH
from fastapi.encoders import jsonable_encoder
from models.user import CTDH, ResponseModel,ErrorResponseModel


router = APIRouter()
#get all data
@router.get('/',summary="get all chi tiet don hang")
async def get_all_CTDH():
    get_CTDH=await receive_CTDH()
    if get_CTDH: 
        return ResponseModel(get_CTDH,"successfull")
    else:
        return ResponseModel(get_CTDH,"empty--rong")
#add data
@router.post('/',summary="add chi tiet don hang")
async def addCTDH(add:CTDH=Body(...)):
    new_add= await add_CTDH(add.dict())
    if new_add:
        return ResponseModel(new_add,"successfull")
    else:
        return ErrorResponseModel("error",404,"cant add")
#get data with id
@router.get("/{id}",summary="read data with id")
async def get_CTDHs(id:str):
    _id= await get_CTDH(id)
    if _id.get("code")!=404:
        return ResponseModel(_id,"successfull")
    elif _id.get("code")==404:
        return ErrorResponseModel ("dont CTDH",404,"dont exist")

#update data with id
@router.put("/{id}",summary="update by id")
async def update(id:str,data:CTDH=Body(...)):
    CTDH_update= await update_CTDH(id,data.dict())
    if CTDH_update:
        return ResponseModel("CTDH by id","successfull")
    else:
        return ErrorResponseModel("error",404,"cant update")


#delete data with id
@router.delete("/{id}",summary="delete with id")
async def delete(id:str):
    del_CTDH= await delete_CTDH(id)
    if del_CTDH:
        return ResponseModel("CTDH by id delete","successfull")
    else:
        return ErrorResponseModel("error",404,"dont {id} exist")




