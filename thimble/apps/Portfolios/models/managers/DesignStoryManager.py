from django.db import models

class DesignStoryManager(models.Manager):
	
	def get_design_stories(self, username):
		# get all the design stories associated with a username
		try:
			rows = self.filter(designer_id=username).values('design_story_id','name')
			if len(rows) == 0:
				return None
			return rows
		except:
			raise

	def get_design_story(self, username, design_story_id):
		# get a design story's data 
		# make sure username and designer_story_id match up
		try:
			row = self.filter(designer_id=username, design_story_id=design_story_id).values('name')
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise