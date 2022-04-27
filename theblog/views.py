from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

#def home(request):
    #return render(request, 'home.html', {})
    
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Article_details.html'
    