from django.db import models 

# Create your models here.
# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.task)
