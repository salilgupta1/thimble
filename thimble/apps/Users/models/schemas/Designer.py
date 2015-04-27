from django.db import models
from django.contrib.auth.models import User
from thimble.apps.Users.models.managers.DesignerManager import DesignerManager
from cloudinary.models import CloudinaryField

# add links to social media accounts
# add link to website

class Designer(models.Model):
	user = models.OneToOneField(User, to_field='username', primary_key=True)
	bio  = models.TextField(max_length=250, blank=True)
	avatar	  = models.CharField(max_length=255, null=False, default='', blank=True) 
	location  = models.CharField(max_length=100, blank=True)
	following = models.BigIntegerField(default=0, blank=True)
	followers = models.BigIntegerField(default=0, blank=True)

	# connect the manager
	objects = DesignerManager()

	class Meta:
		# so migrations know where to look
	    app_label = 'Users'