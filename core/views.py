from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Article, Author


User = get_user_model()


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('articles')
                
    return render(request, 'sign_in.html')


def sign_out(request):
    logout(request)
    return redirect(sign_in)


def registration(request):
    if request.method == "GET":
        return render(request, 'registration.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:
            return render(request, 'registration.html', {'message': 'Пароли не совпадают!'})
        elif User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {'message': 'Логин уже используется'})
        else:
            User.objects.create_user(
                username=username,
                password=password_1,
            )
            return redirect(sign_in)


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

def author_page(request, pk):
    author = Author.objects.get(pk=pk)
    context = {
        "author": author,
        "user": author.user,
    }
    return render(request, "author.html", context)

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    if request.user.is_authenticated:
        article.readers.add(request.user)
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
    if not request.user == article.author.user:
        return HttpResponse('У вас нет прав на это действие')

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "update.html", {"article": article})


@login_required(login_url='/sign-in/')
def add_article(request):
    if request.method == "GET":
        return render(request, "add.html")
    elif request.method == "POST":
        form = request.POST
        title = form.get("title")
        text = form.get("text")
        picture = request.FILES.get('picture')

        # new_article = Article(title=title, text=text)
        # new_article.save()

        new_article = Article()
        new_article.title = title
        new_article.text = text
        new_article.picture = picture
        user = request.user

        if not Author.objects.filter(user=user).exists():
            author = Author(user=user, nik=user.username)
            author.save()
            
        author = user.author
        new_article.author = author
        new_article.save()
        return redirect(article_page, new_article.pk)


def is_author(user):
    if not user.is_authenticated:
        return False
    return Author.objects.filter(user=user).exists()


@user_passes_test(is_author)
def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return HttpResponse("Статья удалена")


@permission_required('core.change_article')
def hide_article(request, id):
    article = Article.objects.get(id=id)
    article.is_active = False
    article.save()
    return redirect(articles)


def search(request):
    word = request.GET.get("word")
    articles = Article.objects.filter(
        Q(title__icontains=word) | Q(text__icontains=word),
        is_active=True
    )
    return render(request, "articles.html", {"articles": articles})

def top(request):
    articles = Article.objects.filter(is_active=True).order_by("-views", "pk")[:3]
    return render(request, "articles.html", {"articles": articles})


class TestView:
    def test_1(self):
        return HttpResponse('test succeed!')
