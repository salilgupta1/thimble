from django.db import models
from thimble.apps.Portfolios.models.managers.CollectionManager import CollectionManager
from taggit.managers import TaggableManager
from django.contrib.contenttypes.models import ContentType

class Collection(models.Model):

	designer 		= models.ForeignKey('Users.Designer', to_field='user', on_delete=models.CASCADE)
	title 			= models.CharField(max_length=70)
	likes 			= models.PositiveIntegerField(default=0, blank=True)
	comments 		= models.PositiveIntegerField(default=0, blank=True)
	wip 			= models.BooleanField(default=False, blank=True)
	description 	= models.TextField(max_length=255, blank=True)
	date_created 	= models.DateField(auto_now_add=True)

	tags = TaggableManager()

	# connect the manager
	objects = CollectionManager()


	# These functions makes model self aware
	# i.e. it knows who it is
	def get_ct(self):
		return ContentType.objects.get_for_model(self)

	class Meta:
		app_label = 'Portfolios'
		unique_together = ("designer","title")