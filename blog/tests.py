from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test", email="test@test.test", password="test"
        )

        cls.post = Post.objects.create(
            title="test",
            body="test core",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "test")
        self.assertEqual(self.post.body, "test core")
        self.assertEqual(self.post.author.username, "test")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test core")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        no_response = self.client.get("/post/500/")
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test core")
        self.assertTemplateUsed(response, "post_detail.html")