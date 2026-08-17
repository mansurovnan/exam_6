from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    conf_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [ "first_name",
            "last_name",
            "username",
            "email",
            "password",
            'tel_number',
            'address',
                ]
    def clean(self):
        data = super().clean()

        password = data.get("password")
        conf_password = data.get("conf_password")

        if password and conf_password and password != conf_password:
                raise forms.ValidationError(
                    "Parollar mos emas"
                )

        return data
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username and username[0].isdigit():
                raise forms.ValidationError(
                    "Username raqam bilan boshlanmasin"
                )

        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "tel_number",
            "address",
        ]

    