from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from thimble.apps.Users.models.schemas.Follow import Follow
from thimble.apps.Users.models.schemas.Designer import Designer

# change follow counts
@receiver([post_save, post_delete], sender = Follow)
def change_follow(sender, instance, **kwargs):

	signal = kwargs.get('signal', None)
	increment = True if signal == post_save else False

	# change the followers count for a followee
	if instance.followee.get_model_name == "designer":
		Designer.objects.update_followers(user = instance.followee.user_id, increment = increment) 
	else:
		Buyer.objects.update_followers(user = instance.followee.user_id, increment = increment)

	# change the following count for a follower
	if instance.follower.get_model_name == "designer":
		Designer.objects.update_following(user = instance.follower.user_id, increment = increment)
	else:
		Buyer.objects.update_following(user = instance.follower.user_id, increment = increment)
