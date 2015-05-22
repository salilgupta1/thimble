from django.test import TestCase
from django.core.urlresolvers import reverse
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer
from thimble.apps.Users.forms.forms import *

# test the views 
class UsersViewsTestCase(TestCase):
	fixtures = ['auth_user.json', 'users.json']

	def test_create_account(self):
		response = self.client.get(reverse('Users:create_account'))
		self.assertEqual(response.status_code, 200)
		self.assertTrue("register_form" in response.context)

	def test_edit_account(self):

		# make sure Buyer form shows up
		self.client.login(username="sdasbooty",password='test')
		response = self.client.get(reverse('Users:edit_account', args=('Buyer',)))

		self.assertTrue(response.status_code, 200)
		self.assertTrue(isinstance(response.context['abstract_user_form'], EditBuyerForm))

		self.client.logout()

		# make sure Designer form shows up
		self.client.login(username="devpat", password='test')
		response = self.client.get(reverse('Users:edit_account', args=('Designer',)))
		self.assertTrue(response.status_code, 200)
		self.assertTrue(isinstance(response.context['abstract_user_form'], EditDesignerForm))


