from django.db import models

class CommentManager(models.Manager):
	
	def get_comments(self, collection_id):
		try:
			rows = self.filter(collection_id=collection_id).values("object_id", "content_type_id", "comment")
			if len(rows):
				return rows
			return None
		except:
			raise
