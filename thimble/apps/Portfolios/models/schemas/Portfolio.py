from django.db import models
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.managers.DesignerManager import DesignerManager
from thimble.apps.Users.models.managers.DesignerManager import DesignerManager


class Designer(models.Model):
	designer = models.OneToOneField(Designer, primary_key=True)

	# Designer specific fields
	subdomain = models.CharField(max_length=30)
	template_theme = models.CharField(max_length=30)

	# connect the manager
	objects = PortfolioManager()

	class Meta:
	    app_label='Portfolios'