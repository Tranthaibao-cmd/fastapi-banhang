from fastapi import FastAPI
from routes.DH import router as DHRouter
from routes.NSX import router as NSXRouter
from routes.MH import router as MHRouter
from routes.KH import router as KHRouter
from routes.CTDH import router as CTDHRouter
from routes.NV import router as NVRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://backend-mongoo.herokuapp.com",
    "http://localhost:5000",
    "http://localhost:4200",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(DHRouter,tags=["DON HANG"],prefix='/donhang')
app.include_router(NSXRouter,tags=["NHA SAN XUAT"],prefix='/NSX')
app.include_router(MHRouter,tags=["MAT HANG"],prefix='/MH')
app.include_router(KHRouter,tags=["KHACH HANG"],prefix='/KH')
app.include_router(CTDHRouter,tags=["CHI TIET DON HANG"],prefix='/CTDH')
app.include_router(NVRouter,tags=["NHAN VIEN"],prefix='/NV')
#  python -m venv D:\be-mongo\venv 