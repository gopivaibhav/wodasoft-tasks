from django.test import TestCase
from .models import Article


# Create your tests here.
class AticleTest(TestCase):

    def create_article(self, title={"en":"12", "fr":"12", "ru":"12"}, default="en"):
        return Article.objects.create(title=title, default=default)

    def test_article_creation(self):
        arti = self.create_article()
        # print("Checking")
        self.assertTrue(isinstance(arti, Article))
        self.assertEqual(arti.__str__(), arti.title['en'])
