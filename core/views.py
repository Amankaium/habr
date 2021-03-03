from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.
def homepage(request):
    return render(request, "index.html")
    # return HttpResponse("<h2>Hello world!</h2>")


def first_article(request):
    article = Article.objects.get(id=1)
    return render(
        request,
        "article_page.html", 
        {"article": article}    
    )