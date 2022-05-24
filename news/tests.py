from django.test import TestCase
from .models import Editor,Article,tags


# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.john = Editor(first_name='John', last_name='Njau', email='john@gmail.com')
        
    # tesing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.john,Editor))
        
    #test save method
    def test_save_method(self):
        self.john.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0)
        
class ArticleTestClass(TestCase):
    def setUp(self):
        self.article = Article(title="The good day", post="Oh, this is a good day", pub_date="23/5/2022")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.article, Article))
        
    def test_save_method(self):
        self.article.save_article()
        articles = Article.objects.all()
        self.assertTrue(len(articles)> 0)
        
#running tests
# python3 manage.py test news
# ./manage.py tests