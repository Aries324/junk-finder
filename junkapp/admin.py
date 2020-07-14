from django.contrib import admin
from junkapp.models import ItemsPost, MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = MyUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )

admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(ItemsPost)

