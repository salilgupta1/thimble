from fabric.api import local

def deploy_production():
	local('heroku maintenance:on --app thimbleapp')
	local('git push heroku master')
	local('heroku run python manage.py migrate --app thimbleapp')
	local('heroku maintenance:off --app thimbleapp')

def deploy_staging():
	local('heroku maintenance:on --app staging-thimble')
	local('git push staging dev:master')
	local('heroku run python manage.py migrate --app staging-thimble')
	local('heroku maintenance:off --app staging-thimble')
