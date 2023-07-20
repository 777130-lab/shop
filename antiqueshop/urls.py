from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store import views as store_views
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store_views.home, name='home'),
    path('store/contact/', store_views.contact, name='contact'),
    path('store/stores/', store_views.stores, name='stores'),
    path('articles/', article_views.articles, name='articles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
