from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.file_service import validate_file, save_file
router = APIRouter(prefix="/api", tags=["upload"])

# File(...) 来自 MultipartForm 必传
# UploadFile 取文件
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("--------------------")
    validate_file(file)
    result = save_file(file)
    return {
        "code": 0,
        "message": "上传成功",
        "data": result
    }
    # 保存文件到服务器
