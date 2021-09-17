from churrasco.models import Churrasco
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Churrasco



class HomeView(ListView):
    model= Churrasco
    template_name = 'churrasco.html'


#def CategoryView(request, cats): 
 #   category_posts = Churrasco.objects.all()
  #  return render(request, 'categories.html', {'cats': cats, 'category_posts':category_posts})   


class ArticleDetailView(DetailView):
    model = Churrasco
    template_name = 'article_details.html'




def index(request):
    return render(request, 'index.html')



def churrasco(request):
    return render(request, 'churrasco.html')