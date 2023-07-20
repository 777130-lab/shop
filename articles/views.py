from .models import Article
from django.shortcuts import render

def create_articles():
    # Создание и сохранение статей
    article1 = Article(title="История антиквариата", content="Здесь содержится информация об истории антиквариата...")
    article1.save()

    article2 = Article(title="Советы по выбору антикварных предметов", content="В этой статье даем советы по выбору антикварных предметов...")
    article2.save()

    article3 = Article(title="Топ 10 самых ценных антикварных предметов", content="Ознакомьтесь с топом самых ценных антикварных предметов...")
    article3.save()


def articles(request):
    create_articles()  # Вызов функции для создания статей
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})
