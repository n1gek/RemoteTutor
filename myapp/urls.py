from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('checkview/', views.checkview, name='checkview'),
    path('subject', views.subject_selection, name='subject_selection'),
     path('send', views.send, name='send'),
    path('getMessages/', views.getMessages, name='getMessages'),
]