from test1 import views
from django.contrib import admin
from django.urls import path

urlpatterns = []
urlpatterns.append(path('add_home', views.add_home, name='add_home'))
urlpatterns.append(path('add_room', views.add_room, name='add_room'))
urlpatterns.append(path('homes_liste', views.homes_liste, name='homes_liste'))
urlpatterns.append(path('room_liste', views.room_liste, name='room_liste'))
urlpatterns.append(path('add_emplacement', views.add_emplacement, name='add_emplacemt'))
#urlpatterns.append(path('mod', views.mod, name='mod'))
