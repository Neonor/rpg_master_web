from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.urls import resolve,reverse

from django.utils.translation import gettext_lazy as _

from menus import menu_left


def template(link_template,css=[],js=[]):
    template = loader.get_template(link_template)
    def http_reponse(func):
        def wrapper(request):
            context = func(request) or {}
            menu = [[name,link,icon,reverse(link) == request.path] for name,link,icon,*_ in menu_left]
            context["menu_enter"] = menu
            context["css"] = css
            context["js"] = js
            return HttpResponse(template.render(context, request))
        return wrapper
    return http_reponse

class Render():
    def __init__(self):
        self.__css = []
        self.__js = []



    def css(self,*css):
        self.__css = list(css)
        def wrap(func):
            return func
        return wrap

    def js(self,*js):
        self.__js = list(js)
        def wrap(func):
            return func
        return wrap    


# def trad(func):
#     def wrapper(request):
#         context = func(request)
#         if settings.DEBUG:
#             reload(traduction)
#         if isinstance(context,dict):
#             context["trad"] = traduction.Translate(request)
#         else:
#             context = {"trad":traduction.Translate(request)}
#         return context
#     return wrapper

def menu(func):
    def wrapper(request):
        context = func(request)

        menu = [[name,link,icon,reverse(link) == request.path] for name,link,icon,*_ in menu_left]
        context_menu = {"menu_enter":menu}
        context_menu.update(context)
        template = loader.get_template('rpgmaster/templates/menu.html')
        template.render(context, request)
        
        if isinstance(context,dict):
            context["menu"] = template.render(context_menu, request)
        else:
            context = {"menu":template.render(context_menu, request)}
        return context
    return wrapper
