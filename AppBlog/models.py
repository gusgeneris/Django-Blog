from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100 )
    estado = models.BooleanField('Categoria Activada/Categoria NO Activada', default = True)#nombre que aparecera en el panel de administracion
    imagen = models.URLField('URL de Imagen', max_length=255,null=True, blank=True) 
    created = models.DateField('Fecha Creacion' , auto_now_add=True)
    updated = models.DateField('Fecha de Modificacion' , auto_now=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre
    

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de Autor',max_length=250)
    apellido = models.CharField('Apellido de Autor', max_length=250)
    facebook = models.CharField('Facebook de Autor', max_length=250, blank=True, null=True)
    twitter = models.CharField('Twitter de Autor', max_length=250, blank=True, null=True)
    instagram = models.CharField('Instagram de Autor', max_length=250, blank=True, null=True)
    email = models.EmailField('Email de Autor', max_length=250)
    estado = models.BooleanField('Autor Activo/Autor NO Activo', default=True)
    created= models.DateField('Fecha Creacion', auto_now_add=True)
    updated = models.DateField('Fecha de Modificacion', auto_now=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nombre 
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=90)
    slug = models.CharField('Slug',max_length=100)
    descripcion = models.CharField('Descripcion',max_length=120)
    contenido = RichTextField()
    imagen = models.URLField('URL de Imagen', max_length=255) #utilizamos urlField ya que utilizaremos heroku en su vercion gratuita
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicadp', default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo

