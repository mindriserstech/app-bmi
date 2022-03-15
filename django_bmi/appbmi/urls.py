# our custom application urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name='user.index'),
    path('login/', views.user_login, name='user.login'),
    path('register/', views.user_create, name='user.create')
]