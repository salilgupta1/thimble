from django.db import models

class EntryManager(models.Manager):
	
	def get_entries(self, story_id):
		# get all entries associated with a story
		try:
			rows = self.filter(design_story_id=story_id).values('entry_title','bucket_link','cover_photo','num_photos')
			if len(rows) == 0:
				return None
			return rows
		except:
			raise

	def get_cover_photos(self, story_id):
		try:
			rows = self.filter(design_story_id=story_id).values('cover_photo').last()
			if len(rows) > 0:
				return rows
		except:
			raise