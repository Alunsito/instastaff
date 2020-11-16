from django import forms

class RegForm(forms.Form):
    name = forms.CharField(max_length=100)
    mail = forms.EmailField()
    salary_hour = forms.IntegerField()
