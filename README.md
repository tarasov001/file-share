# File Share 📁

Простой веб-сервис для обмена файлами по ссылке. Загрузи файл и получи ссылку для скачивания.

## Возможности

- ✅ Загрузка файлов через веб-интерфейс
- ✅ Генерация уникальной ссылки для каждого файла
- ✅ Скачивание файлов по прямой ссылке
- ✅ Приятный UI на Bootstrap 5

## Быстрый старт

### Локальный запуск

```bash
# Установка зависимостей
pip3 install -r requirements.txt

# Запуск сервера
python3 main.py
```

Открой http://localhost:8000 в браузере.

### Docker

```bash
# Сборка и запуск
docker-compose up -d

# Остановка
docker-compose down
```

## API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/` | Веб-интерфейс |
| POST | `/upload` | Загрузка файла |
| GET | `/files/{file_id}` | Скачивание файла |

### Пример загрузки через curl

```bash
curl -F "file=@document.pdf" http://localhost:8000/upload
```

Ответ:
```json
{
  "file_id": "550e8400-e29b-41d4-a716-446655440000",
  "filename": "document.pdf",
  "download_url": "http://localhost:8000/files/550e8400-e29b-41d4-a716-446655440000"
}
```

## Деплой на VPS

### 1. Подготовка сервера

```bash
# Установка Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### 2. Клонирование проекта

```bash
git clone <your-repo-url>
cd file-share
```

### 3. Запуск

```bash
docker-compose up -d
```

### 4. Настройка nginx (опционально)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Структура проекта

```
file-share/
├── main.py              # FastAPI сервер
├── requirements.txt     # Python зависимости
├── Dockerfile           # Docker образ
├── docker-compose.yml   # Docker Compose
├── .gitignore
├── README.md
├── templates/
│   └── index.html       # Веб-интерфейс
└── uploads/             # Загруженные файлы
```

## Технологии

- **Backend:** Python 3, FastAPI, uvicorn
- **Frontend:** HTML5, Bootstrap 5
- **Storage:** Локальная файловая система

## Лицензия

MIT
