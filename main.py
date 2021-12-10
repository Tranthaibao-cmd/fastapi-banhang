from fastapi import FastAPI
from routes.DH import router as DHRouter
from routes.NSX import router as NSXRouter
from routes.MH import router as MHRouter
from routes.KH import router as KHRouter
from routes.CTDH import router as CTDHRouter
from routes.NV import router as NVRouter

app = FastAPI()

app.include_router(DHRouter,tags=["DON HANG"],prefix='/donhang')
app.include_router(NSXRouter,tags=["NHA SAN XUAT"],prefix='/NSX')
app.include_router(MHRouter,tags=["MAT HANG"],prefix='/MH')
app.include_router(KHRouter,tags=["KHACH HANG"],prefix='/KH')
app.include_router(CTDHRouter,tags=["CHI TIET DON HANG"],prefix='/CTDH')
app.include_router(NVRouter,tags=["NHAN VIEN"],prefix='/NV')

#  python -m venv D:\be-mongo\venv 