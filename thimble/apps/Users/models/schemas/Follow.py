from django.db import models
from django.core.exceptions import ValidationError
from thimble.apps.Users.models.managers.FollowManager import FollowManager
from django.contrib.auth.models import User

class Follow(models.Model):
	follower = models.ForeignKey(User, related_name="follow_follower", on_delete = models.CASCADE)
	followee = models.ForeignKey(User, related_name="follow_followee", on_delete = models.CASCADE)

	# connect the manager
	objects = FollowManager()

	def save(self, *args, **kwargs):
		if self.follower == self.followee:
			raise ValidationError("Follower and Followee must be different people")
		super(Follow, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('follower','followee')
		app_label='Users'