from django.db import models

class LikeManager(models.Manager):
	
	def get_likes(self, liker):
		# return which collections a user has liked 
		try:
			object_id = liker.pk
			content_type = liker.get_ct()
			rows = self.filter(object_id=object_id, content_type=content_type).values_list("collection_id", flat=True)
			return rows
		except:
			raise

	def get_is_liked(self, liker, collection_id):
		try:
			object_id = liker.pk
			content_type = liker.get_ct()
			row = self.filter(collection_id=collection_id, object_id=object_id, content_type=content_type).values('collection_id')
			if len(row) > 0:
				return True
			return False
		except:
			raise


	def get_favorite_count(self, liker):
		# count of number of collections a user has liked
		try:
			object_id = liker.pk
			content_type = liker.get_ct()
			count = self.filter(object_id = object_id, content_type=content_type).count()
			return count
		except:
			raise

