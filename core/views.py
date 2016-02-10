from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm

def index(request):

	return render(request, 'index_template_1.html')


def create_playbook(request):

	return render(request, 'create_playbook.html')


def login_user(request):

	if request.POST:
		login_form = LoginForm(request.POST)

		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')

			else:
				messages.add_message(request, messages.INFO, "Username or password invalid.")
				return redirect('login')


	return render(request, 'login.html')


def logout_user(request):
	logout(request)

	return redirect('login')



def registration(request):

	if request.POST:
		registration_form = RegistrationForm(request.POST)

		if registration_form.is_valid():
			username = registration_form.cleaned_data['username']
			email = registration_form.cleaned_data['email']
			password1 = registration_form.cleaned_data['password1']
			password2 = registration_form.cleaned_data['password2']

			if password1 == password2:
				new_user = User.objects.create(username=username, email=email)
				new_user.set_password(password1)

				# TODO: Send confirmation email and have user confirm their email
				new_user.save()
				return redirect('registration_success')

		else:
			return redirect('registration')

	return render(request, 'registration.html')


def registration_success(request):

	return render(request, 'registration.html')