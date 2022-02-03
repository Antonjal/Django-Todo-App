
from django.db import models

# Task Model which essentially defines our task object structure
class Task(models.Model):
    # Our Task Title
    title=models.CharField(max_length=350)
    # "Completed" checkmark with the default value of "false"
    completed=models.BooleanField(default=False) 
    # The datetime indicates when the task was created with the date saved automatically
    created=models.DateTimeField(auto_now_add=True)
    # The default human-readable representation of the object
    def __str__(self):
        return self.title