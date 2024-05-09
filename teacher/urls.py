from django.contrib import admin
from django.urls import include, path

from teacher import views

urlpatterns = [
    path('tlogin/',views.tlogin),
    path('register/',views.register),
    path('teacher_profile/<id>/',views.teacher_profile),
    path('add/<id>/',views.add),
    path('playlist/<id>/',views.playlist),
    path('cedit/<id>/',views.cedit),
    path('delete/<id>/',views.delete),
    path('playedit/<id>/',views.playedit),
    path('playdelete/<id>/',views.playdelete),
    path('t_update/<id>/',views.t_update),
]

                