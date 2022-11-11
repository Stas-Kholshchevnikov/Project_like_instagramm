import os
import json


def load_all_post():
    """
    Загрузка информации о постах из файла
    :return:
    """
    try:
        with open(os.path.join("data", "posts.json"), "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Файл 'posts.json' не найден")


def load_all_comments():
    """
    Загрузка информации о комментариях к постам из файла
    :return:
    """
    try:
        with open(os.path.join("data", "comments.json"), "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Файл 'comments.json' не найден'")


def get_posts_all():
    """
    Получение полного списка постов
    :return:
    """
    all_posts = load_all_post()
    return all_posts


def get_posts_by_user(user_name):
    """
    Получение постов конкретного пользователя
    :param user_name:
    :return:
    """
    post_user_name = []
    all_posts = load_all_post()
    for post in all_posts:
        if post["poster_name"].lower() == str(user_name).lower():
            post_user_name.append(post)
    if len(post_user_name) == 0:
        raise ValueError("Ошибка загрузки постов по пользователю")
    else:
        return post_user_name


def get_comments_by_post_id(post_id):
    """
    Получение комментариев к конкретному посту
    :param post_id:
    :return:
    """
    all_comments = load_all_comments()
    comments_post = []
    for comment in all_comments:
        if comment["post_id"] == post_id:
            comments_post.append(comment)
    if len(comments_post) == 0:
        raise ValueError("Ошибка загрузки поста или комментариев к посту")
    else:
        return comments_post


def search_for_posts(query):
    """
    Получение постов с поиском по содержанию
    :param query:
    :return:
    """
    all_posts = load_all_post()
    search_posts = []
    for post in all_posts:
        if str(query).lower() in post["content"].lower():
            search_posts.append(post)
    if len(search_posts) == 0:
        raise ValueError("Ошибка загрузки постов по содержанию")
    else:
        return search_posts


def get_post_by_pk(pk):
    """
    ПОлучение поста по его номеру
    :param pk:
    :return:
    """
    all_posts = load_all_post()
    post_pk = {}
    for post in all_posts:
        if post["pk"] == pk:
            post_pk = post
    if post_pk:
        return post_pk
    else:
        raise ValueError("Ошибка загрузки постов по номеру")
