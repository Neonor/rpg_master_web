from django import forms
from rpgmaster import models as m
from django.utils.translation import gettext_lazy as _

                    # print(dir(visible.field.widget))
                    # print(visible.field.widget.input_type)

class ModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if "html_class" in dir(self.Meta):
            html_class = getattr(self.Meta, "html_class")
            for visible in self.visible_fields():
                if visible.name in html_class:
                    visible.field.widget.attrs['class'] = html_class[visible.name]
        
        if "input_type" in dir(self.Meta):
            input_type = getattr(self.Meta, "input_type")
            for visible in self.visible_fields():
                if visible.name in input_type:
                    visible.field.widget.input_type = input_type[visible.name]

class NewGroup(ModelForm):
    class Meta:
        model = m.Group
        fields = ["NAME"]
        labels = {
            'NAME': _('name'),
        }
        