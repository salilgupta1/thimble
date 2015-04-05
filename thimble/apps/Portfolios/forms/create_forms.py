from django import forms     

from cloudinary.forms import CloudinaryJsFileField 
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Entry import Entry


class DesignStoryForm(forms.ModelForm):
	class Meta:
		model = DesignStory
		fields = ("name",)

	def __init__(self, *args, **kwargs):
		super(DesignStoryForm, self).__init__(*args, **kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})

class EntryForm(forms.ModelForm):
	cover_photo = CloudinaryJsFileField()
	entry_photos = CloudinaryJsFileField(attrs={'multiple':1})
	num_photos = forms.IntegerField(label="", help_text="", widget=forms.HiddenInput())

	class Meta:
		model = Entry
		fields = ("context","date","cover_photo","num_photos")

	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})
