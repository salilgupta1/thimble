from django.db import models
from thimble.apps.Portfolios.models.managers.DesignStoryManager import DesignStoryManager


class DesignStory(models.Model):
	portfolio = models.ForeignKey('Portfolios.Portfolio')
	
	# design story specific fields
	design_story_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30, unique=True)
	description = models.TextField()
	cover_photo = models.CharField(max_length=255)
	date_created = models.DateField(auto_now_add=True)

	# connect the manager
	objects = DesignStoryManager()

	class Meta:
	    app_label='Portfolios'