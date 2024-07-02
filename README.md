# Task Tracker FastAPI

## Описание

Таск трекер созданный сообществом FS.\
Стек: FastAPI, SQLAlchemy+Alembic.\

## Установка

Следуйте инструкциям ниже для установки и запуска проекта локально.

### Шаги установки

1. Клонируйте репозиторий

   ```bash
   git clone https://github.com/fellowsheet/tracker-team-1.git
   cd tracker-team-1
   ```

2. Создайте и активируйте виртуальное окружение
    - Windows
       ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - Linux and MacOS
       ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. Установите зависимости

   ```bash
   pip install -r requirements.txt
   ```

4. Запуск локального сервера
    ```bash
   cd backend/
   uvicorn main:app --reload
   ```

## Использование

Откройте браузер и перейдите по адресу [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/) для доступа к
документации API.
