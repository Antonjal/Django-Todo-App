from django.urls import path
#This inports the view.py file
from base import views

urlpatterns = [
    path('',views.index,name="index")
]