from django.test import TestCase

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer
from ..models.schemas.Collection import Collection
from ..models.schemas.Piece import Piece
from ..models.schemas.Like import Like
from ..models.schemas.Comment import Comment

class PortfoliosManagerTestCase(TestCase):
	fixtures = ['portfolio_test_data.json', 'auth_user.json','users.json']

	def setUp(self):
		super(PortfoliosManagerTestCase, self).setUp()
		self.designer = Designer.objects.get(pk=1)
		self.buyer = Buyer.objects.get(pk=1)
		self.collection = Collection.objects.get(pk=1)
		self.collection_2 = Collection.objects.get(pk=2)
		self.comment = Comment.objects.get(pk=1)
		self.like = Like.objects.get(pk=2)

class CollectionManagerTestCase(PortfoliosManagerTestCase):

	def test_get_collections(self):
		good_data = Collection.objects.get_collections(self.designer.user)
		for collection in good_data:
			for key in collection.keys():
				if collection['id'] == 1:
					self.assertEquals(collection[key], getattr(self.collection, key)) 
				elif collection['id'] == 2:
					self.assertEquals(collection[key], getattr(self.collection_2, key))

		bad_data = Collection.objects.get_collections("test_user")
		self.assertEquals(bad_data, None)

	def test_get_collection(self):
		good_data = Collection.objects.get_collection(self.collection.pk)
		for key in good_data.keys():
			self.assertEquals(good_data[key], getattr(self.collection, key)) 

		bad_data = Collection.objects.get_collection(234234)
		self.assertEquals(bad_data, None)

	def test_update_likes(self):
		like_count = self.collection.likes

		Collection.objects.update_likes(self.collection.pk, True)
		new_like_count = Collection.objects.filter(pk=self.collection.pk).values("likes")[0]['likes']
		self.assertEqual(like_count + 1, new_like_count)

		Collection.objects.update_likes(self.collection.pk, False)
		new_like_count = Collection.objects.filter(pk=self.collection.pk).values("likes")[0]['likes']
		self.assertEqual(like_count, new_like_count)

	def test_update_comment(self):
		comment_count = self.collection.comments

		Collection.objects.update_comments(self.collection.pk, True)
		new_comment_count = Collection.objects.filter(pk=self.collection.pk).values("comments")[0]['comments']
		self.assertEqual(comment_count + 1, new_comment_count)

		Collection.objects.update_comments(self.collection.pk, False)
		new_comment_count = Collection.objects.filter(pk=self.collection.pk).values("comments")[0]['comments']
		self.assertEqual(comment_count, new_comment_count)

class LikeManagerTestCase(PortfoliosManagerTestCase):

	def test_get_favorites(self):
		num_favs = Like.objects.get_favorites(self.designer)

		# test will only work if self.designer likes 1 collection
		# only for testing purposes
		self.assertTrue(isinstance(num_favs, (int, long)))
		self.assertEqual(num_favs, 1)

	def test_get_likes(self):
		likes = Like.objects.get_likes(self.designer, [self.collection.pk, self.collection_2.pk])

		# test will only work if self.designer specifically only likes self.collection
		# only for testing purposes

		self.assertEqual(likes[0], self.collection.pk)

class CommentManagerTestCase(PortfoliosManagerTestCase):
	def test_get_comments(self):
		bad_data = Comment.objects.get_comments(1000000)
		self.assertEqual(bad_data, None)

		good_data = Comment.objects.get_comments(self.collection.pk)[0]
		self.assertEqual(good_data['object_id'], self.designer.pk)
		self.assertEqual(good_data['content_type_id'], self.designer.get_ct().id)
