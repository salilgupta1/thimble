from django.db import models
from thimble.apps.Portfolios.models.managers.CommentManager import CommentManager

class Comment(models.Model):
	commenter = models.ForeignKey("Users.Designer", on_delete = models.CASCADE)
	design_story = models.ForeignKey("Portfolios.DesignStory", on_delete = models.CASCADE)
	comment = models.TextField(null=False, blank=False)
	date = models.DateField(auto_now_add=True)

	# connect the manager
	objects = CommentManager()
	
	class Meta:
		app_label='Portfolios'