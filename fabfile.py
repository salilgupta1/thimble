from fabric.api import local

def deploy_production():
	local('heroku maintenance:on')
	local('git push production master')
	local('heroku run python manage.py migrate')
	local('heroku run python manage.py collectstatic')
	local('heroku maintenance:off')

def deploy_staging():
	local('heroku maintenance:on')
	local('git push staging dev')
	local('heroku run python manage.py migrate')
	local('heroku run python manage.py collectstatic')
	local('heroku maintenance:off')
