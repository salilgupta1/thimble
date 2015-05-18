from django.db import models
from thimble.apps.Portfolios.models.managers.PieceManager import PieceManager

class Piece(models.Model):
	collection		= models.ForeignKey('Portfolios.Collection', on_delete=models.CASCADE)
	piece_id		= models.AutoField(primary_key=True)
	piece_title		= models.CharField(max_length=60, default='', blank=True)	
	date_created	= models.DateField(auto_now_add=True)

	#bucket_link		= models.CharField(max_length=255, null=False, default='', blank=True) 
	#cover_photo		= models.CharField(max_length=255, null=False, default='', blank=True)

	front_view		= models.CharField(max_length=255, null=False, default='', blank=True)
	back_view 		= models.CharField(max_length=255, null=False, default='', blank=True)
	#piece_desc		= models.TextField(default='', blank=True, max_length=200) 

	# connect the manager
	objects = PieceManager()

	class Meta:
	    app_label ='Portfolios'