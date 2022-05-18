from django import views
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
   path('',views.home, name = "home"),
   path('login/',views.login, name = 'login'),
   path('Signin/addrecord/',views.Addrecord, name = "Signin/addrecord/"),
   path('ticket/',views.ticket, name = 'ticket'),
    path('Add/',views.Add, name = 'Add'),
    path('Add1/',views.Add1, name = 'Add1'),
    path('manage/',views.Add1, name = 'Add1'),
    
]