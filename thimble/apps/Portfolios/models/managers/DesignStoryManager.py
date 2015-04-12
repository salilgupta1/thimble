from django.db import models

class DesignStoryManager(models.Manager):
	
	def get_design_stories(self, username):
		# get all the design stories associated with a username
		try:
			rows = self.filter(designer_id=username).values('design_story_id','title','likes','wip','comments','date_created')
			if len(rows) == 0:
				return None
			return rows
		except:
			raise

	def get_design_story(self, username, design_story_id):
		# get a design story's data 
		# make sure username and designer_story_id match up
		try:
			row = self.filter(designer_id=username, design_story_id=design_story_id).values('title',"likes","comments","description")
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise

	def update_likes(self, design_story_id, increment):
		try:
			if increment:
				self.filter(design_story_id=design_story_id).update(likes=models.F("likes") + 1)
			else:
				self.filter(design_story_id=design_story_id).update(likes=models.F("likes") - 1)
		except:
			raise

	def update_comments(self, design_story_id, increment):
		try:
			if increment:
				self.filter(design_story_id=design_story_id).update(comments=models.F("comments") + 1)
			else:
				self.filter(design_story_id=design_story_id).update(comments=models.F("comments") - 1)
		except:
			raise
