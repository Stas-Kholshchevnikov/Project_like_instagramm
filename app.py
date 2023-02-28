from flask import Flask
from main.view import main_blueprint
from api.view import api_blueprint

#Создание объекта типа Flask
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

#Регистрация блюпринтов
app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    """
    Обработчик ошибок 404
    :param e:
    :return:
    """
    return f'Станица не найдена: "{e}"'


@app.errorhandler(500)
def server_error(e):
    """
    Обработчик ошибок 500
    :param e:
    :return:
    """
    return f'Ошибка обработки сервера: "{e}"'


@app.errorhandler(FileNotFoundError)
def file_not_found(e):
    """
    Обработчик ошибок FileNotFound
    :param e:
    :return:
    """
    return f'Файл json для загрузки данных не найден - {e}'


@app.errorhandler(ValueError)
def value_error(e):
    """
    Обработчик ошибок ValueError
    :param e:
    :return:
    """
    return f'Ошибка данных для обработки - {e}'


if __name__ == "__main__":
    #Запуск сервера
    app.run(host="0.0.0.0", port=5000)
