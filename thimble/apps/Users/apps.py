from django.apps import AppConfig
 

class UsersAppConfig(AppConfig):
	name="thimble.apps.Users"
	verbose_name = "Users"
	
	def ready(self):
		
        # import signal handlers
		import thimble.apps.Users.signals.handlers