from django.db import models
from thimble.apps.Portfolios.models.managers.PortfolioManager import PortfolioManager


class Portfolio(models.Model):
	designer = models.OneToOneField("Users.Designer", primary_key=True)

	# Designer specific fields
	subdomain = models.CharField(max_length=30, unique=True)
	template_theme = models.CharField(max_length=30)

	# connect the manager
	objects = PortfolioManager()

	class Meta:
	    app_label='Portfolios'