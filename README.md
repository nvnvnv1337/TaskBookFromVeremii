# TASKBOOK

# Технологии в проекте:
    Docker,
    Python,
    Django,
    Postgres,
    Redis,
    Django Rest Framework (DRF)

# Требования проекту для запуска:
    Наличия работующего Docker и Docker-Compose и Git



# Переменные окружения:
    DB_NAME=Имя бд
    DB_USER=Пользователь бд
    DB_PASSWORD=13371324
    DJANGO_SECRET_TOKEN=Секретный ключ джанго
    EMAIL_APP_PASSWORD=Пароль от твоего приложения
    EMAIL_HOST=Сервис для отправки
    EMAIL_HOST_USER=Почта для приложения
    EMAIL_PORT=Порт 
    DEFAULT_FROM_EMAIL=От кого будет сообщение в письме

# Как запустить (линукс/MacOs):
    1) Клонировать проект:
        git clone 
        cd 
    2) Создать файл с переменными окружения и вставить туда данные:
        touch .env 
        nano .env
    3) Запустить контейнеры а также применить миграции и создать супер пользователя:
        docker-compose up -d
        docker-compose exec web python manage.py migrate
        docker-compose exec web python manage.py createsuperuser
    4) Для остановки:
        docker-compose down

# Пути приложения:
    http://localhost:8000/ - главная страница
    http://localhost:8000/admin - админка
    http://localhost:8000/api/ - api 
