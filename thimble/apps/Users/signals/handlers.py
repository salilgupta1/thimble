from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from thimble.apps.Users.models.schemas.Follow import Follow
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer

# change follow counts
@receiver([post_save, post_delete], sender = Follow)
def change_follow(sender, instance, **kwargs):

	signal = kwargs.get('signal', None)
	increment = True if signal == post_save else False

	# change the followers count for a followee
	# change the 7 to designer
	
	if instance.followee_content_type_id == 7:
		Designer.objects.update_followers(pk = instance.followee_object_id, increment = increment) 
	else:
		Buyer.objects.update_followers(pk = instance.followee_object_id, increment = increment)

	# change the following count for a follower
	if instance.follower_content_type_id == 7:
		Designer.objects.update_following(pk = instance.follower_object_id, increment = increment)
	else:
		Buyer.objects.update_following(pk = instance.follower_object_id, increment = increment)
