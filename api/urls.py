from .views import *
from django.urls import path
urlpatterns = [
    
    path('Getresult',result.as_view()), 
]