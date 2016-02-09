from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import RegistrationForm 

def index(request):

	return render(request, 'index_template_1.html')


def registration(request):

	if request.POST:
		registration_form = RegistrationForm(request.POST)
		print 'ay'
		if registration_form.is_valid():
			print 'b'
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