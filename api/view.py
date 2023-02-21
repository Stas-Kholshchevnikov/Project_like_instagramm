from flask import Blueprint, jsonify
import utils
import logging

#Объявление blueprint
api_blueprint = Blueprint("api_blueprint", __name__)

#Объявление логера для записи запросов api
logging.basicConfig(level=logging.INFO)
logger_api = logging.getLogger("api_loger")
file_handler = logging.FileHandler(filename=".\logs\api.log", encoding="UTF-8")
format_logger = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(format_logger)
logger_api.addHandler(file_handler)


@api_blueprint.route("/api/posts")
def api_posts_page():
    """
    Функция отображения эндпоинта /api/posts
    :return:
    """
    logger_api.info("Запрос/api/posts")
    return jsonify(utils.get_posts_all())


@api_blueprint.route("/api/posts/<int:pk>")
def api_post_pk_page(pk):
    """
    Функция отображения эндпоинта /api/posts/"номер записи"
    :param pk:
    :return:
    """
    logger_api.info(f"Запрос/api/posts/{pk}")
    return jsonify(utils.get_post_by_pk(pk))
