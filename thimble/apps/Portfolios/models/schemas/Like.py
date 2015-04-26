from django.db import models
from thimble.apps.Portfolios.models.managers.LikeManager import LikeManager

class Like(models.Model):
	liker = models.ForeignKey("Users.Designer", on_delete = models.CASCADE)
	design_story = models.ForeignKey("Portfolios.DesignStory", on_delete = models.CASCADE)

	# connect the manager
	objects = LikeManager()
	
	class Meta:
		unique_together=('liker','design_story')
		app_label='Portfolios'