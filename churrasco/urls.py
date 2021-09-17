
from churrasco.models import Category
from django.conf.urls import include
from django.urls import path
from . import views
from . views import HomeView, ArticleDetailView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)