from django.db import models

class CollectionManager(models.Manager):
	
	def update_likes(self, collection_id, increment):
		try:
			if increment:
				self.filter(id=collection_id).update(likes=models.F("likes") + 1)
			else:
				self.filter(id=collection_id).update(likes=models.F("likes") - 1)
		except:
			raise

	def update_comments(self, collection_id, increment):
		try:
			if increment:
				self.filter(id=collection_id).update(comments=models.F("comments") + 1)
			else:
				self.filter(id=collection_id).update(comments=models.F("comments") - 1)
		except:
			raise

	def get_collections(self, username):
		# get all the design stories associated with a username
		try:
			rows = self.filter(designer_id=username).values('id','title','likes','comments','date_created','description')
			if len(rows) == 0:
				return None
			return rows
		except:
			raise

	def get_collection(self, collection_id):
		# get a specific design story's data 
		try:
			row = self.filter(id=collection_id).values('title',"likes","comments","description")
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise

	def get_tags(self, collection_id):
		try:
			tags = self.filter(id=collection_id)[0].tags.names()
			if len(tags) == 0:
				return None
			return tags
		except:
			raise