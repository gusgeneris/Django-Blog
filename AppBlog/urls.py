from unicodedata import name
from django.urls import path
from .views import *

urlpatterns=[
    path('generisdjangoblog.netlify.app/',Home, name='index'),
    path('post/<slug_post>',Posteo, name='post'),
    path('categoria/<categoria_nombre>',Posteos, name='categoria'),
    path('contacto/',Contacto, name='contacto'),
    
]