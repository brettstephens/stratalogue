from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login_user, name="login"),
	url(r'^logout$', views.logout_user, name="logout"),
	url(r'^register$', views.registration, name="registration"),
	url(r'^register/success$', views.registration, name="registration_success"),


]