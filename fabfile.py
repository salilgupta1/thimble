from fabric.api import local

def deploy():
	local('heroku maintenance:on')
	local('heroku config:push')
	local('pip freeze > requirements/common.txt')
	local('git push heroku master')
	local('heroku run python manage.py migrate')
	local('heroku maintenance:off')

def pull():
	local('pip install -r requirements.txt')
	local('heroku config:pull --overwrite --interactive')
	local('export $(cat .env)')
