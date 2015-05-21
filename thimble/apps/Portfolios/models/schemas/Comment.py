from django.db import models
from thimble.apps.Portfolios.models.managers.CommentManager import CommentManager

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):

	# generic foreign key allows relation to either user types

	content_type 	= models.ForeignKey(ContentType)
	object_id		= models.PositiveIntegerField()
	commenter 		= GenericForeignKey('content_type','object_id')

	collection		= models.ForeignKey("Portfolios.Collection", on_delete=models.CASCADE)
	comment 		= models.TextField(null=False, blank=False)
	date 			= models.DateField(auto_now_add=True)

	# connect the manager
	objects = CommentManager()
	
	class Meta:
		app_label='Portfolios'