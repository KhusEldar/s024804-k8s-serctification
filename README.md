# s024804-k8s-serctification

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
-------------------------------------------------------------

Манифесты разложены по папкам в соответсвии с пунктами содержания сертификации:

1.1. Информация о сертификации
1.2. Создать кластер в VKCS
1.3. Подготовить манифесты
1.4. Подключить Managed PostgreSQL
1.5. Написать Helm Chart
1.6. Запустить CronJob
1.7. Запустить StatefulSet