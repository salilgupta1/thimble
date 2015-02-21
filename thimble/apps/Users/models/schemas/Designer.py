from django.db import models
from django.contrib.auth.models import User
from thimble.apps.Users.models.managers.DesignerManager import DesignerManager
from cloudinary.models import CloudinaryField

class Designer(models.Model):
	user = models.OneToOneField(User)

	# Designer specific fields
	designer_id = models.AutoField(primary_key=True)
	text_bio = models.TextField()

	# not required
	prof_pic = CloudinaryField('image')
	
	MALE = "M"
	FEMALE = "F"
	PNT = "NA",
	OTHER = "OT"
	GENDER = (
	        (MALE,"Male"),
	        (FEMALE,"Female"),
	        (PNT,"Prefer not to Disclose"),
	        (OTHER,"Other"))

	# not required
	gender = models.CharField(max_length=2, choices=GENDER, default=MALE, blank=True, null=False)

	# not required
	age = models.PositiveSmallIntegerField(blank=True, null=True)

	# not required
	location = 	models.CharField(max_length=200, blank=True)

	subdomain = models.SlugField(unique=True)
	template_theme = models.CharField(max_length=30)

	# connect the manager
	objects = DesignerManager()

	class Meta:
	    app_label='Users'