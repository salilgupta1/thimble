from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Portfolios.models.schemas.Comment import Comment
from thimble.apps.Portfolios.models.schemas.Collection import Collection

# change Likes counts
@receiver([post_save, post_delete], sender = Like)
def change_likes(sender, instance, **kwargs):
	
	signal = kwargs.get("signal", None)
	increment = True if signal == post_save else False
	Collection.objects.update_likes(collection_id = instance.collection_id, increment = increment) 


# change Comments counts
@receiver(post_save, sender = Comment)
def change_comments(sender, instance, **kwargs):
	
	signal = kwargs.get("signal", None)
	increment = True if signal == post_save else False
	Collection.objects.update_comments(collection_id = instance.collection_id, increment = increment) 
