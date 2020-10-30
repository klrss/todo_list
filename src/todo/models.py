from django.db import models
from django.utils import timezone

# Create your models here.

class Projects (models.Model):
    name = models.CharField(max_length = 64)
        
    def __str__(self):
        return self.name

class Todo(models.Model):
    task = models.CharField(max_length=254)
    deadline = models.DateField(default = timezone.now)
    priority = models.IntegerField(default=1)
    title = models.ForeignKey(Projects, on_delete = models.CASCADE, default=None)
    completed = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ["priority"]
        
    def __str__(self):
        return self.task