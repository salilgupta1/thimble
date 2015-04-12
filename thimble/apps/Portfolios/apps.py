from django.apps import AppConfig
 
class PortfoliosAppConfig(AppConfig):
	name="thimble.apps.Portfolios"
	verbose_name = "Portfolios"
	
	def ready(self):
		
        # import signal handlers
		import thimble.apps.Portfolios.signals.handlers