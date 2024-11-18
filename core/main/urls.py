from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='qax'),
    path('mayleq/<int:mayla_id>',views.mayla,name='mayla'),
    path('poxoc/<int:poxoc_id>/',views.poxoc,name='poxoc'),
]