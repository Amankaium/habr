from django.shortcuts import render, HttpResponse, redirect
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

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    return render(
        request,
        "article.html",
        {"article": article}
    )


def about(request):
    return render(request, "about.html")


def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "update.html", {"article": article})