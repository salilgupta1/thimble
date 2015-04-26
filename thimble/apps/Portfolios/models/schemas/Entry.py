from django.db import models
from thimble.apps.Portfolios.models.managers.EntryManager import EntryManager
from cloudinary.models import CloudinaryField


class Entry(models.Model):
	design_story = models.ForeignKey('Portfolios.DesignStory', on_delete = models.CASCADE)
	entry_id = models.AutoField(primary_key = True)
	entry_title = models.CharField(max_length=255)	
	date_created = models.DateField(auto_now_add=True)
	bucket_link = models.CharField(max_length=255, null=False, default='', blank=True) 
	cover_photo = models.CharField(max_length=255, null=False, default='', blank=True) 

	# connect the manager
	objects = EntryManager()

	class Meta:
	    app_label='Portfolios'
	    unique_together=('entry_title','design_story')