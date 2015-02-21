from django import forms      
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import CloudinaryJsFileField      
from thimble.apps.Users.models.schemas.Designer import Designer
from django.contrib.auth.models import User

class DesignerRegistrationForm(forms.ModelForm):
  prof_pic = CloudinaryJsFileField(required=False)

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

    class Meta:
        model = User
        fields = ("first_name","last_name","email",)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for fields in self.fields.items():
            fields[1].widget.attrs.update({'class':'form-control'})  