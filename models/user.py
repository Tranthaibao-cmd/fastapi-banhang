from pydantic import BaseModel,Field, fields
class NSX(BaseModel):
    ten:str=''
    diachi:str=''
    SĐT:float

class KH(BaseModel):
    diachi:str=''
    gioitinh:str=''
    SĐT:float
    ten:str=''

class MH(BaseModel):
    giatien:float
    idNSX:str=''
    loai:str=''
    mau:str=''
    soluong:float
    ten:str=''
class NV(BaseModel):
    diachi:str=''
    gioitinh:str=''
    SĐT:float
    ten:str=''
class CTDH(BaseModel):
    giatien:float
    idMHang:str=''
    soluong:float
class DH(BaseModel):
    idCTDH:str=''
    idNV:str=''
    idKH:str=''
    giatien:float
    
    
def ResponseModel(data,message):
    return {
        "data":[data],
        "code":200,
        "message":message
    }

def ErrorResponseModel(error,code,message):
    return {
        "error":error,
        "code":code,
        "message":message
    }

