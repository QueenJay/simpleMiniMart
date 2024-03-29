from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class ContactForm(forms.Form):
    fullname    = forms.CharField(
                widget=forms.TextInput(
                    attrs = {
                        "class": "form-control",
                        "placeholder" : "Your full name"
                    }
                )
    )
    email       = forms.EmailField(
                widget=forms.EmailInput(
                    attrs = {
                        "class": "form-control",
                        "placeholder" : "Your full name"
                    }
                )
    )
    content     = forms.CharField(
                widget=forms.TextInput(
                    attrs = {
                        "class": "form-control",
                        "placeholder" : "Your full name"
                    }
                )
    )

class LoginForm(forms.Form):
    username    =forms.CharField()
    password    =forms.CharField(
            widget =forms.PasswordInput()
            )


class RegisterForm(forms.Form):
    username    =forms.CharField()
    email       = forms.EmailField(
                widget=forms.EmailInput(
                    attrs = {
                        "class": "form-control",
                        "placeholder" : "Your email"
                    }
                )
    )
    password    =forms.CharField(
            widget =forms.PasswordInput()
            )
    
    password2    =forms.CharField(label = "Confirm Password",
            widget =forms.PasswordInput()
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username= username)
        if qs.exists():
            raise forms.ValidationError('Username taken!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(username= email)
        if qs.exists():
            raise forms.ValidationError('Email taken!')
        return email

    def clean(self):
        data        =self.cleaned_data
        password    =self.cleaned_data.get('password')
        password2   =self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data