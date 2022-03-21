# our custom application urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name='user.index'),
    path('profile/', views.user_profile, name='user.profile'),
    path('login/', views.user_login, name='user.login'),
    path('logout/', views.user_logout, name='user.logout'),
    path('register/', views.user_create, name='user.create'),
    path('update/', views.user_update, name='user.update')
]