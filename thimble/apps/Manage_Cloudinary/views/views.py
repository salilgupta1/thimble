from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
import cloudinary.api

@staff_member_required
def render_cloudinary(request):

    delete_orphans()
    return render(request, "manage_cloudinary.html", {})


def delete_orphans():
    result = cloudinary.api.resources(max_results=1000)

    to_be_deleted = []

    for image in result['resources']:
        pid = image['public_id']
        if "/" not in pid:
            to_be_deleted.append(pid)

    i = 0
    num_left = len(to_be_deleted)
    while num_left > 100:
        cloudinary.api.delete_resources(to_be_deleted[i:i+100])
        num_left -= 100
        i += 100

    cloudinary.api.delete_resources(to_be_deleted[i:i+num_left])
