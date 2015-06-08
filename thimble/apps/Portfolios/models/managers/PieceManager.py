from django.db import models

class PieceManager(models.Manager):
    
    def get_pieces(self, collection_id, column_list):
    	try:
    		rows = self.filter(collection_id=collection_id).values(*column_list)
    		if len(rows) == 0:
    			return None
    		return rows
    	except:
    		raise