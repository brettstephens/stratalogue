from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
	name = models.CharField(max_length=32)


class Map(models.Model):
	name = models.CharField(max_length=32)


class Playbook(models.Model):
	name = models.CharField(max_length=64)
	creator = models.OneToOneField(User)
	private = models.BooleanField(default=True)
	de_map = models.ForeignKey(Map)

	# Roles
	role1 = models.ForeignKey(Role, related_name='role1')
	role2 = models.ForeignKey(Role, related_name='role2')
	role3 = models.ForeignKey(Role, related_name='role3')
	role4 = models.ForeignKey(Role, related_name='role4')
	role5 = models.ForeignKey(Role, related_name='role5')