from django import forms
from cloudinary.forms import CloudinaryJsFileField

from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Entry import Entry


class CreateDesignStory(forms.ModelForm):

    class Meta:
        model   = DesignStory
        fields  = ("title", "description")
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5, 'class':'form-control', 
                                                 'placeholder':'Tell the story of the piece'}),

            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Your Story', 'required':True})
        }

class CreateEntry(forms.ModelForm):
    cover_photo     = CloudinaryJsFileField(required=True)
    entry_photos    = CloudinaryJsFileField(attrs={'multiple': 1}, required=False)

    class Meta:
        model   = Entry
        fields  = ("entry_title", "entry_desc")
        widgets = {
            'entry_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Chapter Title', 'required':True}),
            'entry_desc': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Chapter Description', 'cols':40, 'rows':3})
        }

class EditEntry(CreateEntry):
    cover_photo     = CloudinaryJsFileField(required=False)

class EditDesignStory(CreateDesignStory):
    pass