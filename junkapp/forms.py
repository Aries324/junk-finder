from django import forms


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
    pass
