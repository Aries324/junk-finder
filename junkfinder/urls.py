"""junkfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views;
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from junkapp import views, view_helper
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.signup),
    # path('add_item/', views.create_item_view),
    path('logout/', views.logout_action, name='logout'),
    path("login/", views.login_view, name="login"),
    path('postitem/', login_required(views.PostItemView.as_view())),
    path('<int:id>/details/', views.item_detail_view),
    # on form submission, takes form_type and passes it to helper
    # function that takes the type, loads the form data, then redirects
    # to another page
    path('<str:form_type>/standard_form/', view_helper.form_redirect),
]


