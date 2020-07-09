from junkapp.forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import MyUser
from django.contrib.auth.decorators import login_required

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
