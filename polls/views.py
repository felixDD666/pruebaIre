from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'vistas/index.html')



def blog(request):
	posts = Post.objects.order_by("-Fecha_Creacion")
	numPost = Post.objects.count()-3;
	return render(request,'vistas/blog.html',{
	    "posts":posts,
	    "numPost": numPost
	    })


def cvNaza(request):
    return render(request, 'vistas/cvNaza.html')