from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import worker

class registeredAdmin(admin.ModelAdmin):
    list_display =["__str__", "email", "salary_hour"]
    form = RegModelForm
    list_filter = ["timestamp"]
    list_editable = []
    search_fields = ["email", "name"]
    class Meta:
        model = worker

admin.site.register(worker, registeredAdmin)