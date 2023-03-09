from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('family/',family,name='family'),
    path('girl/',girl,name='girl'),
]