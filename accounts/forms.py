from django import forms
from django.forms.widgets import PasswordInput

class Accounts(forms.Form):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )
    )
    confirm_password = forms.CharField(
        widget = PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )
    )


class Login(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class":"form-control",
                "id":"user-password"
            }
        )
    )