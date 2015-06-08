from django import forms      
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget
#from django.utils.translation import ugettext_lazy as _

from cloudinary.forms import CloudinaryJsFileField 
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer

CHOICES = (('Designer', 'Designer'), ('Buyer', 'Buyer'))

class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect())

    class Meta:
        model   = User
        fields  = ("first_name", "last_name", "email", "username")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)

        self.fields['user_type'].label = "Are you a Designer or a Buyer?"

        for fields in self.fields.items():
            fields[1].required = True
            fields[1].widget.attrs.update({'class':'form-control', 'placeholder':fields[1].label, 'required':"True"})

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.error_messages['invalid_login'] = "Sorry your credentials were incorrect!"
        
        for fields in self.fields.items():
            fields[1].widget.attrs.update({ 'class':'form-control', 'placeholder':fields[1].label, 'required':"True"})

class EditAbstractUserForm(forms.ModelForm):
    avatar = CloudinaryJsFileField(required=False)
    class Meta:
        fields = ("bio", "location", "tags")
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'tags': TagWidget(attrs={'class':'form-control', 'placeholder':'add, tags, with, commas', 'required':'False'}),

        }
    def __init__(self, *args, **kwargs):
        super(EditAbstractUserForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class':'form-control'})

class EditDesignerForm(EditAbstractUserForm):

    class Meta(EditAbstractUserForm.Meta):
        model = Designer

class EditBuyerForm(EditAbstractUserForm):

    class Meta(EditAbstractUserForm.Meta):
        model = Buyer
        fields = EditAbstractUserForm.Meta.fields + ("boutique_name",)

class EditUserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ("first_name","last_name","email")

    def __init__(self, *args, **kwargs):
        super(EditUserForm,self).__init__(*args,**kwargs)
        for fields in self.fields.items():
            fields[1].required = True
            fields[1].widget.attrs.update({'class':'form-control', 'required':"True"})