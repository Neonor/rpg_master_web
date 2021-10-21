from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rpgmaster.forms import NewGroup
from rpgmaster.models import GroupUser

from lib import reponses

@reponses.template('rpgmaster/templates/home.html')
def home(request):
    context = {
        'rpg_master': "RPG Master : WIP",
    }
    return context

def new_group(request):
    if request.method == "POST":
        new_group = NewGroup(request.POST)
        if new_group.is_valid():
            group = new_group.save()
            user = request.user
            GroupUser(GROUP=group,USER=user,ADMIN=True).save()
            return HttpResponse("")

    template = loader.get_template('rpgmaster/templates/form/new_group.html')
    form_new_group = NewGroup()
    return HttpResponse(template.render({"new_group":form_new_group}, request))

def robots(request):
    return HttpResponse("""User-agent: *\nDisallow: /""", content_type='text/plain')