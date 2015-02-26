from django.db import models

class DesignStoryManager(models.Manager):
	
	def get_design_stories(self, subdomain):
		# get all the design stories associated with a subdomain
		try:
			rows = self.filter(designer_id=subdomain).values('design_story_id')
			if len(rows) == 0:
				return None
			return rows
		except:
			raise

	def get_design_story(self, subdomain, design_story_id):
		# get a design story's data 
		# make sure subdomain and designer_story_id match up
		try:
			row = self.filter(designer_id=subdomain, design_story_id=design_story_id).values('name','description')
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise