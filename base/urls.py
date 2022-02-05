from django.urls import path
#This imports the view.py file
from base import views

urlpatterns = [
    # The url pattern for the "index page"
    path('',views.index,name="index"),
    # The url pattern for updating tasks
    path("update/<int:pk>/", views.update_task, name="update_task"),
    # The url pattern for deleting tasks
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),


]