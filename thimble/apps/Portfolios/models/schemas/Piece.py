from django.db import models
from thimble.apps.Portfolios.models.managers.PieceManager import PieceManager

class Piece(models.Model):
	collection		= models.ForeignKey('Portfolios.Collection', on_delete=models.CASCADE)
	piece_id		= models.AutoField(primary_key=True)
	piece_title		= models.CharField(max_length=60, default='', blank=True)
	date_created	= models.DateField(auto_now_add=True)
	front_view		= models.CharField(max_length=255, null=False, default='', blank=True)
	back_view 		= models.CharField(max_length=255, null=False, default='', blank=True)
	
	wholesale_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	retail_price 	= models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	min_quantity 	= models.PositiveIntegerField(null=True, blank=True)
	product_number 	= models.CharField(default='', blank=True, max_length=255)
	details 		= models.TextField(default='', blank=True)
	
	# connect the manager
	objects = PieceManager()

	class Meta:
	    app_label ='Portfolios'