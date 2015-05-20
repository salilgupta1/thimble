from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class AbstractUser(models.Model):
	user 		= models.OneToOneField(User, to_field='username', primary_key=True)
	avatar		= models.CharField(max_length=255, null=False, default='', blank=True)
	bio			= models.TextField(max_length=250, blank=True)
	location	= models.CharField(max_length=100, blank=True)
	following	= models.BigIntegerField(default=0, blank=True)
	followers	= models.BigIntegerField(default=0, blank=True)

	class Meta:
		# abstract class so don't create a table
		abstract = True
		app_label = 'Users'