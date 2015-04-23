from django import forms
from cloudinary.forms import CloudinaryJsFileField

from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Entry import Entry


class CreateDesignStory(forms.ModelForm):

    class Meta:
        model   = DesignStory
        fields  = ("title", "description")
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10, 'class':'form-control', 
                                                 'placeholder':'Tell the story of the piece','required':True}),

            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Your Story', 'required':True})
        }
        error_messages = {
            "NON_FIELD_ERRORS": {
                'unique_together':"Sorry, you are already using this Story Title"
            }
        }

class CreateEntry(forms.ModelForm):
    cover_photo     = CloudinaryJsFileField(label='Cover Photo', required=True)
    entry_photos    = CloudinaryJsFileField(attrs={'multiple': 1}, label='Additional Photos')

    class Meta:
        model   = Entry
        fields  = ("entry_title", "entry_desc")
        widgets = {
            'entry_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Chapter Title', 'required':True}),
            'entry_desc': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Chapter Description', 'cols':40, 'rows':3, 'required':False})
        }
        error_messages = {
            "NON_FIELD_ERRORS": {
                'unique_together':"Sorry, you are already using this Chapter Title"
            }
        }

class EditEntryForm(forms.ModelForm):
    cover_photo     = CloudinaryJsFileField(label='Cover Photo', required=False)
    entry_photos    = CloudinaryJsFileField(attrs={'multiple': 1}, label='Additional Photos', required=False)

    class Meta:
        model   = Entry
        fields  = ("entry_title", "entry_desc")

    def __init__(self, *args, **kwargs):
        super(EditEntryForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})

class EditStoryForm(forms.ModelForm):

    class Meta:
        model   = DesignStory
        fields  = ("title","description",)

    def __init__(self, *args, **kwargs):
        super(EditStoryForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})