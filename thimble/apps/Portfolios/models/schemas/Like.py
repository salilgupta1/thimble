from django.db import models
from thimble.apps.Portfolios.models.managers.LikeManager import LikeManager

class Like(models.Model):
	liker 			= models.ForeignKey("Users.Designer", on_delete = models.CASCADE)
	collection	 	= models.ForeignKey("Portfolios.Collection", on_delete = models.CASCADE)

	# connect the manager
	objects = LikeManager()
	
	class Meta:
		unique_together = ('liker','collection')
		app_label = 'Portfolios'