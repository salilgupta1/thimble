from django.db import models
from thimble.apps.Portfolios.models.managers.CollectionManager import CollectionManager
from cloudinary.models import CloudinaryField

class Collection(models.Model):
	designer 		= models.ForeignKey('Users.Designer', to_field='user', on_delete=models.CASCADE)
	collection_id 	= models.AutoField(primary_key=True)
	title 			= models.CharField(max_length=70)
	likes 			= models.BigIntegerField(default=0, blank=True)
	comments 		= models.BigIntegerField(default=0, blank=True)
	wip 			= models.BooleanField(default=False, blank=True)
	description 	= models.TextField(max_length=255, blank=True)
	date_created 	= models.DateField(auto_now_add=True)

	# connect the manager
	objects = CollectionManager()

	class Meta:
		app_label = 'Portfolios'
		
		unique_together = ("designer","title")