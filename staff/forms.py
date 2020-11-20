from django import forms

from .models import worker

class RegModelForm(forms.ModelForm):
    class Meta:
        model = worker
        fields = ["name", "email", "salary_hour"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveeder = email.split("@")
        if not proveeder == "gmail.com":
            raise forms.ValidationError("Por favor, introduzca un email válido.")
        return email

class RegForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    salary_hour = forms.IntegerField()
