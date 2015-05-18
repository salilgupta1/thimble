from django.db import models

class CollectionManager(models.Manager):
	
	def update_likes(self, collection_id, increment):
		try:
			if increment:
				self.filter(collection_id=collection_id).update(likes=models.F("likes") + 1)
			else:
				self.filter(collection_id=collection_id).update(likes=models.F("likes") - 1)
		except:
			raise

	def update_comments(self, collection_id, increment):
		try:
			if increment:
				self.filter(collection_id=collection_id).update(comments=models.F("comments") + 1)
			else:
				self.filter(collection_id=collection_id).update(comments=models.F("comments") - 1)
		except:
			raise