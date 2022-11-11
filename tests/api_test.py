import app


#Класс тестрования для api
class TestApi:
    posts_key = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_api_posts_page(self):
        """
        Тестирование эндпоинта /api/posts
        :return:
        """
        test_client = app.app.test_client()
        responce = test_client.get("/api/posts")
        all_posts = responce.get_json()
        assert responce.status_code == 200, f"Ошибка статус-кода"
        for post in all_posts:
            assert set(post.keys()) == self.posts_key, f"Ошибка ключей"

    def test_api_posts_page_pk(self):
        """
        Тестирование эндпоинта /api/posts/"номер поста"
        :return:
        """
        test_client = app.app.test_client()
        responce = test_client.get("/api/posts/1")
        post = responce.get_json()
        assert responce.status_code == 200, f"Ошибка статус-кода"
        assert set(post.keys()) == self.posts_key, f"Ошибка ключей"
