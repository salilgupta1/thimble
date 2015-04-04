from django.db import models

class DesignerManager(models.Manager):
	pass
	# def get_portfolio_data(self, subdomain):
	# 	try:
	# 		# get the designer information associated with the subdomain
	# 		row = self.filter(subdomain=subdomain)
	# 		if len(row) == 0:
	# 			return None
	# 		return row[0]
	# 	except:
	# 		raise