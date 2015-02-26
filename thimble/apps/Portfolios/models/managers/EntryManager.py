from django.db import models

class EntryManager(models.Manager):
	
	def get_entries(self, story_id):
		# get all entries associated with a story
		try:
			rows = self.filter(design_story_id=story_id).values('context','date','bucket_link')
			if len(rows) == 0:
				return None
			return rows
		except:
			raise