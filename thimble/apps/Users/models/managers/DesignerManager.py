from thimble.apps.Users.models.managers.AbstractUserManager import AbstractUserManager
from django.db import models

class DesignerManager(AbstractUserManager):
	def get_designer_info(self, username):
		try:
			# get the designer information
			row = self.filter(user=username)
			if len(row) == 0:
				return None
			return row[0]
		except:
			raise

	def get_avatar(self, username):
		try:
			row = self.filter(user=username).values('avatar')
			if len(row) == 0:
				return None
			return row[0]['avatar']
		except:
			raise