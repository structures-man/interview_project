from fastapi import HTTPException, status, UploadFile
from pathlib import Path
from ..config import ALLOWED_EXTENSIONS, ALLOWED_MINE_TYPES, MAX_FILE_SIZE, UPLOAD_DIR
# python 内置模块 用来生成全局唯一的ID
import uuid

def validate_file(file: UploadFile) -> None:
    # raise
    if not file.filename:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "File name is required"
        )
    # a.jpg -> .jpg
    # 拿到文件后缀名 并转换为小写

    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"不支持的文件类型： {ext}"
        )
    if file.content_type not in ALLOWED_MINE_TYPES:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"不支持的文件类型： {file.content_type}"
        )
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail = f"文件大小不能超过 {MAX_FILE_SIZE} 字节"
        )
    
        
# 保存文件到服务器指定目录
def save_file(file: UploadFile) -> dict :
    # 自动创建父目录 目录已经创建 不会报错
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    original_name = Path(file.filename).name
    unique_name = f"{Path(original_name).stem}_{uuid.uuid4().hex}{Path(original_name).suffix}"
    target_path = UPLOAD_DIR / unique_name
    # 创建一个写入流 write binary
    # with 语句 会自动关闭文件  
    with target_path.open("wb") as buffer:
        # 每次读取 1MB 
        # 赋值 判断 是否为空
        while chunk := file.file.read(1024 * 1024):
            buffer.write(chunk)
    return {
        "original_name": original_name,
        "saved_name": unique_name,
        "size": target_path.stat().st_size
    }
