from django.db import models
from thimble.apps.Portfolios.models.managers.CommentManager import CommentManager
from django.contrib.auth.models import User

class Comment(models.Model):
	commenter 		= models.ForeignKey(User, on_delete=models.CASCADE)
	collection		= models.ForeignKey("Portfolios.Collection", on_delete=models.CASCADE)
	comment 		= models.TextField(null=False, blank=False)
	date 			= models.DateField(auto_now_add=True)

	# connect the manager
	objects = CommentManager()
	
	class Meta:
		app_label='Portfolios'