from django.db import models

class DesignerManager(models.Manager):
	# self is the DesignerManager object
	# self.model is the Designer model name

	def get_portfolio_data(self, subdomain):
		try:
			row = self.filter(subdomain=subdomain)
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise