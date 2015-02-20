from django.db import models

class DesignStoryManager(models.Manager):
	# self is the DesignStoryManager object
	# self.model is the DesignStory model name
	
	def get_design_stories(self, designer_id):
		try:
			return self.filter(designer=designer_id).values('designer_id','name','cover_photo')
		except self.model.DoesNotExist:
			return None
		except:
			raise