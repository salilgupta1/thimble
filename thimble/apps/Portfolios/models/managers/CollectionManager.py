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

	def get_collections(self, username):
		# get all the design stories associated with a username
		try:
			rows = self.filter(designer_id=username).values('collection_id','title','likes','comments','date_created')
			if len(rows) == 0:
				return None
		except:
			raise


	def get_design_story(self, username, collection_id):
		# get a specific design story's data 
		try:
			row = self.filter(designer_id=username, collection_id=collection_id).values('title',"likes","comments","description")
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise