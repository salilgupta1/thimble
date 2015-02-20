from django.forms import ModelForm      
from cloudinary.forms import CloudinaryJsFileField      
from thimble.apps.Portfolios.models.schemas.Photo import Photo

class PhotoDirectForm(ModelForm):
  class Meta:
      model = Photo
  image = CloudinaryJsFileField()