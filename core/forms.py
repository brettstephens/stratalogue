from django import forms


class RegistrationForm(forms.Form):
	username = forms.CharField(label="username", max_length=25)
	email = forms.EmailField(label="email", max_length=64)
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
	username = forms.CharField(label="username", max_length=25)
	password = forms.CharField(widget=forms.PasswordInput())


class CreatePlaybook(forms.Form):
	name = forms.CharField(label="name", max_length=32)
	private = forms.BooleanField(label="private")
	de_map = forms.CharField(label="de_map", max_length=2)
	role1 = forms.CharField(label="role1", max_length=32)
	role2 = forms.CharField(label="role2", max_length=32)
	role3 = forms.CharField(label="role3", max_length=32)
	role4 = forms.CharField(label="role4", max_length=32)
	role5 = forms.CharField(label="role5", max_length=32)
