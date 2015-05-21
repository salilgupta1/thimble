from thimble.apps.Users.models.managers.DesignerManager import DesignerManager
from thimble.apps.Users.models.schemas.AbstractUser import AbstractUser
from django.db import models

# add links to social media accounts
# add link to website

class Designer(AbstractUser):

	# connect the manager
	objects = DesignerManager()

	class Meta:
		# so migrations know where to look
	    app_label = 'Users'