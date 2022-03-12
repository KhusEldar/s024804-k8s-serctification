Образ хранится в Docker Registry по адресу 109.120.183.68:5000 с названием rest_api. (Каталог https://109.120.183.68:5000/v2/_catalog).

Подключена база данных PostgreSQL-4767, доступная по IP-адресу 146.185.209.122

Ссылка на работающее приложение http://109.120.183.245/app_api/users
-------------------------------------------------------------
Не запускалось приложение в k8s. 
Ошибка была в файле wsgi.py.
Было:
from config import Config

config = Config()

def app():
    app.run(debug=True, host="0.0.0.0", port=config.db_port)

Исправлено:
from app import app as application
app = application

Исправленное приложение в папке users_rest_api.