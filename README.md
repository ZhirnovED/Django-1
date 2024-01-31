# Django-1

## Используйте базовый образ с поддержкой Python
FROM Python 3.11.5 

## Установите рабочую директорию в /
WORKDIR /

## Скопируйте файл requirements.txt в рабочую директорию контейнера
COPY requirements.txt /

## Установите зависимости проекта с помощью pip
RUN pip install -r requirements.txt

## Скопируйте все файлы проекта в рабочую директорию контейнера
COPY . /

## Запустите команду для выполнения миграций базы данных
python manage.py makemigrations main
python manage.py migrate

## Запустите сервер разработки Django при запуске контейнера
CMD ["python", "manage.py"]