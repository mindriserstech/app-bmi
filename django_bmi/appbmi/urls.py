# our custom application urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name='user.index'),
    path('profile/', views.user_profile, name='user.profile'),
    path('login/', views.user_login, name='user.login'),
    path('logout/', views.user_logout, name='user.logout'),
    path('register/', views.user_create, name='user.create'),
    path('update/', views.user_update, name='user.update'),
    path('send-email/', views.sendemail, name='user.email'),
    path('profile-upload/', views.user_profile_upload, name='user.upload'),

    # for bmi
    path('bmi/', views.bmi_index, name="bmi.index"),
    path('bmi/create', views.bmi_create, name="bmi.create"),
    path('bmi/store', views.bmi_store, name="bmi.store"),
    path('bmi/edit/<int:bmi_id>', views.bmi_edit, name="bmi.edit"),
    path('bmi/show/<int:bmi_id>', views.bmi_show, name="bmi.show"),
    path('bmi/update', views.bmi_update, name="bmi.update"),
    path('bmi/delete/<int:bmi_id>', views.bmi_delete, name="bmi.delete"),
]