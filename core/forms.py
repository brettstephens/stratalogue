from django import forms


class RegistrationForm(forms.Form):
	username = forms.CharField(label="username", max_length=25)
	email = forms.EmailField(label="email", max_length=64)
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
	username = forms.CharField(label="username", max_length=25)
	password = forms.CharField(widget=forms.PasswordInput())
