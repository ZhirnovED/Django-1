# Django-1

## Версия Python
Python 3.11.5 

## Установка зависимостей проекта с помощью pip
RUN pip install -r requirements.txt

## Запуск миграции
python manage.py makemigrations main
python manage.py migrate

## Запуск сервера 
python manage.py runserver