from django.db import models
from thimble.apps.Portfolios.models.managers.EntryManager import EntryManager


class Entry(models.Model):
	
	# connect the manager
	objects = EntryManager()

	class Meta:
	    app_label='Portfolios'