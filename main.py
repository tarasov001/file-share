import os
import uuid
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

VERSION = "1.0.1"
app = FastAPI(title="File Share", version=VERSION)

# Директории
BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
TEMPLATES_DIR = BASE_DIR / "templates"

# Создаём директорию для загрузок, если не существует
UPLOAD_DIR.mkdir(exist_ok=True)

# Шаблоны
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Главная страница с формой загрузки."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Загрузка файла и возврат ссылки."""
    # Генерируем уникальный ID для файла
    file_id = str(uuid.uuid4())
    
    # Сохраняем файл
    file_path = UPLOAD_DIR / file_id
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Формируем ссылку
    host = "http://localhost:8000"
    download_url = f"{host}/files/{file_id}"
    
    return {
        "file_id": file_id,
        "filename": file.filename,
        "download_url": download_url
    }


@app.get("/files/{file_id}")
async def download_file(file_id: str):
    """Скачивание файла по ID."""
    file_path = UPLOAD_DIR / file_id

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Файл не найден")

    return FileResponse(
        path=file_path,
        filename=file_id,
        media_type="application/octet-stream"
    )


@app.get("/version")
async def get_version():
    """Версия приложения."""
    return {"version": VERSION}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
