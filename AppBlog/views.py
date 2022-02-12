from django.shortcuts import render
from .models import *

from django.core.paginator import Paginator #gestoe de paginacion

# Create your views here.

def Home (request):
    
    posts = Post.objects.filter(estado=True)
    categorias = Categoria.objects.all()
    
    paginator= Paginator(posts,2)
    
    page = request.GET.get('page')
    
    posts = paginator.get_page(page)
    
    return render(request,'index.html',{'posts': posts,'categorias':categorias})

def Posteo (request,slug_post):
    
    posteo = Post.objects.get (slug=slug_post)
    
    categorias = Categoria.objects.all()
    
    return render(request,'post.html',{'posteo':posteo,'categorias':categorias})

def Posteos (request,categoria_nombre):
    
    categoria = Categoria.objects.get(nombre = categoria_nombre)
    
    categorias = Categoria.objects.all()
    
    posts= Post.objects.filter(categoria=categoria)
    
    return render(request,'categoria.html',{'posts':posts,'categorias':categorias,'categoria':categoria})

def Contacto (request):
    return render(request,'contacto.html')