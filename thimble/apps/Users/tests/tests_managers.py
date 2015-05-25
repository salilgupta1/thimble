from django.test import TestCase

from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from django.contrib.auth.models import User
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer
from thimble.apps.Users.models.schemas.Follow import Follow


class UsersManagerTestCase(TestCase):
	fixtures = ['auth_user.json','users.json']

	def setUp(self):
		super(UsersManagerTestCase, self).setUp()
		self.user = User.objects.get(pk=36)
		self.designer = Designer.objects.get(pk=1)
		self.buyer = Buyer.objects.get(pk=1)

	def test_get_designer_info(self):
		data = Designer.objects.get_designer_info(self.designer.user)
		self.assertEqual(data, self.designer)
		
		bad_data = Designer.objects.get_designer_info('dummy')
		self.assertEqual(bad_data, None)

	def test_update_following(self):
		following_count = self.designer.following
		Designer.objects.update_following(self.designer.pk, True)
		new_following_count = Designer.objects.filter(pk=1).values("following")[0]['following']
		self.assertEqual(following_count + 1, new_following_count)

		Designer.objects.update_following(self.designer.pk, False)
		new_following_count = Designer.objects.filter(pk=1).values("following")[0]['following']
		self.assertEqual(following_count, new_following_count)

	def test_update_followers(self):
		follower_count = self.designer.followers
		Designer.objects.update_followers(self.designer.pk, True)
		new_follower_count = Designer.objects.filter(pk=1).values("followers")[0]['followers']
		self.assertEqual(follower_count + 1, new_follower_count)

		Designer.objects.update_followers(self.designer.pk, False)
		new_followers_count = Designer.objects.filter(pk=1).values("followers")[0]['followers']
		self.assertEqual(follower_count, new_followers_count)


