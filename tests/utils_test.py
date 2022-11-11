import pytest
import utils


#Класс для тестирования функций
class TestUtils:

    posts_key = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    user_exceptions = [("mark", ValueError), ("Fedor", ValueError), (111, ValueError)]
    search_by_pk = [(1, 1), (2, 2), (5, 5)]
    pk_exceptions = [(0, ValueError), (25, ValueError), (-1, ValueError)]
    post_comment = [(1, 1), (2, 2), (3, 3)]
    post_comment_exceptions = [(0, ValueError), (-1, ValueError), ("a", ValueError)]
    search_in_posts = [("sdfjsdfgj", ValueError), ("+++++++++++sdjks", ValueError) ]

    def test_type_load_all_posts(self):
        """
        Тестирование загрузки данных из списка постов
        :return:
        """
        assert type(utils.get_posts_all()) == list, f"Ошибка типа полученных данных"

    def test_load_all_posts(self):
        """
        Тестирование корректности получаемых данных постов
        :return:
        """
        test_list = utils.get_posts_all()
        for test_post in test_list:
            assert set(test_post.keys()) == self.posts_key, f"Ошибка для ключей"

    @pytest.mark.parametrize("search_name, user_name", [("leo", "leo"), ("johnny", "johnny"), ("hank", "hank")])
    def test_get_posts_by_user(self, search_name, user_name):
        """
        Тестирование корректности получаемых данных постов конкретного пользователя
        :param search_name:
        :param user_name:
        :return:
        """
        assert utils.get_posts_by_user(search_name)[0]["poster_name"] == user_name, f"Ошибка для пользователя {search_name}"

    @pytest.mark.parametrize("search_name, exception", user_exceptions)
    def test_get_posts_by_user_exceptions(self, search_name, exception):
        """
        Тестирование возможных ошибок при получении постов пользователя
        :param search_name:
        :param exception:
        :return:
        """
        with pytest.raises(exception):
            utils.get_posts_by_user(search_name)

    @pytest.mark.parametrize("search_pk, pk", search_by_pk)
    def test_get_post_by_pk(self, search_pk, pk):
        """
        Тестирование корректности получаемых данных конкретного поста
        :param search_pk:
        :param pk:
        :return:
        """
        assert utils.get_post_by_pk(search_pk)["pk"] == pk, f"Ошибка по посту  {search_pk}"

    @pytest.mark.parametrize("search_pk, exception", pk_exceptions)
    def test_get_post_by_pk_exceptions(self, search_pk, exception):
        """
        Тестирование возможных ошибок при получении конкретного поста
        :param search_pk:
        :param exception:
        :return:
        """
        with pytest.raises(exception):
            utils.get_post_by_pk(search_pk)

    @pytest.mark.parametrize("search_post_comment, post_comment", post_comment)
    def test_get_comments_by_post_id(self, search_post_comment, post_comment):
        """
        Тестирование корректности получаемых данных комментариев для поста
        :param search_post_comment:
        :param post_comment:
        :return:
        """
        assert utils.get_comments_by_post_id(search_post_comment)[0]["post_id"] == post_comment, f"Ошибка для поста {search_post_comment}"

    @pytest.mark.parametrize("search_post_comment, exception", post_comment_exceptions)
    def test_get_comments_by_post_id_exceptions(self, search_post_comment, exception):
        """
        Тестирование возможных ошибок при получении комментариев
        :param search_post_comment:
        :param exception:
        :return:
        """
        with pytest.raises(exception):
            utils.get_comments_by_post_id(search_post_comment)

    @pytest.mark.parametrize("search, exception", search_in_posts)
    def test_search_for_posts(self, search, exception):
        """
        Тестирование возможных ошибок при получении постов по содержанию
        :param search:
        :param exception:
        :return:
        """
        with pytest.raises(exception):
            utils.search_for_posts(search)

