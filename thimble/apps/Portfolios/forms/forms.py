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

class CreateEntry(forms.ModelForm):
    entry_title     = forms.CharField(label='Chapter Title', required=True, max_length=60)
    entry_desc      = forms.CharField(label='Chapter Description', required=False)
    cover_photo     = CloudinaryJsFileField(label='Cover Photo')
    entry_photos    = CloudinaryJsFileField(attrs={'multiple': 1}, label='Additional Photos')

    class Meta:
        model   = Entry
        fields  = ("entry_title", "entry_desc")
        error_messages={
            'entry_title':{
                'max_length':"Please limit your title to 60 characters"
            },
        }

    def __init__(self, *args, **kwargs):
        super(CreateEntry, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})

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
