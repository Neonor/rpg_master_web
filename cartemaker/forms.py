from django import forms
from cartemaker import models as m
from rpgmaster.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class UploadCarte(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class BgHexagone(ModelForm):
    class Meta:
        model = m.BgHexagone
        fields = ["BG_COLOR","BD_COLOR","PATH_FILE"]
        labels = {
            'BG_COLOR': _('bg_color'),
            'BD_COLOR': _('bd_color'),
            'PATH_FILE': _('path_file'),
        }
        html_class = {
            'BG_COLOR' : 'venue_type_select'
        }
        input_type = {
            'BG_COLOR' : 'color',
            'BD_COLOR' : 'color'
        }    
        error_messages = {
            'BD_COLOR': {
                'max_length': _("This writer's name is too long."),
            },
        }

class FromNewHexaMap(ModelForm):
    """ Création/Modification d'une map """
    class Meta:
        model = m.HexaMap
        fields = ["NAME"]

class FormHexa(forms.Form):
    """ Création/Modification d'une case """