from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)

    def __str__(self):
        return self.title