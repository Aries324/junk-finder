from junkapp.forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import View

from view_helper import obj_creator, form_validator
from junkapp.models import ItemsPost, MyUser
from junkapp.forms import create_user_form, PostItemForm

# Create your views here.
def login_view(request):
    html = "login.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                name=data["name"],
                username=data["username"],
                email=data["email"],
                phone=data["phone"],
                password=data['password'])
            new_user.set_password(raw_password=data['password'])
            new_user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", reverse('login')))


def index(request):
    posts = ItemsPost.objects.all()
    return render(request, 'index.html', {'posts': posts})


def item_detail_view(request, id):
    post = ItemsPost.objects.get(id=id)
    return render(request, 'item_detail.html', {'post': post})


def items_by_date_view(request):
    posts = ItemsPost.objects.order_by('-date_and_time')
    return render(request, 'items_by_date.html', {'posts': posts})

def not_claimed_view(request):
    posts = ItemsPost.objects.filter(claimed=False)
    return render(request, 'claimed.html', {'posts': posts})

def category_view(request, category):
    posts = ItemsPost.objects.filter(items=category)
    return render(request, 'category.html', {'posts': posts})

#def login_view(request):
 #   form = login_form()
   # return render(request, 'forms.html', {'form': form})

def create_user_view(request):
    form_validator('user')
    form = create_user_form()
    return render(request, 'forms.html', {'form': form})

# @login_required
# def create_item_view(request):
#     form_validator('item')
#     form = create_item_form()
#     return render(request, 'forms.html', {'form': form})


class PostItemView(View):

    def post(self, request, *args, **kwargs):
        form = PostItemForm(request.POST)
        item = form.save(commit=False)
        item.save()
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    def get(self, request, *args, **kwargs):
        form = PostItemForm()
        return render(request, 'post_item_form.html', {'form': form})
