from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from django.contrib.contenttypes.models import ContentType

class AbstractUser(models.Model):
	user 		= models.OneToOneField(User, to_field='username')
	avatar		= models.CharField(max_length=255, null=False, default='', blank=True)
	bio			= models.TextField(max_length=250, blank=True)
	location	= models.CharField(max_length=100, blank=True)
	following	= models.PositiveIntegerField(default=0, blank=True)
	followers	= models.PositiveIntegerField(default=0, blank=True)
	tags 		= TaggableManager()

	# These functions makes model self aware
	# i.e. it knows who it is
	def get_ct(self):
		return ContentType.objects.get_for_model(self)

	def get_model_name(self):
		return self.get_ct().model

	class Meta:
		# abstract class so don't create a table
		abstract = True
		app_label = 'Users'