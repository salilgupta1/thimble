from thimble.apps.Users.models.managers.BuyerManager import BuyerManager
from thimble.apps.Users.models.schemas.AbstractUser import AbstractUser
from django.db import models

# add links to social media accounts
# add link to website

class Buyer(AbstractUser):
	boutique_name 	= models.CharField(max_length=100)

	# connect the manager
	objects = BuyerManager()

	class Meta:
		# so migrations know where to look
	    app_label = 'Users'