from django.shortcuts import reverse, HttpResponseRedirect
from junkapp.forms import LoginForm, SignUpForm, CreateItemForm
from junkapp.models import MyUser, ItemsPost
from django.contrib.auth import login, authenticate


def obj_creator(create_type, data):
    create_dict = {}
    if create_type == 'signup':
        create_dict['signup'] = MyUser.objects.create_user(
            name=data["name"],
            username=data["username"],
            email=data["email"],
            phone=data["phone"],
            password=data['password'])
    elif create_type == 'item':
        create_dict['item'] = ItemsPost.objects.create(
            claimed=data['claimed'],
            description=data['description'],
            title=data['title'],
            email=data['email'],
            address=data['address'],
            items=data['items'])

    return create_dict[create_type]

# For forms where an object is created
def object_form_validator(request, form_type):
    form_type_dict = {
    'signup': SignUpForm(request.POST),
    'item': CreateItemForm(request.POST)
    }
    if request.method == 'POST':
        form = form_type_dict[form_type]
        if form.is_valid():
            data = form.cleaned_data
            new_obj = obj_creator(form_type, data)
            if form_type == 'signup':
                new_obj.set_password(raw_password=data['password'])
            new_obj.save()
            return HttpResponseRedirect(reverse('home'))

def login_validator(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )

# Handling standard form post request
def form_redirect(request, form_type):
    form_dict = {
        'login': login_validator(request),
        'signup': object_form_validator(request, form_type),
        'item': object_form_validator(request, form_type)
    }
    return form_dict[form_type]
