from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Portfolios.models.schemas.Comment import Comment
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory

# increment Likes counts
@receiver(post_save, sender = Like)
def increment_likes(sender, instance, **kwargs):
	DesignStory.objects.update_likes(design_story_id = instance.design_story_id, increment = True) 

# decrement Likes counts
@receiver(post_delete, sender = Like)
def decrement_likes(sender, instance, **kwargs):
	DesignStory.objects.update_likes(design_story_id = instance.design_story_id, increment = False)

# increment Comments counts
@receiver(post_save, sender = Comment)
def increment_comments(sender, instance, **kwargs):
	DesignStory.objects.update_comments(design_story_id = instance.design_story_id, increment = True) 

# decrement Comments counts
@receiver(post_delete, sender = Comment)
def decrement_comments(sender, instance, **kwargs):
	DesignStory.objects.update_comments(design_story_id = instance.design_story_id, increment = False)
