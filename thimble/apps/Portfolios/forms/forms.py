from django import forms
from cloudinary.forms import CloudinaryJsFileField
from taggit.forms import TagWidget

from thimble.apps.Portfolios.models.schemas.Collection import Collection
from thimble.apps.Portfolios.models.schemas.Piece import Piece


class CreateCollection(forms.ModelForm):

	photos = CloudinaryJsFileField(attrs={'multiple': 1}, required=False)
	class Meta:
		model   = Collection
		fields  = ("title", "description", "tags")
		widgets = {
		    'description': forms.Textarea(attrs={'cols': 40, 'rows': 5, 'class':'form-control', 
		                                         'placeholder':'Tell the story of the collection'}),

		    'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Your Collection', 'required':'True'}),
            'tags': TagWidget(attrs={'class':'form-control', 'placeholder':'add, tags, with, commas', 'required':'True'}),
		}

class EditCollection(forms.ModelForm):
	class Meta:
		model = Collection
		fields = {"title", "description", "tags"}
		widgets = {
		    'description': forms.Textarea(attrs={'cols': 40, 'rows': 5, 'class':'form-control', 
		                                         'placeholder':'Tell the story of the collection'}),

		    'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Your Collection', 'required':'True'}),
            'tags': TagWidget(attrs={'class':'form-control', 'placeholder':'add, tags, with, commas', 'required':'True'}),
		}

class PieceForm(forms.ModelForm):
	class Meta:
		model = Piece
		fields = {"piece_title","wholesale_price","retail_price","min_quantity","product_number","details"}
		widgets = {
		    'details': forms.Textarea(attrs={'cols': 40, 'rows': 5 }),
		    'piece_title': forms.TextInput(attrs={'required':'True'}),
		}

		def __init__(self, *args, **kwargs):
			super(CreatePiece, self).__init__(*args, **kwargs)
			for fields in self.fields.items():
				fields[1].widget.attrs.update({'class':'form-control'})


