from django.db import models
from django.core.exceptions import ValidationError
from thimble.apps.Users.models.managers.FollowManager import FollowManager

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Follow(models.Model):

	# generic foreign key allows relation to either user types
	
	follower_content_type = models.ForeignKey(ContentType, related_name='follower_content_type')
	follower_object_id = models.PositiveIntegerField()
	follower = GenericForeignKey('follower_content_type', 'follower_object_id')
		
	followee_content_type = models.ForeignKey(ContentType)
	followee_object_id = models.PositiveIntegerField()
	followee = GenericForeignKey('followee_content_type', 'followee_object_id')

	# connect the manager
	objects = FollowManager()

	def save(self, *args, **kwargs):
		if self.follower_content_type == self.followee_content_type and self.follower_object_id == self.followee_object_id:
			raise ValidationError("Follower and Followee must be different people")
		super(Follow, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('follower_content_type','follower_object_id','followee_content_type','followee_object_id')
		app_label='Users'