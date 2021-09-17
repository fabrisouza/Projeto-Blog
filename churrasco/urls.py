from django.urls import path

from . import views
import churrasco

urlpatterns = [
    path('', views.index, name='index'),
    path('churrasco', views.churrasco, name='churrasco')
]