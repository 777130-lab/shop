from django.shortcuts import render
from .models import Store

def home(request):
    return render(request, 'store/home.html')

def contact(request):
    return render(request, 'store/contact.html')

def stores(request):
    stores = Store.objects.all()
    return render(request, 'store/stores.html', {'stores': stores})

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})
