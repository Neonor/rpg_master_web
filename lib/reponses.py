from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.urls import resolve,reverse

from importlib import reload

# from . import traduction

from menus import menu_left


def template(link_template):
    template = loader.get_template(link_template)
    def http_reponse(func):
        def wrapper(request):
            context = func(request)
            return HttpResponse(template.render(context, request))
        return wrapper
    return http_reponse

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
