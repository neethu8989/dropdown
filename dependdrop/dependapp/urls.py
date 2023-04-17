from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('templates/register', views.register, name="register"),
    path('templates/login', views.loginpage, name="login"),
    path('templates/formpage', views.person_create_view, name='formpage'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    # path('template/formpage', views.Userform, name="Userform"),

    path('templates/logout', views.logout, name="logout"),

     # AJAX
]