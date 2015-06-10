from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from thimble.apps.Users.forms.forms import *

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer

from cloudinary.forms import cl_init_js_callbacks

from thimble.utils import photo_rename

def create_account(request):
    reg_form = RegistrationForm(request.POST or None, label_suffix="")
    if request.method == "POST":
        
        if reg_form.is_valid():

            # create an instance of the user model
            new_user = reg_form.save()
            user_type = request.POST.get("user_type")
            if user_type == "Designer":
                # create a designer instance
                designer = Designer.objects.create(user=new_user)
            else:
                # create a buyer instance
                buyer = Buyer.objects.create(user=new_user)

            # login user after account is created
            user = authenticate(username=reg_form.cleaned_data['username'],
                                password=reg_form.cleaned_data['password1'])
            login(request, user)

            # send them to edit their profile
            return HttpResponseRedirect(reverse('Users:edit_account', args=(user_type,)))

    context = {"register_form":reg_form}
    return render(request, "Users/create_account.html", context)

@login_required
def edit_account(request, user_type):
    context = {}

    user_form = EditUserForm(request.POST or None, instance=request.user, label_suffix="")
    
    if user_type == "Designer":
        abstract_user_form = EditDesignerForm(request.POST or None, instance=request.user.designer, label_suffix="")
    else:
        abstract_user_form = EditBuyerForm(request.POST or None, instance=request.user.buyer, label_suffix="")
    
    if request.method == "POST":
        if user_form.is_valid() and abstract_user_form.is_valid():

            # save forms if valid
            user = user_form.save()
            abstract_user = abstract_user_form.save(commit=False)

            # rename avatar link to a folder
            if request.POST.get("avatar") is not None:
                avatar_link = request.user.username
                avatar_link = photo_rename(avatar_link, [request.POST.get("avatar")])[0]
                abstract_user.avatar = avatar_link

            abstract_user.save()

            context['changes_saved'] = "Changes saved."

    context['user_form'] = user_form
    context['abstract_user_form'] = abstract_user_form
    context['action'] = request.path
    cl_init_js_callbacks(context['abstract_user_form'], request)

    return render(request, "Users/edit_account.html", context)
