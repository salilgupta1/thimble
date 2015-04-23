from django import forms      
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from cloudinary.forms import CloudinaryJsFileField 
from thimble.apps.Users.models.schemas.Designer import Designer

class RegistrationForm(UserCreationForm):

    class Meta:
        model   = User
        fields  = ("first_name", "last_name", "email", "username")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        
        for fields in self.fields.items():
            fields[1].required = True
            fields[1].widget.attrs.update({'class':'form-control', 'placeholder':fields[1].label, 'required':True})

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.error_messages['invalid_login'] = "Sorry your credentials were incorrect!"
        
        for fields in self.fields.items():
            fields[1].widget.attrs.update({ 'class':'form-control', 'placeholder':fields[1].label, 'required':True})

class EditDesignerForm(forms.ModelForm):
    avatar = CloudinaryJsFileField(required=False)

    class Meta:
        model  = Designer
        fields = ("bio","location")
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }
    def __init__(self, *args, **kwargs):
        super(EditDesignerForm, self).__init__(*args, **kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class':'form-control'})

class EditUserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ("first_name","last_name","email","username")

    def __init__(self, *args, **kwargs):
        super(EditUserForm,self).__init__(*args,**kwargs)
        for fields in self.fields.items():
            fields[1].required = True
            fields[1].widget.attrs.update({'class':'form-control', 'required':True})
