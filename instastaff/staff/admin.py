from django.contrib import admin

# Register your models here.
from .models import worker

class registeredAdmin(admin.ModelAdmin):
    list_display =["__str__", "name", "timestamp"]
    list_filter = ["timestamp"]
    list_editable = []
    search_fields = ["email", "name"]
    class Meta:
        model = worker

admin.site.register(worker, registeredAdmin)