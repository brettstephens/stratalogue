from django.shortcuts import render

from .forms import RegistrationForm 

def index(request):

	return render(request, 'index_template_1.html')


def registration(request):

	if request.POST:
		registration_form = RegistrationForm(request.POST)

		if registration_form.is_valid():
			username = registration_form.cleaned_data['username']
			email = registration_form.cleaned_data['email']
			password1 = registration_form.cleaned_data['password1']
			password2 = registration_form.cleaned_data['password2']

			if password1 is password2:
				print 'yay'
			else:
				print 'boo'

	return render(request, 'registration.html')