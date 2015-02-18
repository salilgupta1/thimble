from django.db import models
from thimble.apps.Portfolios.models.managers.DesignStoryManager import DesignStoryManager


class DesignStory(models.Model):
	designer = models.OneToOneField("Users.Designer", primary_key=True)

	# Designer specific fields
	subdomain = models.CharField(max_length=30)
	template_theme = models.CharField(max_length=30)

	# connect the manager
	objects = DesignStoryManager()

	class Meta:
	    app_label='Portfolios'