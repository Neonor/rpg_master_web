from django import forms
from django.utils.translation import gettext_lazy as t

class UploadCarte(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class FromNewHexaMap(forms.Form):
    """ Création/Modification d'une map """
    map_name = forms.CharField(label="")

class FormHexa(forms.Form):
    """ Création/Modification d'une case """