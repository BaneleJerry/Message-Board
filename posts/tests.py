from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = 'Hello, this is a test')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'Hello, this is a test')
    
    def test_urls_exits_at_correct_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage(self): # new
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Hello, this is a test")
