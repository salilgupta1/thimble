from django.db import models

class LikeManager(models.Manager):
	
	def get_likes(self, liker, collection_ids):
		# return which design stories a user has liked 
		try:
			rows = self.filter(collection_id__in=collection_ids, liker=liker).values_list("collection_id", flat=True)
			return rows
		except:
			raise

	def get_favorites(self, liker):
		# count of number of stories a user has liked
		try:
			count = self.filter(liker_id=liker).count()
			return count
		except:
			raise