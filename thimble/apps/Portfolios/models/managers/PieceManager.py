from django.db import models

class PieceManager(models.Manager):
    
    def get_pieces(self, collection_id):
    	try:
    		rows = self.filter(collection_id=collection_id).values('piece_id','piece_title','front_view')
    		if len(rows) == 0:
    			return None
    		return rows
    	except:
    		raise