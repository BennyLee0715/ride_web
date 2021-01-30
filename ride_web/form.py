from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=32)
    password = forms.CharField(label="password", max_length=128, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=32)
    password = forms.CharField(label="password", max_length=128, widget=forms.PasswordInput)
    email = forms.CharField(label="email", max_length=128)