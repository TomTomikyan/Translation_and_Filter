from django.contrib import admin
from .models import Qaxaq,Mayla,Poxoc

# Register your models here.

class QaxaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img')  
    search_fields = ('name',)
    list_filter = ('name',)  
    ordering = ('id',)  

class MaylaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'Qaxaq')  
    search_fields = ('name',)
    list_filter = ('name',)  
    ordering = ('id',)

class PoxocAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'Mayla')  
    search_fields = ('name',)
    list_filter = ('name',)  
    ordering = ('id',)

admin.site.register(Qaxaq,QaxaqAdmin)
admin.site.register(Mayla,MaylaAdmin)
admin.site.register(Poxoc,PoxocAdmin)
