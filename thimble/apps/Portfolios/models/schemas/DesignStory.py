from django.db import models
from thimble.apps.Portfolios.models.managers.DesignStoryManager import DesignStoryManager
from cloudinary.models import CloudinaryField

class DesignStory(models.Model):
	designer 		= models.ForeignKey('Users.Designer', to_field='user', on_delete=models.CASCADE)
	design_story_id = models.AutoField(primary_key=True)
	title 			= models.CharField(max_length=30)
	likes 			= models.BigIntegerField(default=0, blank=True)
	comments 		= models.BigIntegerField(default=0, blank=True)
	wip 			= models.BooleanField(default=False, blank=True)
	description 	= models.TextField(null=False)
	date_created 	= models.DateField(auto_now_add=True)

	# connect the manager
	objects = DesignStoryManager()

	class Meta:
		app_label = 'Portfolios'
		
		unique_together = ("designer","title")