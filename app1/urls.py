from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('mom/',mom,name='mom'),
    path('dad/',dad,name='dad'),
]