from django.contrib import admin
from junkapp.models import ItemsPost, MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(MyUser, UserAdmin)
admin.site.register(ItemsPost)

