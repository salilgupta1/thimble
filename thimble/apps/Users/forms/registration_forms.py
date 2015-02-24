from django import forms      
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from cloudinary.forms import CloudinaryJsFileField 
from thimble.apps.Users.models.schemas.Designer import Designer


class DesignerRegistrationForm(forms.ModelForm):

  # pass the folder and public_id attribute in upon upload
  prof_pic = CloudinaryJsFileField()

  class Meta:
      model = Designer
      fields = ("subdomain","template_theme","prof_pic")

  def __init__(self, *args, **kwargs):
  	super(DesignerRegistrationForm, self).__init__(*args, **kwargs)
  	for fields in self.fields.items():
  		fields[1].widget.attrs.update({'class':'form-control'})
  

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(error_messages = {"invalid":"The email given is not valid!", "required":"Please input an email"})
    first_name = forms.CharField(max_length = 50, error_messages = {'required':"You must have a first name right?","max_length":"There is no way that your first name is that long...."})
    last_name = forms.CharField(max_length = 50, error_messages = {'required':"You must have a last name right?","max_length":"There is no way that your last name is that long...."})
    username = forms.CharField(max_length = 50, error_messages = {'required':"A username is required.","max_length":"Your username is too long."})

    class Meta:
        model = User
        fields = ("first_name","last_name","email","username")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class':'form-control'})  