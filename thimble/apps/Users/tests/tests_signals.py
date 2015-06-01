import mock
from django.test import TestCase

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer
from thimble.apps.Users.models.schemas.Follow import Follow
from django.db.models.signals import post_save, post_delete


class UserSignalsTestCase(TestCase):
	fixtures = ['auth_user.json','users.json']
	def setUp(self):
		super(UserSignalsTestCase, self).setUp()
		self.designer = Designer.objects.get(pk=1)
		self.buyer = Buyer.objects.get(pk=1)


	def test_follow_signal_on_save(self):

		with mock.patch('thimble.apps.Users.signals.handlers.change_follow', autospec=True) as mocked_handler:
			post_save.connect(mocked_handler, sender=Follow)
			d_content_type = self.designer.get_ct()
			d_object_id =  self.designer.pk

			b_content_type = self.buyer.get_ct()
			b_object_id =  self.buyer.pk

			Follow.objects.create(
				followee_content_type=b_content_type, 
				followee_object_id=b_object_id, 
				follower_content_type=d_content_type, 
				follower_object_id=d_object_id)

	    # Check that your signal was called.
		self.assertTrue(mocked_handler.called)

	    # Check that your signal was called only once.
		self.assertEqual(mocked_handler.call_count, 1)


	# def test_follow_signal_on_delete(self):
	# 	with mock.patch('thimble.apps.Users.signals.handlers.change_follow', autospec=True) as mocked_handler:
	# 		post_delete.connect(mocked_handler, sender=Follow)
