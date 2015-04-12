from django.db import models

class FollowManager(models.Manager):
	
	def get_is_following(self, follower, followee):
		try:
			row = self.filter(follower=follower, followee=followee)
			if len(row) == 0:
				return False
		except:
			raise
		return True
