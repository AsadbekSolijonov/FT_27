from django.urls import path
from blog_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.blog_detail, name='blog_detail'),
]
