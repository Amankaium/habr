from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from .models import Article, Author

def articles(request):
    articles = Article.objects.filter(is_active=True)
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


def add_article(request):
    if request.method == "GET":
        return render(request, "add.html")
    elif request.method == "POST":
        form = request.POST
        title = form.get("title")
        text = form.get("text")

        # new_article = Article(title=title, text=text)
        # new_article.save()

        new_article = Article()
        new_article.title = title
        new_article.text = text
        user = request.user

        if not Author.objects.filter(user=user).exists():
            author = Author(user=user, nik=user.username)
            author.save()
            
        author = user.author
        new_article.author = author
        new_article.save()
        return redirect(article_page, new_article.pk)


def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return HttpResponse("Статья удалена")

def hide_article(request, id):
    article = Article.objects.get(id=id)
    article.is_active = False
    article.save()
    return redirect(articles)


def search(request):
    # POST GET
    word = request.GET.get("word")
    articles = Article.objects.filter(
        Q(title__icontains=word) | Q(text__icontains=word),
        is_active=True
    )
    return render(request, "articles.html", {"articles": articles})
