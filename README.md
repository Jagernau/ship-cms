# Корабельная CMS
Нужна для сопоставлений и вывода файлов и информации

# Установка всего необходимого
версия сырая и находится в дебаге, в дальнейшем возможно всё приложение будет запускаться через docker compose.


## И так готовим самое необходимое
1. Скачать репозиторий `git clone https://github.com/jagernau/ship-cms.git`
2. Установить docker на Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
3. Установить docker-compose: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04

## Запуск бд Postgres в докере
База собранна в коробочке.
1. Заходим в папку ship-cms `cd ship-cms`
2. Используем команду `docker-compose up -d` либо `sudo docker-compose up -d` для запуска бд. Всё про контейнер прописанно в файле `docker-compose.yml`
3. Вуаля Бд на 5222 вроде порту

## Жесть щас  будет (запускаем проект) вручную
Так как времени писать контейнер под приложение нет. Будем запускать в ручную
1. Нужен Python >= 3.10
2. Нужен pip
3. Устанавливаем библиотеку virtualenv `pip install virtualenv`
4. Создаём песочницу: `python3.10 -m virtual env `
5. Входим в песочницу `source env/bin/activate`
6. Добавляем в песочницу нужные библиотеки `pip install -r requirements.txt`
7. Накатываем миграции `python3.10 manage.py migrate`
8. Создаём админа `python3.10 manage.py createsuperuser`
9. Запускаем проект `python3.10 manage.py runserver 0.0.0.0:8000`
10. Админка по ссылке: `http://localhost:8000/admin/`

## Запуск приложения Через docker-compose лёгкий вариант
Я запилил.
Просто запусти `sudo docker-compose up --build`
Если вылетит с ошибкой значит приложение не хочет конектится к постгрес контейнеру и либо у тебя порт 5432 занят либо local хост нужно менять в settings в Django
А так если мелочи порешать то пашет и можно разрабатывать.

Приложение будет работать на http://localhost:8000
В дальнейшем если всё норм, можно запускать `sudo docker-compose up --build -d`
