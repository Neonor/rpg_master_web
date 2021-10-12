from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from lib import reponses

@reponses.template('rpgmaster/templates/home.html')
@reponses.menu
@reponses.trad
def home(request):
    template = loader.get_template('rpgmaster/templates/home.html')
    context = {
        'rpg_master': "RPG Master : WIP",
    }
    return context

def robots(request):
    return HttpResponse("""User-agent: *\nDisallow: /""", content_type='text/plain')