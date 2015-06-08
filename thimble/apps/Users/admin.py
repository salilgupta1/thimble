from django.contrib import admin
from models.schemas import Designer, Follow, Buyer

# Register your models here.
admin.site.register(Buyer.Buyer)
admin.site.register(Designer.Designer)
admin.site.register(Follow.Follow)