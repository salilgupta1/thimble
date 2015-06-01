from django.db import models
from thimble.apps.Portfolios.models.managers.LikeManager import LikeManager

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Like(models.Model):

	# generic foreign key allows relation to either user types

	content_type 	= models.ForeignKey(ContentType)
	object_id		= models.PositiveIntegerField()
	liker	 		= GenericForeignKey('content_type','object_id')

	collection	 	= models.ForeignKey("Portfolios.Collection", on_delete = models.CASCADE)

	# connect the manager
	objects = LikeManager()
	
	class Meta:
		app_label = 'Portfolios'
		unique_together = ('content_type','object_id','collection')