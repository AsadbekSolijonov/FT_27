from django.urls import path, include
from blog_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('accounts/', include('django.contrib.auth.urls'))
]
