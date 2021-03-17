from django.shortcuts import render, HttpResponse
from .models import Article, Author

def articles(request):
    articles = Article.objects.all()
    return render(
        request,
        "articles.html",
        {"articles": articles}
    )

def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors.html",
        {"authors": authors}
    )

def article(request, id):
    article = Article.objects.get(id=id)
    return render(
        request,
        "article.html",
        {"article": article}
    )