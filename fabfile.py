from fabric import local

def deploy():
	local('heroku maintenance:on')
	local('git push heroku master')
	local('heroku run python manage.py migrate')
	local('heroku maintenance:off')

