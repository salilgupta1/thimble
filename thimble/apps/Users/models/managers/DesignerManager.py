from thimble.apps.Users.models.managers.AbstractUserManager import AbstractUserManager
from django.db import models

class DesignerManager(AbstractUserManager):
	def get_portfolio_data(self, username, column_list):
		try:
			# get the designer information
			row = self.filter(user=username).values(*column_list)
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise