from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def render_cloudinary(request): #show list of all objects
    context = {}
    return render(request, "manage_cloudinary.html",context)