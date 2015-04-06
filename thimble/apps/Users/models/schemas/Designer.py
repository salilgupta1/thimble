from django.db import models
from django.contrib.auth.models import User
from thimble.apps.Users.models.managers.DesignerManager import DesignerManager
from cloudinary.models import CloudinaryField

# social media accounts

class Designer(models.Model):
	user = models.OneToOneField(User, to_field='username', primary_key=True)
	bio = models.TextField(blank=True)

	# Points to a Cloudinary image
	avatar = CloudinaryField('image', blank=True, null=True)
	location = 	models.CharField(max_length=200, blank=True)
	following = models.BigIntegerField(default=0, blank=True)
	followers = models.BigIntegerField(default=0, blank=True)

	# connect the manager
	objects = DesignerManager()

	class Meta:
		# so migrations know where to look
	    app_label='Users'