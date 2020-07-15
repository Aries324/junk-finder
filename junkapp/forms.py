from django import forms
from junkapp.models import ItemsPost


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class CreateItemForm(forms.Form):
    ITEM_CHOICES = (
        ('FURNITURE', 'Furniture'),
        ('ELECTRONICS', 'Electronics'),
        ('HOME_IMPROVEMENT', 'Home_Improvement'),
        ('SCRAPS', 'Scraps'),
        ('CLOTHING', 'Clothing')

    )
    claimed = forms.BooleanField()
    description = forms.CharField(widget=forms.Textarea)
    title = forms.CharField(max_length=200)
    address = forms.URLField()
    items = forms.ChoiceField(choices=ITEM_CHOICES)
