from django.test import TestCase

# Create your tests here.
def create_article(name, description, price, department):
    """ Creates a new article """
    return Article.objects.create(name=name, description=description, price=price, department=department)


"""class ArticleCreationTest(TestCase):
    def test_
"""
