from django.db import models
from thimble.apps.Portfolios.models.managers.EntryManager import EntryManager
from cloudinary.models import CloudinaryField


class Entry(models.Model):
	
	design_story = models.ForeignKey('Portfolios.DesignStory', on_delete = models.CASCADE)

	# entry specific fields
	entry_id = models.AutoField(primary_key = True)
	context = models.TextField(blank = True)
	
	### remove
	date = models.DateField(blank=True)
	####

	### 
	## date uploaded
	###
	 
	bucket_link = models.CharField(max_length=255, null=False, default='dummy') # /subdomain/story_id/entry_id
	cover_photo = CloudinaryField('image') 
	num_photos = models.IntegerField(default=0)

	# connect the manager
	objects = EntryManager()

	class Meta:
	    app_label='Portfolios'