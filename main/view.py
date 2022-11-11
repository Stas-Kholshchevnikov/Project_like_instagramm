from flask import Blueprint, render_template, request
import utils

#Создание btueprint
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    """
    Обработка эндпоинта главной страницы
    :return:
    """
    posts = utils.get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("posts/<int:pk>")
def post_pf_page(pk):
    """
    Обработка эндпоинта поста по его номеру
    :param pk:
    :return:
    """
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(post["pk"])
    count_comments = len(comments)
    return render_template("post.html", post=post, comments=comments, count_comments=count_comments)


@main_blueprint.route("search")
def search_page():
    """
    Обработка эндпоинта поиска постов по содержанию
    :return:
    """
    user_search = request.args['searching']
    search_list = utils.search_for_posts(user_search)
    counts_items = len(search_list)
    return render_template("search.html", search_list=search_list, counts_items=counts_items)


@main_blueprint.route("user/<user_name>")
def user_page(user_name):
    """
    Обработка эндпоинта поиска постов конкретного пользователя
    :param user_name:
    :return:
    """
    user_posts = utils.get_posts_by_user(user_name)
    name = user_name.title()
    return render_template("user-feed.html", user_posts=user_posts, name=name)
