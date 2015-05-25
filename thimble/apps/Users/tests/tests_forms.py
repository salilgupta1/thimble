from django.test import TestCase
from thimble.apps.Users.forms.forms import *
from django.contrib.auth.models import User
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer

# class UserFormsTestCase(TestCase):

# 	fixtures = ['auth_user.json','users.json']
# 	def setUp(self):
# 		super(UserFormsTestCase, self).setUp()

# 		self.user = User.objects.get(pk=36)
# 		self.designer = Designer.objects.get(pk=1)
# 		self.buyer = Buyer.objects.get(pk=1)

# 	def test_edit_designer(self):
# 		edit_designer = EditDesignerForm(None, instance=self.designer)
# 		self.assertTrue(isinstance(edit_designer.instance, Designer))
# 		try:
# 			self.assertTrue(edit_designer.is_valid())
# 		except AssertionError:
# 			print "hi"
# 			for field in edit_designer.fields:
# 				print field
# 			#print edit_designer.non_field_errors()


# 	def test_edit_user(self):
# 		edit_user = EditUserForm(None, instance=self.user)
# 		self.assertTrue(edit_user.is_valid())

				


			
		