from django.test import TestCase
from django.db import IntegrityError, transaction
from ..models.schemas.Collection import Collection
from ..models.schemas.Comment import Comment
from ..models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer

class PortfoliosModelTestCase(TestCase):
	fixtures = ['portfolio_test_data.json', 'auth_user.json','users.json']

	def setUp(self):
		super(PortfoliosModelTestCase, self).setUp()
		self.designer = Designer.objects.get(pk=1)
		self.buyer = Buyer.objects.get(pk=1)
		self.collection = Collection.objects.get(pk=1)
		self.collection_2 = Collection.objects.get(pk=2)
		self.comment = Comment.objects.get(pk=1)
		self.like = Like.objects.get(pk=2)


class CollectionTestCase(PortfoliosModelTestCase):

	def test_collection_unique_together(self):
		with transaction.atomic():
			faulty_collection = Collection(self.collection.designer.pk,self.collection.title)
			self.assertRaises(IntegrityError, faulty_collection.save)

		try:
			Collection.objects.create(designer_id=self.collection.designer.pk, title="New Collection")
		except:
			self.fail("Unique Together check isn't working as planned for Collection table")

class CommentTestCase(PortfoliosModelTestCase):
	def test_anyone_can_comment_collection(self):
		try:
			Comment.objects.create(commenter=self.buyer, collection = self.collection_2)
			Comment.objects.create(commenter=self.designer, collection = self.collection_2)
		except:
			self.fail("both buyers and designers should be able to comment on a collection")

class LikeTestCase(PortfoliosModelTestCase):
	
	def test_like_unique_together(self):
		with transaction.atomic():
			faulty_like = Like(liker=self.designer, collection=self.collection)
			self.assertRaises(IntegrityError, faulty_like.save)

		try:
			Like.objects.create(liker=self.buyer, collection = self.collection)
		except:
			self.fail("Unique Together check isn't working as planned for Like table")

	def test_anyone_can_like_collection(self):
		try:
			Like.objects.create(liker=self.buyer, collection = self.collection_2)
			Like.objects.create(liker=self.designer, collection = self.collection_2)
		except:
			self.fail("both buyers and designers should be able to like a collection")

class PieceTestCase(PortfoliosModelTestCase):
	pass
