from django.contrib import admin
from django.urls import include, path

from myapp import views
urlpatterns = [
    # path('',views.login),
    path('',views.home),
    path('course/', views.course, name='course'),  # URL without id parameter
    path('teachers/', views.teachers, name='teachers'),  # URL without id parameter
    path('contact/', views.contact, name='contact'),  # URL without id parameter
    path('about/', views.about, name='about'),  # URL without id parameter


    path('login/',views.login),
    path('new/',views.new),
    path('home/<id>/',views.home),
    path('course/<id>/',views.course),
    path('teachers/<id>/',views.teachers),
    path('t_profile/<id>/',views.t_profile),
    path('contact/<id>/',views.contact),
    path('about/<id>/',views.about),
    path('t_playlist/<id>/',views.t_playlist),
    path('purchase/<id>/',views.purchase),
    path('update/<id>/',views.update)
]