from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from thimble.apps.Users.models.schemas.Follow import Follow
from thimble.apps.Users.models.schemas.Designer import Designer

# increment follow counts
@receiver(post_save, sender = Follow)
def increment_follow(sender, instance, **kwargs):

	# increment the followers count for a followee
	Designer.objects.update_followers(user = instance.followee.user_id, increment = True) 

	# increment the following count for a follower
	Designer.objects.update_following(user = instance.follower.user_id, increment = True)

# decrement follow counts
@receiver(post_delete, sender = Follow)
def decrement_follow(sender, instance, **kwargs):

	# decrement the followers count for a followee
	Designer.objects.update_followers(user = instance.followee.user_id, increment = False)

	# decrement the following count for a follower
	Designer.objects.update_following(user = instance.follower.user_id, increment = False)