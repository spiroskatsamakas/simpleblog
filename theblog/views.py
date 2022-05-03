from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm, EditForm, Category
from django.urls import reverse_lazy, reverse
import folium
import requests

# Create your views here.

#def home(request):
    #return render(request, 'home.html', {})
    

class MarkersMapView(TemplateView):
        #"""Markers map view."""
        
    template_name = 'map.html'    
    
def map(request):
    url = ("https://github.com/spiroskatsamakas/foliumemample01/raw/main/")
    
    Map = f"{url}/greece01.json"

    m = folium.Map(
    location=[29.1759, 39.6016],
    tiles="cartodbpositron",
    zoom_start=5,)
    
    folium.GeoJson(Map, name="geojson").add_to(m)
    geojson = folium.GeoJson(Map)
    popup = folium.Popup('name')
    popup.add_to(geojson)
    geojson.add_to(m)

    folium.LayerControl().add_to(m)
    
    m = m._repr_html_()
    
    context = {
        'm': m,
    }
    return render(request, 'map.html', context)



 
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-published_date']

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})



def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.replace('-', ' ').title(), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html' 

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = ('title', 'body')
    
class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = ('title', 'body')

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']
    
class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')    
