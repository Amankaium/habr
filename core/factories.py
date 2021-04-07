import factory
from .models import Article

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
