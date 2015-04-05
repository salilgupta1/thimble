from django.db import models

class DesignerManager(models.Manager):
	def get_portfolio_data(self, username):
		try:
			# get the designer information associated with the subdomain
			row = self.filter(user=username)
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise