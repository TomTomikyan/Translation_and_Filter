from django.shortcuts import render
from .models import Qaxaq, Mayla, Poxoc

# Create your views here.

def index(request):
    qaxaq_list = Qaxaq.objects.all()
    return render(request,'index.html',context={
        'qaxaq_list':qaxaq_list,
    })

def mayla(request,mayla_id):
    mayla_list = Mayla.objects.filter(Qaxaq_id = mayla_id)
    return render(request,'mayla.html',context={
        'mayla_list':mayla_list,
    })

def poxoc(request,poxoc_id):
    poxoc_list = Poxoc.objects.filter(Mayla_id = poxoc_id)
    return render(request,'poxoc.html',context={
        'poxoc_list':poxoc_list,
    })