from django.db import models
from thimble.apps.Portfolios.models.managers.DesignStoryManager import DesignStoryManager
from cloudinary.models import CloudinaryField

# work in progress
# number of likes
# link to who likes
# number of comments
# link to comments

class DesignStory(models.Model):
	designer = models.ForeignKey('Users.Designer', to_field='user', on_delete = models.CASCADE)
	
	design_story_id = models.AutoField(primary_key=True)

	name = models.CharField(max_length=30)

	#description = models.TextField(null=False)
	#cover_photo = CloudinaryField('image')

	date_created = models.DateField(auto_now_add=True)

	# connect the manager
	objects = DesignStoryManager()

	class Meta:
		app_label='Portfolios'
		
		unique_together = ("designer","name")