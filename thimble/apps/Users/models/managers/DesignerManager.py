from django.db import models

class DesignerManager(models.Manager):
	# self is the DesignerManager object
	# self.model is the Designer model name

	def get_portfolio_data(self, subdomain):
		try:
			return self.get(subdomain=subdomain).values('designer_id','template_theme')
		except self.model.DoesNotExist:
			return None
		except:
			raise