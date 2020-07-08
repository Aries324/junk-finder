from django.shortcuts import reverse, HttpResponseRedirect
from junkapp.forms import create_user_form, create_item_form
from junkapp.models import MyUser, ItemsPost

def obj_creator(create_type):
    create_dict = {
        'user': MyUser.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
            ),
        'item': ItemsPost.objects.create(
            claimed=data['claimed'],
            description=data['description'],
            title=data['title'],
            email=data['email'],
            address=data['address'],
            items=data['items']
        )
    }
    return create_dict[create_type]

def form_validator(request, form_type):
    form_type_dict = {
    'user': create_user_form(request.POST),
    'item': create_item_form(request.POST)
    }

    if request.method == 'POST':
        form = form_type_dict[form_type]
        if form.is_valid():
            data = form.cleaned_data
            obj_creator(form_type)
            return HttpResponseRedirect(reverse('home'))