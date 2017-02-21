from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(ModelForm):
    password_again = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password']

    def is_valid(self):
        valid = super(RegistrationForm, self).is_valid()
        if not valid:
            return valid
        # import ipdb; ipdb.set_trace()# BREAKPOINT)

        # Check if password and password_again match
        password = self.data.get('password')
        password_again = self.data.get('password_again')

        if password != password_again:
            return False

        return valid


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
