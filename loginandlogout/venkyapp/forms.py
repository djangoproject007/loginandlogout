from django import forms
from django.contrib.auth.models import User
class signupForm(forms.ModelForm):
    class Meta:
        fields=['username','password','email','first_name','last_name']