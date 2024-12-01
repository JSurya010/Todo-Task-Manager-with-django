from django.db import models
from django.contrib.auth.models import User

class todo_list(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    task = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    task_created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
