from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name','last_name', 'email', 'username', 'password']
        help_texts = {'first_name':'Enter Your First Name', 'username':'Select a Unique Username'}
        widgets={'password':forms.PasswordInput}