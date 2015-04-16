from django.db import models

class LikeManager(models.Manager):
	
	def get_likes(self, liker, story_ids):
		try:
			rows = self.filter(design_story_id__in=story_ids, liker=liker).values_list("design_story_id", flat=True)
			return rows
		except:
			raise

	def get_favorites(self, liker):
		try:
			count = self.filter(liker_id=liker).count()
			return count
		except:
			raise