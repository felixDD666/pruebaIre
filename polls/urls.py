from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('cv1', views.cvNaza, name='cv1'),
]