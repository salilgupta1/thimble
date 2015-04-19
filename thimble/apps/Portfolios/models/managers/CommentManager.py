from django.db import models

class CommentManager(models.Manager):
	
	def get_comments(self, design_story_id):
		try:
			rows = self.filter(design_story_id=design_story_id).values("commenter", "comment")
			if len(rows):
				return rows
			return None
		except:
			raise
