from django.db import models

# Create your models here.

class Timing(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()

class chief(models.Model):
    name_chief = models.CharField(max_length=50)
    salary_chief = models.IntegerField()
    email_chief = models.EmailField()

class worker(models.Model):
    name = models.CharField(max_length=50)
    salary_hour = models.IntegerField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    timing = models.ForeignKey(Timing, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


