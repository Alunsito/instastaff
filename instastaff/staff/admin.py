from django.contrib import admin

# Register your models here.
from .models import worker

class registeredAdmin(admin.ModelAdmin):

admin.site.register(worker)