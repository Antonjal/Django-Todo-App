from django.contrib import admin
# This imports the "Task" Model
from .models import Task

# This registers the "Task" Model to be accessed via the admin panel
admin.site.register(Task)