from fastapi import FastAPI 
from .routers import upload
# cors 跨域中间件
# from fastapi.middleware.cors import CORSMiddleware
# from .routers import upload

app = FastAPI(title="File Upload API")

@app.get("/")
def root(): 
    return {"message": "File Upload API", "docs": "/docs"}


app.include_router(upload.router)
