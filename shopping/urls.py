from django.urls import path
from shopping.views import *
app_name='shopping'
urlpatterns=[
    path('suit/',suit,name='suit')
]