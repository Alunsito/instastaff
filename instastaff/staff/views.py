from django.shortcuts import render
from .forms import RegForm
from .models import worker

# Create your views here.
def index(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        email = form_data.get('email')
        username = form_data.get('name')
        emailobj = worker.objects.create(email, username)
        print (form_data.get('name'))
        print (form_data.get('age'))
        print (form_data.get('mail'))
        print (form_data.get('salary_hour'))
    return render(request, "index.html", {'form': form})