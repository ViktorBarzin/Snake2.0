from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from authentication.models import Profile


class RegistrationForm(ModelForm):
    password_again = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['username', 'password', 'profile_picture_url']
        widgets ={
                # todo: fix password input type
                'username': forms.TextInput(attrs={'class':'form-control'}),
                # 'password': forms.CharField(widget=forms.PasswordInput()),
                # 'password_again': forms.CharField(widget=forms.PasswordInput()),
                # 'password': forms.CharField(widget=forms.PasswordInput,attrs={'class':'form-control'}),
                # 'password_again': forms.CharField(widget=forms.PasswordInput,attrs={'class':'form-control'}),
                'email': forms.TextInput(attrs={'class':'form-control'}),
        }

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
