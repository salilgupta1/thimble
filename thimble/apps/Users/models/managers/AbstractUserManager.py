from django.db import models

class AbstractUserManager(models.Manager):

	def update_following(self, user, increment):
		try:
			if increment:
				self.filter(user_id=user).update(following=models.F("following") + 1)
			else:
				self.filter(user_id=user).update(following=models.F("following") - 1)
		except:
			raise

	def update_followers(self, user, increment):
		try:
			if increment:
				self.filter(user_id=user).update(followers=models.F("followers") + 1)
			else:
				self.filter(user_id=user).update(followers=models.F("followers") - 1)
		except:
			raise