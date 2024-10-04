# Тестовое задание на FastApi для Workmate

Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:
```
uvicorn app.main:app --reload
```
Для запуска всех сервисов (БД, FastAPI) необходимо использовать файл docker-compose.yml и команды:
```
docker compose build
docker compose up
```
Документация в формате Swagger доступна по адресу:
```
http://127.0.0.1:8000/docs
```