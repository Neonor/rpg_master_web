from django.urls import resolve
from django.conf import settings

from os import path

class Translate(object):
    """ gestion des languages """
    def __init__(self,request):
        langs = [value for value in request.META["HTTP_ACCEPT_LANGUAGE"].replace(",",";").split(";") if not "q=" in value]

        base_lang_folder = path.join(settings.PROJECT_ROOT,"lang")
        if resolve(request.path).app_name:
            app_lang_folder = path.join(settings.BASE_DIR,resolve(request.path).app_name,"lang")
        else:
            app_lang_folder = None

        base_lang = None
        app_lang = None

        for lang in langs:
            if not base_lang and path.isfile(path.join(base_lang_folder,lang)):
                base_lang = path.join(base_lang_folder,lang)
            if app_lang_folder and not app_lang and path.isfile(path.join(app_lang_folder,lang)):
                app_lang = path.join(app_lang_folder,lang)
            if base_lang and app_lang:
                break

        for name,value in self._load_files(base_lang):
            setattr(self,name.strip(),value.strip())
        if app_lang:
            for name,value in self._load_files(app_lang):
                setattr(self,name.strip(),value.strip())

    def _load_files(self,filename):
        with open(filename) as f_lang:
            raw_lang = f_lang.read()
        
        trad = []
        for enter in raw_lang.split("\n"):
            if "::" in enter:
                trad.append(enter.split("::"))
            elif trad and enter:
                trad[-1][-1] += "\n" + enter
        return trad
