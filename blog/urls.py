from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.index,name='index'),
    path('blog/blogpost/<int:id>',views.blogpost,name='blogpost'),
   # path('post/',views.blog,name='blog'),
]
