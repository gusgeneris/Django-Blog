from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class CategoriaResources(resources.ModelResource):
    class Meta:
        model = Categoria
    

class AutorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #se especifica que estos campos pertenecientes al modelo son solo de lectura
    list_display = ('nombre', 'apellido', 'estado','email',)
    search_fields = ('nomre', 'apellido',)
    
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre','estado','created',)
    resources_class = CategoriaResources
    

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo','descripcion','created',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)