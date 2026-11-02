# 静态服务器
from pathlib import Path
# 项目根目录
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
#  SET 集合 不重复元素
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png",".pdf",".docx"}
ALLOWED_MINE_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
}

MAX_FILE_SIZE = 1024*1024*10 # 10MB