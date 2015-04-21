from django import forms
from cloudinary.forms import CloudinaryJsFileField

from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Entry import Entry


class CreateDesignStory(forms.ModelForm):
    wip = forms.BooleanField(initial=False, label='Work in Progress?', required=False)

    class Meta:
        model = DesignStory
        fields = ("title", "description", "wip")

    def __init__(self, *args, **kwargs):
        super(CreateDesignStory, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})


class CreateEntry(forms.ModelForm):
    entry_title = forms.CharField(label='Chapter Title')
    cover_photo = CloudinaryJsFileField(label='Main Photo')
    entry_photos = CloudinaryJsFileField(attrs={'multiple': 1}, label='Supplementary Photos')

    class Meta:
        model = Entry
        fields = ("entry_title",)

    def __init__(self, *args, **kwargs):
        super(CreateEntry, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})


class EditEntryForm(forms.ModelForm):
    cover_photo = CloudinaryJsFileField(label='Main Photo', required=False)
    entry_photos = CloudinaryJsFileField(attrs={'multiple': 1}, label='Supplementary Photos',required=False)

    class Meta:
        model = Entry
        fields = ("entry_title",)

    def __init__(self, *args, **kwargs):
        super(EditEntryForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})


class EditStoryForm(forms.ModelForm):

    class Meta:
        model = DesignStory
        fields = ("title","description",)

    def __init__(self, *args, **kwargs):
        super(EditStoryForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class': 'form-control'})
