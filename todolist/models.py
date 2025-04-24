from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    taskName = models.CharField(max_length=100)
    isDone = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.name