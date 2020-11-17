from django.db import models

# Create your models here.

class worker(models.Model):
    name = models.CharField(max_length=50)
    salary_hour = models.IntegerField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


