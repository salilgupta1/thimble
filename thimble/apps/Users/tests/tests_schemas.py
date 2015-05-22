from django.test import TestCase

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer
from thimble.apps.Users.models.schemas.Follow import Follow

from django.contrib.contenttypes.models import ContentType

class UsersModelTestCase(TestCase):
	fixtures = ['auth_user.json','users.json']

	def setUp(self):
		super(UsersModelTestCase, self).setUp()
		self.designer = Designer.objects.get(pk=1)
		self.buyer = Buyer.objects.get(pk=1)

class AbstractUserTestCase(UsersModelTestCase):

	def test_content_type(self):

		self.assertEqual(self.designer.get_ct(), ContentType.objects.get_for_model(self.designer))

		self.assertEqual(self.buyer.get_ct(), ContentType.objects.get_for_model(self.buyer))

		self.assertEqual(self.designer.get_ct().model, ContentType.objects.get_for_model(self.designer).model)

		self.assertEqual(self.buyer.get_ct().model, ContentType.objects.get_for_model(self.buyer).model)

class FollowTestCase(UsersModelTestCase):

	def test_cant_follow_self(self):
		# cannot follow yourself
		content_type = self.designer.get_ct()
		object_id =  self.designer.get_ct_id()

		follow = Follow(
			followee_content_type=content_type, 
			followee_object_id=object_id, 
			follower_content_type=content_type, 
			follower_object_id=object_id)

		self.assertRaises(ValidationError, follow.save)

	def test_cant_repeat_follow(self):
		# cannot follow same person more than once

		d_content_type = self.designer.get_ct()
		d_object_id =  self.designer.get_ct_id()

		b_content_type = self.buyer.get_ct()
		b_object_id =  self.buyer.get_ct_id()

		# first follow attempt
		Follow.objects.create(
			followee_content_type=d_content_type, 
			followee_object_id=d_object_id, 
			follower_content_type=b_content_type, 
			follower_object_id=b_object_id)

		# second follow attempt
		second_follow_attempt = Follow(
									followee_content_type=d_content_type, 
									followee_object_id=d_object_id, 
									follower_content_type=b_content_type, 
									follower_object_id=b_object_id)

		self.assertRaises(IntegrityError,second_follow_attempt.save)

	def test_follow_each_other(self):
		d_content_type = self.designer.get_ct()
		d_object_id =  self.designer.get_ct_id()

		b_content_type = self.buyer.get_ct()
		b_object_id =  self.buyer.get_ct_id()

		try:
			# buyer follows designer
			Follow.objects.create(
				followee_content_type=d_content_type, 
				followee_object_id=d_object_id, 
				follower_content_type=b_content_type, 
				follower_object_id=b_object_id)

			# designer follows buyer
			Follow.objects.create(
				followee_content_type=b_content_type, 
				followee_object_id=b_object_id, 
				follower_content_type=d_content_type, 
				follower_object_id=d_object_id)

			
		except:
			self.fail("Two users should be able to follow each other. Test Failed")
