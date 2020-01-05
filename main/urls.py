from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    #path('host/',views.host,name='host'),
    #path('result/',views.result,name='result'),
    #path('room/',views.room,name='room'),
]