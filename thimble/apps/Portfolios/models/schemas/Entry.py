from django.db import models
from thimble.apps.Portfolios.models.managers.EntryManager import EntryManager


class Entry(models.Model):
	
	design_story = models.ForeignKey('Portfolios.DesignStory')

	# entry specific fields
	entry_id = models.AutoField(primary_key = True)
	context = models.TextField(blank = True)
	date = models.DateField(blank=True)
	bucket_link = models.CharField(max_length=255, null=False)
	
	# connect the manager
	objects = EntryManager()

	class Meta:
	    app_label='Portfolios'