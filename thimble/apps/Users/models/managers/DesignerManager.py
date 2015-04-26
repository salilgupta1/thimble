from django.db import models

class DesignerManager(models.Manager):
	def get_portfolio_data(self, username, column_list):
		try:
			# get the designer information
			row = self.filter(user=username).values(*column_list)
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise

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