from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mobile_number', 'first_name',
                  'last_name', 'date_of_birth', 'sex', 'email']
