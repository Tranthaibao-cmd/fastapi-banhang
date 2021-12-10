from fastapi import APIRouter,Body
from starlette.responses import Response
from config.db_DH import receive_don_hangs,add_donhangs,update_donhang,delete_dh,get_donhang
from fastapi.encoders import jsonable_encoder
from models.user import ResponseModel,ErrorResponseModel

router = APIRouter()

@router.get('/',summary="get all don hang")
async def get_all_dh():
    donhang= await receive_don_hangs()
    if donhang: 
        return ResponseModel(donhang,"successfull")
    else:
        return ResponseModel(donhang,"empty--rong")


@router.post('/',summary="add don hang")
async def add_dh(add:dict=Body(...)):
    add =jsonable_encoder(add)
    new_add= await add_donhangs(add)
    if new_add:
        return ResponseModel(new_add,"successfull")
    else:
        return ErrorResponseModel("error",404,"cant add")

@router.get("/{id}",summary="read data with id")
async def get_donhangs(id:str):
    donhang_id= await get_donhang(id)
    if donhang_id.get("code")!=404:
        return ResponseModel(donhang_id,"successfull")
    elif donhang_id.get("code")==404:
        return ErrorResponseModel ("dont don hang",404,"dont exist")


@router.put("/{id}",summary="update by id")
async def update(id:str,data:dict=Body(...)):
    donhang_update= await update_donhang(id,data)
    if donhang_update:
        return ResponseModel("don hang by id","successfull")
    else:
        return ErrorResponseModel("error",404,"cant update")

@router.delete("/{id}",summary="delete with id")
async def delete(id:str):
    del_dh= await delete_dh(id)
    if del_dh:
        return ResponseModel("don hang by id delete","successfull")
    else:
        return ErrorResponseModel("error",404,"dont {id} exist")




