from django.db import models

class LikeManager(models.Manager):
	
	def get_likes(self, liker, collection_ids):
		# return which collections a user has liked 
		try:
			object_id = liker.pk
			content_type = liker.get_ct()
			rows = self.filter(collection_id__in=collection_ids, object_id=object_id, content_type=content_type).values_list("collection_id", flat=True)
			return rows
		except:
			raise

	def get_favorites(self, liker):
		# count of number of collections a user has liked
		try:
			object_id = liker.pk
			content_type = liker.get_ct()
			count = self.filter(object_id = object_id, content_type=content_type).count()
			return count
		except:
			raise
