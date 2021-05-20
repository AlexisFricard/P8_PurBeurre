"""
FORMS SETTINGS
"""
from django import forms


class RegistrationForm(forms.Form):

    username = forms.CharField(label='Pseudo', max_length=50)
    first_name = forms.CharField(label='Prenom', max_length=50)
    last_name = forms.CharField(label='Nom', max_length=50)
    mail = forms.EmailField(label='Mail', max_length=50)
    password = forms.CharField(
        label='Mot de passe',
        max_length=50,
        widget=forms.PasswordInput()
        )
