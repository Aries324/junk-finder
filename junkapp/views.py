from junkapp.forms import LoginForm, SignUpForm, CreateItemForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic.detail import View

from junkapp.view_helper import obj_creator, object_form_validator, login_validator
from junkapp.models import ItemsPost, MyUser
from junkapp.forms import SignUpForm, PostItemForm
from django.views.generic.edit import CreateView


# Regarding additional text that might be needed for individual
# form views, it would be necessary to define them in the view
# and add them to the render dictionary.


def login_view(request):
    if request.method == "POST":
        return login_validator(request)
    else:
        form = LoginForm()
        return render(request, 'forms.html', {"form": form,
                                              'isSignupShown': True})


def signup(request):
    if request.method == "POST":
        return object_form_validator(request, 'signup')
    else:
        form = SignUpForm()
        return render(request, 'forms.html', {'form': form,
                                              'isLoginShown': True})


# Class based view
class HomeView(CreateView):
    def get(self, request):
        context = {
            'data': ItemsPost.objects.all()
        }
        return render(request, 'home.html', context)


@login_required(login_url='/login/')
def home(request):
    posts = ItemsPost.objects.all()
    return render(request, 'home.html', {'data': posts})


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", reverse('login')))


def item_detail_view(request, id):
    post = ItemsPost.objects.get(id=id)
    return render(request, 'item_detail.html', {'post': post})


def items_by_date_view(request):
    posts = ItemsPost.objects.order_by('-date_and_time')
    return render(request, 'items_by_date.html', {'posts': posts, 'category': 'By Date'})


def not_claimed_view(request):
    posts = ItemsPost.objects.filter(claimed=False)
    return render(request, 'claimed.html', {'posts': posts, 'category': 'Not Claimed'})


def category_view(request, category):
    posts = ItemsPost.objects.filter(items=category)
    return render(request, 'category.html', {'posts': posts, 'category': category})


def create_user_view(request):
    form_validator('user')
    form = create_user_form()
    return render(request, 'forms.html', {'form': form})



class PostItemView(View):

    def post(self, request, *args, **kwargs):
        form = PostItemForm(request.POST)
        item = form.save(commit=False)
        item.save()
        form.save()
        return HttpResponseRedirect(reverse('home'))

    def get(self, request, *args, **kwargs):
        form = PostItemForm()
        return render(request, 'post_item_form.html', {'form': form})

